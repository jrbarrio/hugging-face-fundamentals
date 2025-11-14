# Define an action callback that accepts the agent step and the agent
def action_callback(agent_step, agent):
    step_num = agent_step.step_number
    print(f"Step {step_num}: Analyzing basketball data!")
    
    # Check if the agent step includes token usage
    if agent_step.is_final_answer:
        total_tokens = agent_step.token_usage.total_tokens
        # Print how many tokens were used
        print(f"Analysis complete! Total tokens used: {total_tokens}")