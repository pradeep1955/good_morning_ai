from crewai import Agent

def create_quote_agent(llm):

    return Agent(
        role="Quote Selector",
        goal="Help choose an inspiring quote",
        backstory="Expert in inspirational messages",
        llm=llm,
        verbose=True
    )
