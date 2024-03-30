
def total_unique_customer(df):
    """
    Calculate the total number of unique customers based on unique email addresses provided in the 'Email' column.

    This function checks if the specified column exists within the DataFrame. If the column exists, it calculates
    the number of unique values, which represents the total number of unique customers. If the column does not exist,
    or another error occurs, it raises an exception.

    Args:
    df (pandas.DataFrame): The dataframe containing the Shopify orders data.
    column_name (str): The column name to use for identifying unique customers. Default is 'Email'.

    Returns:
    int: The total number of unique customers if successful, or an error message string if not.

    Note:
        There are Null Values in Emails, so for lots of orders we don't know about Customers.
    """
    try:
        column_name = 'Email'
        # Check if the column exists in the DataFrame
        if column_name in df.columns:
            # Calculate the number of unique values in the column
            return df[column_name].nunique()
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


# Use the function on the dataset to get the count of unique customers based on the 'Email' column
# unique_customer_count_by_email = calculate_unique_customers_by_email(data)
# print(unique_customer_count_by_email)
