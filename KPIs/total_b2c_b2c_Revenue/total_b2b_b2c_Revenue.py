
def calculate_revenue_by_category(df):
    """
    Calculates the total revenue and breaks it down into B2B+Sample revenue and B2C revenue.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        tuple: A tuple containing the total revenue, B2B+Sample revenue, and B2C revenue.

    Raises:
        KeyError: If necessary columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.

    Note:
        The function assumes 'Total' column contains the revenue amount
        and 'Tags' are categorized as 'B2B', 'Sample', or 'B2C'.
    """
    try:
        # Columns to check
        name_column = 'Name'
        tags_column = 'Tags'
        total_column = 'Total'

        # Ensure necessary columns exist
        if any(col not in df.columns for col in [name_column, tags_column, total_column]):
            print(f"One or more necessary columns do not exist in the DataFrame.")
            return None, None, None

        # Fill 'Tags' by grouping on 'Name'
        grouped_tags = df.groupby(name_column)[tags_column].transform(lambda x: x.bfill().ffill())
        df['Filled Tags'] = grouped_tags.apply(lambda x: 'B2B' if x in ['B2B', 'Sample'] else 'B2C')

        # Calculate total revenue
        total_revenue = df[total_column].sum()

        # Calculate B2B+Sample revenue
        b2b_sample_revenue = df[df['Filled Tags'] == 'B2B'][total_column].sum()

        # Calculate B2C revenue
        b2c_revenue = df[df['Filled Tags'] == 'B2C'][total_column].sum()

        return total_revenue, b2b_sample_revenue, b2c_revenue

    except KeyError as e:
        print(f"KeyError: {e}")
        return None, None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None, None
