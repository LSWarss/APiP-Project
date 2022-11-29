from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from fastapi.responses import FileResponse
from app.image_processing import ears_drawing, face_recognition
from app.resources.paths import test_photo
from sqlalchemy.orm import Session
from app import models
from app.database import session_local, engine
from os import getcwd, path

app = FastAPI()
models.base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = session_local()
        yield db
    finally:
        db.close()


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

    image = models.Image(url=image_model.url)
    return image


@app.get("/api/image/download/{id}")
async def get_image(id: int, db: Session = Depends(get_db)):
    image_model = db.query(models.Images).filter(
        models.Images.id == id).first()

    if image_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"Image with ID: '{id}': Does not exist"
        )

    image = models.Image(url=image_model.url)

    return FileResponse(path=getcwd() + "/" + image.url,
                        media_type='application/octet-stream',
                        filename=image.url)


@app.get("/api/images")
async def get_image_list(db: Session = Depends(get_db)):
    return db.query(models.Images).all()


@app.post("/api/image")
async def post_image(file: UploadFile = File(...),
                     db: Session = Depends(get_db)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()

    image_model = models.Images()
    image_model.url = file.filename
    db.add(image_model)
    db.commit()

    return image_model


@app.post("/api/processing")
async def proccess_image(file: UploadFile = File(...),
                         db: Session = Depends(get_db)):
    with open(file.filename, 'wb') as image:
        content = await file.read()
        image.write(content)
        image.close()

    faces = face_recognition.recognize_faces(file.filename)
    photo = ears_drawing.draw_ears(faces, file.filename)
    filename, file_extension = path.splitext(file.filename)
    process_filename = filename + "_shreked" + file_extension
    photo.save(process_filename)

    image_model = models.Images()
    image_model.url = process_filename
    db.add(image_model)
    db.commit()

    return FileResponse(path=getcwd() + "/" + process_filename,
                        media_type='application/octet-stream',
                        filename=process_filename)


@app.delete("/api/image/{id}", status_code=204)
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


@app.get("/api/processing")
async def get_status():
    return {"status": "IN_PROGRESS"}
