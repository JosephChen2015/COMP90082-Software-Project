# -*- coding: utf-8 -*-
"""
Main flask application with all the routes
"""

import firebase as firebase
from flask import Flask, request, jsonify
import config
from datetime import datetime
import imgUtils
from faceUtils import FaceUtils
import traceback
import logging

firebase = firebase.Firebase(config.firebaseConfig)
storage = firebase.storage()
database = firebase.database()
faceUtils = FaceUtils()

app = Flask(__name__)
app.config.from_object(config)

# Error messages to be sent if the user passes in invalid json or error on image processing possibly due to bad data
errorInvalidJson = {"Error": "Failed to parse json, invalid format"}
errorClassificationFailed = {"Error": "Failed to process image, try another image"}

@app.route('/recog/recogUploadApi', methods=['GET', 'POST'])
def recogUploadApi():
    """
    REST API which recognises all faces in an image and uploads the results to Real-time Database and Storage.
    recogUploadApi accepts JSON as input. Input must contain:
        imageBase64: Base64 encoded image
        uid: The user ID
        date: The upload date
    The API returns a JSON in the format of:
        {
         imageUrl: "The URL of the Base64 encoded image with bounding boxes labelled by their names"
         classified: "Boolean value of whether face(s) is classified in the image"
         results: "List of {
                            "{
                              name: "the name "
                              probability: "the highest probability"
                             }" (for each detected face only if it is classified)
                           }"
        }
    """

    try:
        requestJson = request.json
        imgBase64 = requestJson["imageBase64"]
        userId = requestJson["uid"]
    except:
        return jsonify(errorInvalidJson)

    try:
        rgbImg = imgUtils.base64StringToRgb(imgBase64)
        classified, nameProb, imgBuffer = faceUtils.face_match_img(rgbImg)
        # classified, nameProb, imgBuffer = faceUtils.face_match_img("./Web/App/unknowns/test.jpg")

        # Get the classification time
        time = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

        # Upload the classification result to Real-time Database
        entryName = database.child('users/' + userId + '/' + 'recognitions').push({
            "date": time, "results": nameProb, "userId": userId})["name"]

        # Upload the labelled image to Storage
        storage.child('imageLabelUploads/' + userId + '/' + entryName + '/' + 'label.jpg').put(imgBuffer)

        # Upload the labelled image url to Real-time Database
        imgUrl = storage.child('imageLabelUploads/' + userId + '/' + entryName + '/' + 'label.jpg').get_url(None)
        database.child('users/' + userId + '/' + 'recognitions/' + entryName).update({"imageUrl": imgUrl})

        # Only upload the result of each image to a separate directory
        database.child('recognitions').push({"results": nameProb, "imageUrl": imgUrl})

        message = {"imageUrl": imgUrl, "classified": classified, "results": nameProb}
        return jsonify(message)
    except Exception as e:
        print('str(Exception):\t', str(Exception))
        print('str(e):\t\t', str(e))
        print('repr(e):\t', repr(e))
        print('traceback.print_exc():')
        traceback.print_exc()
        print('traceback.format_exc():\n%s' % traceback.format_exc())
        return jsonify(errorClassificationFailed)

# Main function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
