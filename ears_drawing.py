from PIL import Image, ImageOps


def draw_ears(faces, image_path):
    photo = Image.open(image_path)
    ear = Image.open('resources/shrek_ear.png')

    for (x, y, w, h) in faces:
        right_ear = ear.resize((int(int(h) * 3 / 4), int(int(h) * 3 / 4)))
        left_ear = ImageOps.mirror(right_ear)

        photo.paste(right_ear, (int(x + w * 2 / 3), y - h), right_ear)
        photo.paste(left_ear, (int(x - w * 3 / 10), y - h), left_ear)

    photo.save('resources/shreked.png')

    return photo
