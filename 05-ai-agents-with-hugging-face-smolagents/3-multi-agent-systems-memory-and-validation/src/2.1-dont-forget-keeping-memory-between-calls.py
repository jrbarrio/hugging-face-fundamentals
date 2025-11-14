# Step 1: Tell the agent your flight date
travel_agent.run("My Tokyo flight confirmation code is ZX9Q2L.")

# Step 2: Confirm the agent remember when passing the correct reset parameter
follow_up = "What’s my Tokyo flight confirmation code?"
response = travel_agent.run(follow_up, reset=False)

print(response)