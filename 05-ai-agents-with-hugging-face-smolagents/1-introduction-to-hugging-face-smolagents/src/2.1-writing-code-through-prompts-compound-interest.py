# Import the CodeAgent class
from smolagents import CodeAgent, InferenceClientModel

model=InferenceClientModel()

# Create a basic agent without tools
agent = CodeAgent(tools=[], model=model)

task = "I deposit $100 every month into an account that pays 5% annual interest, compounded monthly. Calculate the total balance after 10 years."

# Run the agent
result = agent.run(task)
print(result)