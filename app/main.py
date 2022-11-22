from fastapi import FastAPI, File, UploadFile, responses, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from ImageProcessing import ears_drawing, face_recognition
from Resources.Paths import test_photo

app = FastAPI()

faces = face_recognition.recognize_faces(test_photo)
photo = ears_drawing.draw_ears(faces, test_photo)
photo.show()


class Image(BaseModel):
    id: UUID
    url: str


IMAGES = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/image/{id}")
async def get_image(id: UUID):
    for image in IMAGES:
        if image.id == id:
            return image
    raise HTTPException(
        status_code=404,
        detail=f"Image with ID: '{id}': Does not exist"
    )


@app.get("/api/images")
async def get_image_list():
    return IMAGES


@app.post("/api/image")
async def post_image(file: UploadFile = File(...)):
    image = Image(id=uuid4(), url=file.filename)
    IMAGES.append(image)
    return image


@app.delete("/api/image/{id}", status_code=204)
async def delete_image(id: UUID):
    for index, image in enumerate(IMAGES):
        if image == id:
            IMAGES.pop(index)
            return f"Image with ID: {id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"Image with ID: '{id}': Does not exist"
    )


@app.get("/api/processing")
async def get_status():
    return {"status": "IN_PROGRESS"}
