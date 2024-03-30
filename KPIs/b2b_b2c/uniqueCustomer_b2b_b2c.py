import re
import pandas as pd


def unique_customer_b2b_b2c(df):
    """
    This function categorizes customers as B2B or B2C by checking for the presence of 'b2b' in the tags column,
    using a case-insensitive regular expression. It then calculates the number of unique customers in each category
    based on their email addresses. Null values in the tags column are left unchanged.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        tuple: A tuple containing the count of unique B2B customers and unique B2C customers.

    Raises:
        KeyError: If the specified columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.

    Note:
        All the Tag contain b2b inside it will be shifted to B2B and everything else to B2C.
        All NUll will stay Null. Then we will use Email to find unique customers of both categories.
    """

    try:
        tags_column = 'Tags'
        email_column = 'Email'
        # Check if the required columns exist in the DataFrame
        if tags_column not in df.columns or email_column not in df.columns:
            print(f"One or both columns '{tags_column}' and '{email_column}' do not exist in the DataFrame.")
            return None, None

        # Initialize the regular expression pattern for B2B tags
        b2b_pattern = re.compile(r'\bb2b\b', re.IGNORECASE)

        # Categorize each row as 'b2b' or 'b2c'
        df[tags_column] = df[tags_column].apply(
            lambda x: 'b2b' if pd.notnull(x) and b2b_pattern.search(x) else ('b2c' if pd.notnull(x) else None))

        # Split the dataframe into B2B and B2C based on the tags
        b2b_customers = df[df[tags_column] == 'b2b'][email_column]
        b2c_customers = df[df[tags_column] == 'b2c'][email_column]

        # Calculate the number of unique customers in each category based on email
        unique_b2b_customers = b2b_customers.nunique()
        unique_b2c_customers = b2c_customers.nunique()

        # Return the count of unique B2B and B2C customers
        return unique_b2b_customers, unique_b2c_customers

    except KeyError as e:
        # Handle the case where the specified columns are not found in the dataframe
        print(f"KeyError: {str(e)}")
        return None, None
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"KeyError: {str(e)}")
        return None, None

# Example usage:
# Replace 'your_dataframe' with your actual dataframe variable.
# unique_b2b_count, unique_b2c_count = categorize_and_count_unique_customers(your_dataframe)
