
def match_order_returns(returns_df, orders_df):
    """
    Processes and matches return order numbers from the returns dataframe with names in the orders dataframe.

    Parameters:
    - returns_df (pd.DataFrame): Dataframe containing return information with columns 'ID' and 'Cleaned_Order_Number'.
    - orders_df (pd.DataFrame): Dataframe containing order information with columns 'Name' and 'B2C'.

    Returns:
    - int: Count of matched entries between cleaned order numbers in returns and names in orders.

    Raises:
    - ValueError: If required columns are missing in the dataframes.
    """

    # Check if required columns are present in the dataframes
    required_returns_columns = ['ID', 'Cleaned_Order_Number']
    required_orders_columns = ['Name', 'B2C']
    if not all(column in returns_df.columns for column in required_returns_columns):
        raise ValueError(f"Returns dataframe is missing one of the required columns: {required_returns_columns}")
    if not all(column in orders_df.columns for column in required_orders_columns):
        raise ValueError(f"Orders dataframe is missing one of the required columns: {required_orders_columns}")

    try:
        # Clean returns data
        returns_cleaned = returns_df.drop_duplicates(subset='ID')
        returns_cleaned = returns_cleaned.dropna(subset=['Cleaned_Order_Number'])
        returns_cleaned = returns_cleaned.drop_duplicates(subset='Cleaned_Order_Number')

        # Clean orders data
        orders_cleaned = orders_df[orders_df['B2C'] == True]
        orders_cleaned = orders_cleaned.drop_duplicates(subset='Name')

        # Match Cleaned_Order_Number in returns with Name in orders
        match_count = returns_cleaned['Cleaned_Order_Number'].isin(orders_cleaned['Name']).sum()

        return match_count

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# Example usage (assuming returns_data and orders_data are loaded pandas DataFrames)
# match_count = match_order_returns(returns_data, orders_data)
# print(f"Number of matches: {match_count}")
