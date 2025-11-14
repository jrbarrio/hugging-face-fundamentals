# Inspect the code executed by the agent
executed_code = travel_agent.memory.return_full_code()

print("Executed code during session:")
print("=" * 50)
print(executed_code)