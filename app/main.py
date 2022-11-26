from fastapi import FastAPI
from ImageProcessing import ears_drawing, face_recognition
from Resources.Paths import test_photo

faces = face_recognition.recognize_faces(test_photo)
photo = ears_drawing.draw_ears(faces, test_photo)
photo.show()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/processing")
async def get_status():
    return {"status": "IN_PROGRESS"}
