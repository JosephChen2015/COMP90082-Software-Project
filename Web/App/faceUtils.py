import os
import cv2
import face_recognition
import imgUtils

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class FaceUtils:
    names = []
    images = []
    face_encodings = []

    def __init__(self, img_path="./Web/App/knowns/"):
    # def __init__(self, img_path="./knowns/"):
        self.img_path = img_path
        self.load_images()
        self.encoding_faces()

    def load_images(self):
        for file in os.listdir(self.img_path):
            if not file.startswith(".") and allowed_file(file):
                self.names.append(os.path.splitext(file)[0])
                self.images.append(face_recognition.load_image_file(self.img_path + file))

    def encoding_faces(self):
        for image in self.images:
            encoding = face_recognition.face_encodings(image)[0]
            self.face_encodings.append(encoding)

    def face_match_img(self, file_stream):
        unknown_image = face_recognition.load_image_file(file_stream)
        unknown_face_encodings = face_recognition.face_encodings(unknown_image)
        face_locations = face_recognition.face_locations(unknown_image)
        name_confidence_score = []
        classified = False
        for i in range(len(unknown_face_encodings)):
            unknown_encoding = unknown_face_encodings[i]
            face_location = face_locations[i]
            top, right, bottom, left = face_location
            cv2.rectangle(unknown_image, (left, top), (right, bottom), (0, 255, 0), 2)
            results = face_recognition.compare_faces(self.face_encodings, unknown_encoding)
            scores = [1 - d for d in face_recognition.face_distance(self.face_encodings, unknown_encoding)]
            result_index = scores.index(max(scores))
            if results[result_index]:
                classified = True
                name = self.names[result_index]
                confidence_score = scores[result_index]
                name_confidence_score_json = {"name": name, "confidence score": confidence_score}
                name_confidence_score.append(name_confidence_score_json)
                cv2.putText(unknown_image, name, (left - 10, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        unknown_image_buffer = imgUtils.rgbToBuffer(unknown_image)

        return classified, name_confidence_score, unknown_image_buffer

# Simple test
# face_util = FaceUtils()
# unknown_path = "./unknowns/"
# for u in os.listdir(unknown_path):
#     if not u.startswith(".") and allowed_file(u):
#         img = open(unknown_path + u, 'rb')
#         classified, name_confidence_score, unknown_image_buffer = face_util.face_match_img(img)
#         print(name_confidence_score)
