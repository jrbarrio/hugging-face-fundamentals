def check_answer_length(final_answer, agent_memory):
    # Check if answer contains less than 200 characters
    if len(str(final_answer)) < 200:
        raise Exception("The answer is too short. Please include more details.")
    # Return True if check passes
    return True