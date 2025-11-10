# Import the VisitWebpageTool class
from smolagents import VisitWebpageTool, CodeAgent, InferenceClientModel

model=InferenceClientModel()

# Create agent with web search capabilities
agent = CodeAgent(
    tools=[VisitWebpageTool()],
    model=model
)

task = "Find GBP to USD exchange rates and summarize how this rate has changed over the past 7 days. A good source is usually Wise."

# Run the agent with the task
result = agent.run(task)