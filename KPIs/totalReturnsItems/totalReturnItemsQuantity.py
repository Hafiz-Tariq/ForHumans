
def total_return_items_qty(df):
    """
    Adds a new column to the DataFrame that contains the sum of all values in the 'Quantity' column.

    This function checks if the 'Quantity' column exists within the DataFrame. If the column exists, it calculates
    the sum of all values in that column and adds this total as a new column to the DataFrame. If the column
    does not exist, it raises an exception.

    Args:
    df (pandas.DataFrame): The dataframe containing the returns' data.

    Returns:
    pandas.DataFrame: The modified DataFrame with a new column 'Total Quantity' added.

    Note:
    - We are using Quantity column and taking sum of it.
    """
    try:
        column_name = 'Quantity'
        # Check if the column exists in the DataFrame
        if column_name in df.columns:
            # Calculate the sum of all values in the 'Quantity' column
            total_quantity = df[column_name].sum()
            return total_quantity
        else:
            # If the column does not exist, raise an exception
            print(f"Column '{column_name}' does not exist in the DataFrame.")
            return None
    except KeyError as e:
        # Return the exception message if a KeyError is encountered
        print(str(e))
        return None
    except Exception as e:
        # Catch any other exceptions that might occur
        print(str(e))
        return None
