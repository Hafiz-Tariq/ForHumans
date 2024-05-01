
def analyze_customer_data(df):
    """
    Analyze customer data to find unique and matching emails under specified conditions.

    Parameters:
    df (pandas.DataFrame): The dataframe containing customer data.

    Returns:
    int, int: The number of unique customers where both Sample and B2B are True,
              and the count of these customers that match when only B2B is True and Sample is None.
    """
    try:
        # Filter dataframe where both 'Sample' and 'B2B' are True
        sample_b2b_true = df[(df['Sample'] == True) & (df['B2B'] == True)]
        # Get unique emails, excluding null values
        unique_emails_sample_b2b = sample_b2b_true['Email'].dropna().unique()

        # Save unique emails count
        unique_emails_count = len(unique_emails_sample_b2b)

        # Filter dataframe where 'B2B' is True and 'Sample' is None
        b2b_true_sample_none = df[(df['B2B'] == True) & (df['Sample'].isna())]
        # Get unique emails in this slice
        unique_emails_b2b = b2b_true_sample_none['Email'].dropna().unique()

        # Find the intersection of the two unique email lists
        matching_emails_count = len(set(unique_emails_sample_b2b).intersection(unique_emails_b2b))

        # Return both counts
        return unique_emails_count, matching_emails_count

    except KeyError as e:
        print(f"Missing column in DataFrame: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
