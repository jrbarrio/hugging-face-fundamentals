from smolagents import CodeAgent

# Create a code agent with the lookup_orders and generate_order_id tools
agent = CodeAgent(
    tools=[lookup_orders, generate_order_id],
    model=model,
    # Authorize pandas import
    additional_authorized_imports=['pandas']
)

task = (
    "For table 5, list their current drink orders and generate a unique order ID for each one."
)

# Run the agent passing the task
result = agent.run(task)
print(result)