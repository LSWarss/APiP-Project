from PIL import Image, ImageOps
from Resources.Paths import shrek_ear, output_path


def draw_ears(faces, image_path):
    photo = Image.open(image_path)
    ear = Image.open(shrek_ear)
    right_ear = ear.resize((30, 30))
    left_ear = ImageOps.mirror(right_ear)

    for (x, y, w, h) in faces:
        photo.paste(right_ear, (int(x + w * 2 / 3), y - h), right_ear)
        photo.paste(left_ear, (int(x - w * 3 / 10), y - h), left_ear)

    photo.save(output_path)

    return photo
