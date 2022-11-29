from app.resources.paths import haarcascade
import cv2


def load_cascade():
    return cv2.CascadeClassifier(haarcascade)


def read_image(image_path):
    return cv2.imread(image_path)


def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def detect_faces(face_cascade, grayscale):
    return face_cascade.detectMultiScale(grayscale, 1.1, 4)


def recognize_faces(image_path):
    face_cascade = load_cascade()
    img = read_image(image_path)
    grayscale = convert_to_grayscale(img)
    return detect_faces(face_cascade, grayscale)
