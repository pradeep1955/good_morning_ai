from tools.style_tool import list_samples
from agents.style_agent import create_style_agent

import json
from crewai import Agent, Task, Crew, LLM
from dotenv import load_dotenv
import os

from tools.quote_tool import load_quotes
from tools.image_tool import list_images

load_dotenv()

llm = LLM(
#    model="openrouter/google/gemma-3-4b-it",
    model="openrouter/google/gemma-4-31b-it:free",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

# Select image

images = list_images()

print("\nAvailable Images:\n")

for i, img in enumerate(images, start=1):
    print(f"{i}. {img}")

choice = int(input("\nChoose image number: "))

selected_image = images[choice - 1]

print(f"\nSelected Image: {selected_image}")

samples = list_samples()

print("\nAvailable Styles:\n")

for i, sample in enumerate(samples, start=1):
    print(f"{i}. {sample}")

choice = int(input("\nChoose style number: "))

selected_style = samples[choice - 1]

print(f"\nSelected Style: {selected_style}")

quotes = load_quotes()

print("\nAvailable Quotes:\n")

for i, quote in enumerate(quotes, start=1):
    print(f"{i}. {quote}")

choice = int(input("\nChoose quote number: "))

selected_quote = quotes[choice - 1]

style_agent = create_style_agent(llm)

quote_agent = Agent(
    role="Good Morning Message Writer",
    goal="Create attractive good morning messages",
    backstory="Expert greeting card designer",
    llm=llm,
    verbose=True
)

task = Task(
    description=f"""
Create a beautiful good morning message
using this quote:

{selected_quote}

Keep it short and suitable for putting on an image.
""",
    expected_output="A short good morning greeting",
    agent=quote_agent
)

style_task = Task(
    description=f"""
    The user selected:

    {selected_style}

    Return ONLY valid JSON.

    Example:

    {{
        "text_color":"#FFFFFF",
        "position":"center",
        "shadow":true
    }}

    Rules:

    - text_color must be a hex color.
    - position must be:
      center
      bottom_left
      bottom_center

    - shadow must be true or false.

    Return JSON only.
    """,

    expected_output="JSON style",

    agent=style_agent
)

crew = Crew(
    agents=[quote_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

style_crew = Crew(
    agents=[style_agent],
    tasks=[style_task],
    verbose=True
)

style_result = style_crew.kickoff()

print("\nRAW STYLE RESULT:")
print(repr(str(style_result)))
print("-" * 50)

style_text = str(style_result)

style_text = style_text.replace("```json", "")
style_text = style_text.replace("```", "")
style_text = style_text.strip()

style = json.loads(style_text)

print("\nStyle Selected:")
print(style)

from tools.render_tool import create_greeting_image

create_greeting_image(
    image_path=f"images/{selected_image}",
    message=str(result),
    output_path="output/good_morning.jpg",
    style=style
)

print("\nImage created:")
print("output/good_morning.jpg")

print("\n")
print("=" * 50)
print(result)
print("=" * 50)
