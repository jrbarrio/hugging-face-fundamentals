expense_data = {
    "groceries": [120, 95, 110, 140],
    "utilities": [85, 92, 78, 88],
    "entertainment": [45, 0, 75, 30],
    "transportation": [60, 55, 70, 65]
}

# Task for the agent
task = f"""Analyze my monthly expense data by category. Calculate total spending per category, find my highest expense area, and suggest a realistic budget for next month. Use simple text format in your final answer. Here is my weekly expense data for the past four weeks:

{expense_data}
"""

# Execute the financial analysis
result = agent.run(task)

print("Personal finance analysis:\n")
print(result)