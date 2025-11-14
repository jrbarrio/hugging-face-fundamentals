# Import ActionStep to register a callback for it
from smolagents import ActionStep

coach_agent = CodeAgent(
    tools=[basketball_tool],
    model=model,
    verbosity_level=0,
    # Register a callback that runs when an ActionStep is triggered
    step_callbacks={ActionStep: action_callback}
)

# Run a question through the agent
result = coach_agent.run("What defensive strategy should we use to stop their point guard who averages 25 points per game?")
print(result)