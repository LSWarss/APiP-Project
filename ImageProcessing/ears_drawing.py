from PIL import Image, ImageOps
from Resources.Paths import shrek_ear, output_path
from Resources import Constants


def draw_ears(faces, image_path):
    photo = Image.open(image_path)
    ear = Image.open(shrek_ear)

    for (x, y, w, h) in faces:
        right_ear = ear.resize((round(w / Constants.heigth_divider), round(h / Constants.heigth_divider)))
        left_ear = ImageOps.mirror(right_ear)
        photo.paste(right_ear,
                    (int(x + w * Constants.right_width_multiplier),
                     y - round(h / Constants.heigth_divider)),
                    right_ear)
        photo.paste(left_ear,
                    (int(x - w * Constants.left_width_multiplier),
                     y - round(h / Constants.heigth_divider)),
                    left_ear)

    photo.save(output_path)

    return photo
