from crewai import Agent

def create_style_agent(llm):

    return Agent(
        role="Greeting Card Style Designer",

        goal="""
        Analyze greeting card styles and
        recommend colors, placement,
        and presentation.
        """,

        backstory="""
        You are an experienced graphic designer
        who creates attractive greeting cards
        and social media posts.
        """,

        llm=llm,

        verbose=True
    )
