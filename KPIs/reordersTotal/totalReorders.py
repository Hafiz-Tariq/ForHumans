
def count_unique_customers_multiple_orders(df):
    """
    Counts unique customers who have placed more than one order.

    This function first removes any rows where either the 'Name' or 'Email' fields are null
    to ensure data completeness. It then removes duplicate orders by the 'Name' column,
    implying that each name should correspond to a unique order. Finally, it counts how
    many unique customers (identified by their email) have more than one order.

    Parameters:
        df (pd.DataFrame): A pandas DataFrame containing at least 'Name' and 'Email' columns.

    Returns:
        int: The count of unique customers who have placed more than one order.

    Raises:
        ValueError: If the required columns are missing in the DataFrame.
        Exception: For other unforeseen errors that may occur during function execution.
    """
    try:
        # Check for required columns
        if 'Name' not in df.columns or 'Email' not in df.columns:
            raise ValueError("DataFrame must contain 'Name' and 'Email' columns")

        # Remove rows where 'Name' or 'Email' is null
        cleaned_df = df.dropna(subset=['Name', 'Email'])
        # print(len(cleaned_df['Email']))

        # Remove duplicate orders based on the 'Name' column
        unique_orders = cleaned_df.drop_duplicates(subset='Name')

        # Count unique customers with more than one order based on 'Email' column
        customer_order_counts = unique_orders['Email'].value_counts()
        unique_customers_multiple_orders = customer_order_counts[customer_order_counts > 1].count()

        return unique_customers_multiple_orders

    except ValueError as ve:
        # Handle missing column error specifically
        return None

    except Exception as e:
        # Handle any other exceptions that could occur
        print("An error occurred: ", str(e))
        return None
