import pandas as pd


def unique_customer_b2b_b2c(df):
    """
    This function counts unique customers categorized as B2B and B2C based on their email addresses.
    It uses the email addresses to determine uniqueness. The B2B and B2C columns should be marked
    with a numeric value (likely 1.0) to indicate a customer belongs to that category.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.

    Returns:
        tuple: A tuple containing the count of unique B2B and unique B2C customers.

    Raises:
        KeyError: If the specified columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.
    """
    try:
        email_column = 'Email'
        b2b_column = 'B2B'
        b2c_column = 'B2C'

        # Check if the required columns exist in the DataFrame
        if any(col not in df.columns for col in [email_column, b2b_column, b2c_column]):
            raise KeyError(f"One or more required columns do not exist in the DataFrame.")

        # Filter the data by non-null emails
        filtered_data = df[df[email_column].notna()]

        # Identify unique B2B and B2C customers
        unique_b2b_customers = filtered_data[filtered_data[b2b_column].notna()][email_column].nunique()
        unique_b2c_customers = filtered_data[filtered_data[b2c_column].notna()][email_column].nunique()

        # Return the count of unique customers in both groups
        return unique_b2b_customers, unique_b2c_customers

    except KeyError as e:
        # Handle the case where the specified columns are not found in the dataframe
        print(f"KeyError: {e}")
        return None, None
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Exception: {e}")
        return None, None

# Usage example:
# Ensure you load your DataFrame as 'df' before using this function
# df = pd.read_excel('your_data_file.xlsx')
# unique_b2b, unique_b2c = unique_customer_b2b_b2c(df)
# print("Unique B2B Customers:", unique_b2b)
# print("Unique B2C Customers:", unique_b2c)
