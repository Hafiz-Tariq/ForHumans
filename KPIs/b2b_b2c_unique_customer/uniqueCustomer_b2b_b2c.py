import pandas as pd


def unique_customer_b2b_b2c(df):
    """
    This function counts unique customers categorized as B2B (including 'Sample') and B2C based on their tags.
    It uses the email addresses to determine uniqueness. The tags column must contain 'b2b', 'Sample', or 'B2C',
    with null values left unchanged.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        tuple: A tuple containing the count of unique B2B (including 'Sample') customers and unique B2C customers.

    Raises:
        KeyError: If the specified columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.

    Note:
        The dataframe passed as parameter already have tags column which contains 'b2b', 'Sample' and 'B2C' in it.
        'B2B' and 'Sample' are combined to count unique customers in that group, and 'B2C' are counted separately.
    """

    try:
        tags_column = 'Tags'
        email_column = 'Email'
        # Check if the required columns exist in the DataFrame
        if tags_column not in df.columns or email_column not in df.columns:
            raise KeyError(f"One or both columns '{tags_column}' and '{email_column}' do not exist in the DataFrame.")

        # Combine 'b2b' and 'Sample' tags for B2B customers
        df['Customer Category'] = df[tags_column].apply(
            lambda x: 'B2B' if x in ['b2b', 'Sample'] else ('B2C' if x == 'B2C' else None)
        )

        # Split the dataframe into the two groups
        b2b_sample_customers = df[df['Customer Category'] == 'B2B'][email_column]
        b2c_customers = df[df['Customer Category'] == 'B2C'][email_column]

        # Calculate the number of unique customers in each group
        unique_b2b_sample_customers = b2b_sample_customers.nunique()
        unique_b2c_customers = b2c_customers.nunique()

        # Return the count of unique customers in both groups
        return unique_b2b_sample_customers, unique_b2c_customers

    except KeyError as e:
        # Handle the case where the specified columns are not found in the dataframe
        print(f"KeyError: {e}")
        return None, None
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Exception: {e}")
        return None, None
