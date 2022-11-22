from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from ImageProcessing import ears_drawing, face_recognition
from Resources.Paths import test_photo
import models
from database import engine, session_local
from sqlalchemy.orm import Session


app = FastAPI()
models.base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


faces = face_recognition.recognize_faces(test_photo)
photo = ears_drawing.draw_ears(faces, test_photo)
photo.show()


class Image(BaseModel):
    url: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/image/{id}")
async def get_image(id: int, db: Session = Depends(get_db)):
    image_model = db.query(models.Images).filter(
        models.Images.id == id).first()

    if image_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Image with ID: '{id}': Does not exist"
        )

    image = Image(url=image_model.url)
    return image


@app.get("/api/images")
async def get_image_list(db: Session = Depends(get_db)):
    return db.query(models.Images).all()


@app.post("/api/image")
async def post_image(file: UploadFile = File(...),
                     db: Session = Depends(get_db)):
    image_model = models.Images()
    image_model.url = file.filename
    db.add(image_model)
    db.commit()

    return image_model


@ app.delete("/api/image/{id}", status_code=204)
async def delete_image(id: int, db: Session = Depends(get_db)):
    image_model = db.query(models.Images).filter(
        models.Images.id == id).first()

    if image_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Image with ID: '{id}': Does not exist"
        )

    db.query(models.Images).filter(models.Images.id == id).delete()
    db.commit()


@ app.get("/api/processing")
async def get_status():
    return {"status": "IN_PROGRESS"}
