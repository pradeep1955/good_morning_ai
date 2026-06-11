from tools.render_tool import create_greeting_image

style = {
    "text_color": "#FFFFFF",
    "position": "bottom_left",
    "shadow": True
}

create_greeting_image(
    image_path="images/vasant_rangoli.jpg",
    message="GOOD MORNING",
    output_path="output/test_style.jpg",
    style=style
)

print("Done")
