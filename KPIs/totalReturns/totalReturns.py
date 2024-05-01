
def total_returns(df):
    """
    Calculate the total number of returns based on unique IDs provided in the specified column, filtered by
    the 'Return type' column having the value 'CUSTOMER'.

    This function checks if the necessary columns exist within the DataFrame. If the columns exist, it filters
    the DataFrame where 'Return type' is 'CUSTOMER' and calculates the number of unique 'ID' values, which
    represents the total number of customer returns. If the required columns do not exist, or another error
    occurs, it raises an exception.

    Args:
    df (pandas.DataFrame): The dataframe containing the returns' data.

    Returns:
    int: The total number of customer returns if successful, or None if not.

    Note:
    - We use the 'ID' column of a returns file. After filtering rows where 'Return type' is 'CUSTOMER',
      counting the unique values will give the total customer returns.
    """
    try:
        id_column_name = 'ID'
        return_type_column = 'Return type'

        # Check if the necessary columns exist in the DataFrame
        if id_column_name in df.columns and return_type_column in df.columns:
            # Filter the DataFrame where 'Return type' is 'CUSTOMER'
            filtered_df = df[df[return_type_column] == 'CUSTOMER']
            # Calculate the number of unique values in the 'ID' column
            return filtered_df[id_column_name].nunique()
        else:
            # If any of the columns do not exist, raise an exception
            missing_columns = [col for col in [id_column_name, return_type_column] if col not in df.columns]
            print(f"Missing column(s): {', '.join(missing_columns)} in the DataFrame.")
            return None
    except KeyError as e:
        # Return the exception message if a KeyError is encountered
        print(str(e))
        return None
    except Exception as e:
        # Catch any other exceptions that might occur
        print(str(e))
        return None
