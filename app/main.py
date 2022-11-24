from cmath import log
from fastapi import FastAPI, File, UploadFile, responses
# from deta import Deta
import os
from pathlib import Path

from ImageProcessing import ears_drawing, face_recognition
from Resources.Paths import test_photo

faces = face_recognition.recognize_faces(test_photo)
photo = ears_drawing.draw_ears(faces, test_photo)
photo.show()

# PROJECT_KEY = os.environ['PROJECT_KEY']
app = FastAPI()

# deta = Deta(PROJECT_KEY)
# drive = deta.Drive("preprocessed")


@app.get("/")
async def root():
    return {"message": "Hello World"}


# @app.get("/api/image/{image_name}", status_code=201)
# async def get_image(image_name: str):
#     img = drive.get(image_name)
#     ext = image_name.split(".")[1]
#     return responses.StreamingResponse(img.iter_chunks(),
#                                        media_type="image/{ext}")


# @app.get("/api/images")
# async def get_image_list():
#     return drive.list()


# @app.post("/api/image")
# async def post_image(file: UploadFile = File(...)):
#     return drive.put(file.filename, file.file)


# @app.delete("/api/image/{image_name}", status_code=204)
# async def delete_image(image_name: str):
#     img = drive.delete(image_name)


@app.get("/api/processing")
async def get_status():
    return {"status": "IN_PROGRESS"}
