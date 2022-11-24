import cv2


def load_cascade():
    return cv2.CascadeClassifier('/Users/psztefko/PycharmProjects/APiP-Project/Resources/haarcascade_frontalface_default.xml')


def read_image(image_path):
    return cv2.imread(image_path)


def read_ears():
    return cv2.imread('resources/shrek_ear.png')


def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def detect_faces(face_cascade, grayscale):
    return face_cascade.detectMultiScale(grayscale, 1.1, 4)


def draw_rectangles(faces, img):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)


def recognize_faces(image_path='/Users/psztefko/PycharmProjects/APiP-Project/Assets/test.jpg'):
    face_cascade = load_cascade()
    img = read_image(image_path)
    grayscale = convert_to_grayscale(img)
    return detect_faces(face_cascade, grayscale)
