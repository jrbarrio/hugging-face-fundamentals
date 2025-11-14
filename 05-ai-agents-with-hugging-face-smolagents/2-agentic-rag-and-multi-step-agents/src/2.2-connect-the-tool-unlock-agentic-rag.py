from smolagents import CodeAgent

# Create AI assistant for appliance help
assistant = CodeAgent(
    tools=[appliance_tool],
    model=model,
    instructions="Help with appliance questions using manual information. Search multiple times if needed for complete answers.",
    verbosity_level=1,
    max_steps=6
)

result = assistant.run("If the AC isn’t cooling and shows error E1, what should I check and what’s the next step?")
print(result)