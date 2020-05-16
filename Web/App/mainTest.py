# -*- coding: utf-8 -*-
"""
Main flask application with all the routes
"""

import firebase as firebase
from flask import Flask, request, redirect, flash, url_for, session, jsonify
import config
import json
import requests
import imgUtils
# from faceUtils import FaceUtils

firebase = firebase.Firebase(config.firebaseConfig)
storage = firebase.storage()
database = firebase.database()
# auth = firebase.auth()

app = Flask(__name__)
app.config.from_object(config)

# HTML to be shown to the unregistered user if they try to access a page only accessible for signed in users
# ASK_LOGIN_TEXT = "You must log in to access this page!<br><a href = '/login'></b>click here to log in</b></a>"

# Error messages to be sent if the user passes in invalid json or error on image processing possibly due to bad data
errorInvalidJson = {"Error": "Failed to parse json, invalid format"}
errorClassificationFailed = {"Error": "Failed to process image, try another image"}


# # Index page
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if 'email' in session:
#         return render_template('home.html', username=session.get('email'))
#     return render_template('index.html')
#
# # Login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if 'email' not in session:
#         if request.method == "POST":
#             user_info = request.form.to_dict()
#             email = user_info.get("email")
#             password = user_info.get("password")
#
#             try:
#                 user = auth.sign_in_with_email_and_password(email, password)
#                 flash('Successful login!')
#                 session['email'] = email
#                 session['user_id'] = user['localId']
#                 return redirect(url_for('home'))
#             except requests.exceptions.HTTPError as e:
#                 error_json = e.args[1]
#                 error = json.loads(error_json)['error']
#                 flash(error['message'])
#
#         return render_template('login.html')
#     return render_template('home.html', username=session.get('email'))
#
# # Register
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == "POST":
#         user_info = request.form.to_dict()
#         email = user_info.get("email")
#         password = user_info.get("password")
#
#         if password != user_info.get("password2"):
#             flash("Passwords are different!")
#             return redirect(url_for("register"))
#
#         try:
#             auth.create_user_with_email_and_password(email, password)
#             flash('Congratulations, you are now a registered user!')
#             return redirect(url_for('login'))
#         except requests.exceptions.HTTPError as e:
#             error_json = e.args[1]
#             error = json.loads(error_json)['error']
#             flash(error['message'])
#
#     return render_template('register.html')
#
# # Homepage
# @app.route('/home', methods=['GET', 'POST'])
# def home():
#     if 'email' in session:
#         return render_template('home.html', username=session.get('email'))
#     return ASK_LOGIN_TEXT
#
# # Upload image
# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if 'email' in session:
#         return render_template('upload.html', username=session.get('email'))
#     return ASK_LOGIN_TEXT
#
# # Call camera
# @app.route('/camera', methods=['GET', 'POST'])
# def camera():
#     if 'email' in session:
#         return render_template('camera.html')
#     return ASK_LOGIN_TEXT
#
# # History page
# @app.route('/history', methods=['GET', 'POST'])
# def history():
#     if 'email' in session:
#         user = database.child('users').child(session.get('user_id')).get()
#         histories = user.val()
#         if histories is not None:
#             return render_template('history.html', histories=histories.values())
#         return render_template('history.html')
#     return ASK_LOGIN_TEXT
#
# # Profile page
# @app.route('/profile', methods=['GET', 'POST'])
# def profile():
#     if 'email' in session:
#         email = session['email']
#         user = database.child('users').child(session.get('user_id')).get()
#         histories = user.val()
#         if histories is not None:
#             count = len(histories)
#         else:
#             count = 0
#         return render_template('profile.html', email=email, count=count)
#     return ASK_LOGIN_TEXT
#
# # Logout
# @app.route('/logout')
# def logout():
#     if 'email' in session:
#         flash('Successful logout!')
#         session.pop('email', None)
#         session.pop('user_id', None)
#         return redirect(url_for('login'))
#     return ASK_LOGIN_TEXT
#
# @app.route('/recogApi', methods=['GET', 'POST'])
# def recogApi():
#     """
#     REST API which recognises all faces in an image.
#     recogApi accepts JSON as input. Input must contain:
#         imageBase64: Base64 encoded image
#     The API returns a JSON in the format of:
#         {
#          image: "Base64 encoded image with bounding boxes labelled by their names"
#          classified: "Boolean value of whether face(s) is classified in the image"
#          results: "List of {
#                             "{
#                               name: "the name "
#                               distance: "the confident score"
#                              }"
#                            }"(present only if it is classified)
#         }
#     """
#
#     try:
#         requestJson = request.json
#         imgBase64 = requestJson["imageBase64"]
#     except:
#         return jsonify(errorInvalidJson)
#
#     try:
#         rgbImg = imgUtils.base64StringToRgb(imgBase64)
#         message, nameConfidScore, imgBuffer = faceUtils.face_match_img(rgbImg)
#         return jsonify(message)
#     except:
#         return jsonify(errorClassificationFailed)

@app.route('/recogUploadApi', methods=['GET', 'POST'])
def recogUploadApi():
    """
    REST API which recognises all faces in an image and uploads the results to Real-time Database and Storage.
    recogUploadApi accepts JSON as input. Input must contain:
        imageBase64: Base64 encoded image
        uid: The user ID
        date: The upload date
    The API returns a JSON in the format of:
        {
         image: "Base64 encoded image with bounding boxes labelled by their names"
         classified: "Boolean value of whether face(s) is classified in the image"
         results: "List of {
                            "{
                              name: "the name "
                              distance: "the confident score"
                             }"
                           }"(present only if it is classified)
        }
    """

    # try:
    #     requestJson = request.json
    #     imgBase64 = requestJson["imageBase64"]
    #     userId = requestJson["uid"]
    #     date = requestJson["date"]
    # except:
    #     return jsonify(errorInvalidJson)
    #
    # try:
    #     rgbImg = imgUtils.base64StringToRgb(imgBase64)
    #     classified, nameConfidScore, imgBuffer = faceUtils.face_match_img(rgbImg)
    #
    # # Upload the classification result to the database
    # entryName = database.child('users/' + userId + '/' + 'recognitions').push({
    #     "date": date, "result": nameConfidScore, "userId": userId})["name"]
    #
    # # Upload the labelled image to the storage
    # img = storage.child('imageLabelUploads/' + userId + '/' + entryName + '/' + 'label.jpg')
    # img.put(imgBuffer)
    #
    # # Upload the labelled image url to the database
    # imgUrl = storage.child('imageLabelUploads/' + userId + '/' + entryName + '/' + 'label.jpg').get_url(None)
    # database.child('users/' + userId + '/' + 'recognitions/' + entryName).update({"imageUrl": imgUrl})
    #
    # message = {"imageUrl": imgUrl, "classified": classified, "results": nameConfidScore}
    #
    # return jsonify(message)
    # except:
    #     return jsonify(errorClassificationFailed)

# Test function of uploading results to Real-time Database and Storage
@app.route('/', methods=['GET', 'POST'])
def helloWorld():
    # # Upload the classification result to Real-time Database
    # entryName = database.child('users/' + 'userId' + '/' + 'recognitions').push({
    #     "date": "date", "result": "null", "userId": "user Id"})["name"]
    #
    # # Upload the labelled image to Storage
    # img = storage.child('imageLabelUploads/' + 'userId' + '/' + entryName + '/' + 'label.jpg')
    # img.put("test.jpg")
    #
    # # Upload the labelled image url to Real-time Database
    # imgUrl = storage.child('imageLabelUploads/' + 'userId' + '/' + entryName + '/' + 'label.jpg').get_url(None)
    # database.child('users/' + 'userId' + '/' + 'recognitions/' + entryName).update({"imageUrl": imgUrl})

    return 'Hello, World!'

# Main function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")