# Import the tool decorator
from smolagents import tool
from datetime import datetime

# Create a tool with the @tool decorator
@tool
def generate_order_id(table_id: str, drink_name: str) -> str:
    """
    Generates a unique order ID for a café order.
    
    Args:
        table_id: The table's identifier (e.g. "T5")
        drink_name: Name of the drink (e.g. "Latte")
    
    Returns:
        A string in the format "{table_id}_{drink_name}_{YYYYMMDD_HHMM}"
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    order_id = f"{table_id}_{drink_name}_{timestamp}"
    
    # Return the order ID
    return order_id