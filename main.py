from face_recognition import recognize_faces
from ears_drawing import draw_ears

faces = recognize_faces()
photo = draw_ears(faces, 'test.jpg')
photo.show()
