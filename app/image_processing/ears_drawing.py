from PIL import Image, ImageOps
from app.resources.paths import shrek_ear, output_path
from app.resources import constants


def draw_ears(faces, image_path):
    photo = Image.open(image_path)
    ear = Image.open(shrek_ear)

    for (x, y, w, h) in faces:
        right_ear = ear.resize(
            (round(w / constants.height_divider),
             round(h / constants.height_divider)))
        left_ear = ImageOps.mirror(right_ear)
        photo.paste(right_ear,
                    (int(x + w * constants.right_width_multiplier),
                     y - round(h / constants.height_divider)),
                    right_ear)
        photo.paste(left_ear,
                    (int(x - w * constants.left_width_multiplier),
                     y - round(h / constants.height_divider)),
                    left_ear)

    photo.save(output_path)

    return photo
