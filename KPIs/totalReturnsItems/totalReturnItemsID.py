def total_return_items(df):
    """
    Adds a new column to the DataFrame that contains the total count of entries in the 'ID' column.

    This function checks if the 'ID' column exists within the DataFrame. If the column exists, it calculates
    the total number of entries in that column (not the unique count) and adds this number as a new column
    to the DataFrame. If the column does not exist, it raises an exception.

    Args:
    df (pandas.DataFrame): The dataframe containing the returns' data.

    Returns:
    pandas.DataFrame: The modified DataFrame with a new column 'Total Entries' added.

    Note:
    - This function take in ID column, count all the values of it. And they work as an Item.
    """
    try:
        column_name = 'ID'
        return_type_column = 'Return type'

        # Check if the column exists in the DataFrame
        if column_name in df.columns:
            # Filter the DataFrame where 'Return type' is 'CUSTOMER'
            df = df[df[return_type_column] == 'CUSTOMER']

            # Calculate the total number of entries in the 'ID' column
            total_entries = len(df[column_name])
            return total_entries
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

