from pathlib import Path

def list_images():
    image_folder = Path("images")

    images = []

    for file in image_folder.iterdir():
        if file.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            images.append(file.name)

    return images
