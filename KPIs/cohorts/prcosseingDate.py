import pandas as pd


def convert_created_at_to_date(order_data):
    """
    Converts the 'Created at' column of the order data from datetime with timezone
    to a date-only format (YYYY-MM-DD).

    Parameters:
    - order_data (pd.DataFrame): DataFrame containing the 'Created at' column with datetime values.

    Returns:
    - pd.DataFrame: Updated DataFrame with 'Created at' in date-only format.
    """
    try:
        # Convert 'Created at' to datetime with UTC timezone, then extract the date part
        order_data['Created at'] = pd.to_datetime(order_data['Created at'], utc=True).dt.date
        return order_data
    except Exception as e:
        print(f"An error occurred while converting the 'Created at' column: {e}")
        return None

# Example usage:
# Load your data
# order_data = pd.read_excel('path_to_order_data.xlsx')

# Update the 'Created at' column
# updated_order_data = convert_created_at_to_date(order_data)
# print(updated_order_data.head())
