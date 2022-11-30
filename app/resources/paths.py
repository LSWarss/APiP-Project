from pathlib import Path

_haarcascade_abs = "resources/haarcascade_frontalface_default.xml"

haarcascade = str(Path(__file__).parents[1] / _haarcascade_abs)
test_photo = str(Path(__file__).parents[1] / "assets/test.jpg")
shrek_ear = str(Path(__file__).parents[1] / "assets/shrek_ear.png")
output_path = str(Path(__file__).parents[1] / "assets/output.png")
