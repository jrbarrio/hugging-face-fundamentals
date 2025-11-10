# Import the tool decorator
from smolagents import tool
import pandas as pd

# Create a tool that receives the table_id as input
@tool
def lookup_orders(table_id: str) -> list[str]:
    """
    Retrieves the current drink orders for a café table.

    Args:
        table_id (str): The table's identifier (e.g., "T5").

    Returns:
        list[str]: A list of drink orders, each formatted like "Latte (Large)".
    """
    
    # Read the orders.csv file
    df = pd.read_csv('orders.csv')
    orders = df[df['table_id'] == table_id].apply(lambda row: f"{row['drink_name']} ({row['size']})", axis=1).tolist()
    
    # Return the table orders
    return orders