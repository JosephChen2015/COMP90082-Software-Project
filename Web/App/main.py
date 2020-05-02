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
        return render_template("base.html", img_stream=message)
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
    #     img_base64 = json_msg["image"]
    #     img_name = json_msg["img_name"]
    # except:
    #     return jsonify(JSON_ERROR_INVALID_JSON)

    try:
        # rgb_img = img_utils.base64_to_rgb(img_base64)
        message, name_distance, unknown_image_buffer = face_utils.face_match_img("test.jpg")

        if message["classified"] is False:
            return message
            # return jsonify(message)
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
            img_location = storage.child('upload/' + 'jingyin' + '/' + entry_name + '/' + entry_name + '.jpg').get_url(None)
            database.child('users').child('jingyin').child(entry_name).update({"image_location": img_location})

            return message
            # return jsonify(message)
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
