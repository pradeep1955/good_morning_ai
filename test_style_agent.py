from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM
import os

from agents.style_agent import create_style_agent

load_dotenv()

llm = LLM(
    model="openrouter/google/gemma-4-31b-it:free",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

style_agent = create_style_agent(llm)

task = Task(
    description="""
    The user selected sample_modern.jpg

    Return ONLY valid JSON.

    Use exactly these keys:

    {
        "text_color": "#FFFFFF",
        "position": "center",
        "shadow": true
    }

    Rules:

    - text_color must be a hex color code.
    - position must be one of:
      center
      bottom_left
      bottom_center

    - shadow must be true or false.

    Do NOT return font_style.
    Do NOT return explanations.
    Do NOT return markdown.
    Return JSON only.
    """,

    expected_output="""
    Valid JSON with text_color, position and shadow only.
    """,

    agent=style_agent
    )

crew = Crew(
    agents=[style_agent],
    tasks=[task],
    verbose=True
)

result = crew.kickoff()

print("\nRESULT\n")
print(result)
import json

style = json.loads(str(result))

print("\nParsed Style:")
print(style)

print("\nText Color:")
print(style["text_color"])
