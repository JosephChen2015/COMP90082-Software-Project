# -*- coding: utf-8 -*-
"""
Main flask application with all the routes
"""

import firebase as firebase
from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
import config
from datetime import datetime
import json
import requests
import img_utils
from face_utils import FaceUtils
import cv2

firebase = firebase.Firebase(config.firebaseConfig)
storage = firebase.storage()
database = firebase.database()
# auth = firebase.auth()

face_utils = FaceUtils()

app = Flask(__name__)
app.config.from_object(config)

# HTML to be shown to the unregistered user if they try to access a page only accessible for signed in users
# ASK_LOGIN_TEXT = "You must log in to access this page!<br><a href = '/login'></b>click here to log in</b></a>"

# Error messages to be sent if the user passes in invalid json or error on image processing possibly due to bad data
JSON_ERROR_INVALID_JSON = {"Error": "Failed to parse json, invalid format"}
JSON_ERROR_CLASSIFICATION_FAILED = {"Error": "Failed to process image, try another image"}


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


@app.route('/recog_api', methods=['GET', 'POST'])
def recog_api():
    """
    REST API which recognises all faces in an image.
    recog_api accepts JSON as input. Input must contain:
        image: Base64 encoded image
    The API returns a JSON in the format of:
        {
         image: "Base64 encoded image with bounding boxes labelled by their names"
         classified: "Boolean value of whether face(s) is classified in the image"
         results: "List of {
                            classification: "{
                                              name: "the name "
                                              distance: "the confident score"
                                             }"
                           }"(present only if it is classified)
        }
    """

    # try:
    #     json_msg = request.json
    #     img_base64 = json_msg["image"]
    # except:
    #     return jsonify(JSON_ERROR_INVALID_JSON)

    try:
        # rgb_img = img_utils.base64_to_rgb(img_base64)
        message, name_distance, unknown_image_buffer = face_utils.face_match_img("./Web/App/unknowns/test.jpg")
        # print(message)
        # cv2.imshow("Output", unknown_image_buffer)
        # cv2.waitKey(0)
        return render_template("base.html", img_stream=message["image"])
        # return jsonify(message)
    except:
        return JSON_ERROR_CLASSIFICATION_FAILED
        # return jsonify(JSON_ERROR_CLASSIFICATION_FAILED)


@app.route('/recog_upload_api', methods=['GET', 'POST'])
def recog_upload_api():
    """
    REST API which recognises all faces in an image and uploads the results to Real-time Database if the user is logged in.
    Function is the same with recog_api if the user is not logged in.
    recog_upload_api accepts JSON as input. Input must contain:
        image: Base64 encoded image
        img_name: The name of the image to be uploaded to the database.
    The API returns a JSON in the format of:
        {
         image: "Base64 encoded image with bounding boxes labelled by their names"
         classified: "Boolean value of whether face(s) is classified in the image"
         results: "List of {
                            classification: "{
                                              name: "the name "
                                              distance: "the confident score"
                                             }"
                           }"(present only if it is classified)
        }
    """

    # try:
    #     json_msg = request.json
    #     img_base64 = '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'
    #     img_name = json_msg["img_name"]
    # except:
    #     return jsonify(JSON_ERROR_INVALID_JSON)

    try:
        # rgb_img = img_utils.base64_to_rgb(img_base64)
        message, name_distance, unknown_image_buffer = face_utils.face_match_img("./Web/App/unknowns/test.jpg")
        # message, name_distance, unknown_image_buffer = face_utils.face_match_img(rgb_img)

        if message["classified"] is False:
            # return message
            return jsonify(message)
        else:
            # if 'email' in session:
            # time = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

            # # Upload the classification result to the database
            # entry_name = database.child('users/' + session.get('user_id')).push({
            #     "image_name": img_name, "upload_time": time, "result": face_predictions})["name"]
            #
            # # Upload the labelled image to the storage
            # image = storage.child('upload/' + session.get('user_id') + '/' + entry_name + '/' + entry_name + '.jpg')
            # image.put(boxed_img_buff)
            #
            # # Upload the labelled image location to the database
            # img_location = storage.child('upload/' + session.get('user_id') + '/' + entry_name + '/' + entry_name + '.jpg').get_url(None)
            # database.child('users').child(session.get('user_id')).child(entry_name).update({"image_location": img_location})

            # # Upload the classification result to the database
            # entry_name = database.child('users/' + 'jingyin').push({
            #     "image_name": "test.jpg", "upload_time": time, "result": name_distance})["name"]
            #
            # # Upload the labelled image to the storage
            # image = storage.child('upload/' + 'jingyin' + '/' + entry_name + '/' + entry_name + '.jpg')
            # image.put(unknown_image_buffer)
            #
            # # Upload the labelled image location to the database
            # img_location = storage.child('upload/' + 'jingyin' + '/' + entry_name + '/' + entry_name + '.jpg').get_url(None)
            # database.child('users').child('jingyin').child(entry_name).update({"image_location": img_location})

            time = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")

            # Upload the classification result to the database
            entry_name = database.child('users/' + 'jingyin').push({
                "image_name": "test.jpg", "upload_time": time, "result": name_distance})["name"]

            # Upload the labelled image to the storage
            image = storage.child('upload/' + 'jingyin' + '/' + entry_name + '/' + entry_name + '.jpg')
            image.put(unknown_image_buffer)

            # Upload the labelled image location to the database
            img_location = storage.child('upload/' + 'jingyin' + '/' + entry_name + '/' + entry_name + '.jpg').get_url(
                None)
            database.child('users').child('jingyin').child(entry_name).update({"image_location": img_location})

            # return message
            return jsonify(message)
    except:
        return JSON_ERROR_CLASSIFICATION_FAILED
        # return jsonify(JSON_ERROR_CLASSIFICATION_FAILED)


# Test the function of upload to database and storage
# @app.route('/', methods=['GET', 'POST'])
# def hello_world():
#     time = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
#
#     # Upload the classification result to the database
#     entry_name = database.child('users/' + 'u_id').push({
#         "image_name": "img_name", "upload_time": time, "result": "null_result"})["name"]
#
#     # Upload the labelled image to the storage
#     image = storage.child('upload/' + 'u_id' + '/' + entry_name + '/' + entry_name + '.jpg')
#     image.put("img_name")
#
#     # Upload the labelled image location to the database
#     img_location = storage.child('upload/' + 'u_id' + '/' + entry_name + '/' + entry_name + '.jpg').get_url(None)
#     database.child('users').child('u_id').child(entry_name).update({"image_location": img_location})
#
#     return 'Hello, World!'

# Main function
if __name__ == '__main__':
    app.run()
