from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import textwrap

def create_greeting_image(
        image_path,
        message,
        output_path,
        style):

    image = Image.open(image_path)
    img_width, img_height = image.size
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            40
        )
    except:
        font = ImageFont.load_default()
    wrapped_text = textwrap.fill(message, width=30)
    bbox = draw.multiline_textbbox(
    (0, 0),
    wrapped_text,
    font=font
    )
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    position = style["position"]

    if position == "center":

        x = (img_width - text_width) / 2
        y = (img_height - text_height) / 2

    elif position == "bottom_left":

        x = 50
        y = img_height - text_height - 50

    elif position == "bottom_center":

        x = (img_width - text_width) / 2
        y = img_height - text_height - 50

    else:

        x = (img_width - text_width) / 2
        y = img_height * 0.70

    if style["shadow"]:

        draw.multiline_text(
            (x + 2, y + 2),
            wrapped_text,
            fill="black",
            font=font,
            align="center"
        )

    draw.multiline_text(
        (x, y),
        wrapped_text,
        fill=style["text_color"],
        font=font,
        align="center"
    )


    image.save(output_path)

    return output_path
