
def count_total_orders(df):
    """
    Count the total number of non-null orders based on the 'Name' column in the dataframe.

    Args:
    df (pandas.DataFrame): The dataframe containing order data.

    Returns:
    int: The total number of non-null orders.

    Raises:
    KeyError: If the 'Name' column does not exist in the dataframe.
    Exception: For handling other unexpected errors that may occur.

    Note:
    Counting all the values from Name column and considering all the duplicate one as a unique order.
    """
    try:
        column_name = 'Name'
        # Check if the 'Name' column exists in the DataFrame
        if column_name not in df.columns:
            print(f"Column '{column_name}' does not exist in the DataFrame.")
            return None

        # Count the total number of non-null values in the 'Name' column
        total_orders = df[column_name].dropna().nunique()
        return total_orders

    except KeyError as e:
        # Return the exception message if a KeyError is encountered
        print(str(e))
        return None
    except Exception as e:
        # Catch any other exceptions that might occur
        print(str(e))
        return None
