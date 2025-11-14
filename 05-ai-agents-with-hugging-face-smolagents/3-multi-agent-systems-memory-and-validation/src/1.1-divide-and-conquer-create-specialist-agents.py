# School research specialist
school_agent = CodeAgent(
    # Assign a list of tools the agent can use
    tools=[WebSearchTool()],
    model=model,
    # Set the agent's unique name identifier
    name="school_research_agent",
    description="Expert in researching universities, programs, and admission requirements"
)

# Essay writing specialist  
essay_agent = CodeAgent(
    tools=[WebSearchTool()],
    # Provide the model used to generate responses
    model=model,
    name="essay_writing_agent",
    # Write a short description of the agent's area of expertise
    description="Expert in crafting compelling college application essays and personal statements"
)