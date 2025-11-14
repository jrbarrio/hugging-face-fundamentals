real_estate_agent = CodeAgent(
    tools=[],
    model=model,
    # Create the agent with answer length validation
    final_answer_checks=[check_answer_length],
    verbosity_level=2
)

# Run the agent with a short prompt
response = real_estate_agent.run("Suggest a neigborhood for a couple moving to Austin.")
print(response)