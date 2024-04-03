import re
import pandas as pd


def categorize_tags_and_count_orders(df):
    """
    Group by the 'Name' column and fill down the 'Tags' based on the non-null values associated with each unique 'Name'.
    If a 'Name' has at least one non-null 'Tag', all entries with that 'Name' will have their 'Tags' filled with the same value,
    standardized to 'B2B' if it contains 'b2b'. Entries with no non-null 'Tag' for a 'Name' will remain null.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        dict: A dictionary containing the counts of total unique orders for 'B2B' and 'B2C'.

    Raises:
        KeyError: If the specified columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.

    Note:
        Transfer Tags to B2B and B2C.
        Categorize them on Name and fill down the non-null value if exists.
    """
    try:
        name_column = 'Name'
        tags_column = 'Tags'
        # Check if the required columns exist in the DataFrame
        if name_column not in df.columns or tags_column not in df.columns:
            print(f"One or both columns '{name_column}' and '{tags_column}' do not exist in the DataFrame.")
            return None, None

        # Initialize the regular expression pattern for B2B tags
        b2b_pattern = re.compile(r'\bb2b\b', re.IGNORECASE)

        # Group by 'Name' and apply the logic to 'Tags'
        grouped = df.groupby(name_column)[tags_column].transform(lambda x: x.bfill().ffill())
        # Update df with the new tags
        df[tags_column] = grouped.apply(
            lambda x: 'B2B' if pd.notnull(x) and b2b_pattern.search(x) else ('B2C' if pd.notnull(x) else None)
        )

        # Count unique orders for each category
        unique_b2b_orders = df[df[tags_column] == 'B2B'][name_column].size
        unique_b2c_orders = df[df[tags_column] == 'B2C'][name_column].size

        # Return the counts of total unique orders for 'B2B' and 'B2C'
        return unique_b2b_orders, unique_b2c_orders

    except KeyError as e:
        # Handle the case where the specified columns are not found in the dataframe
        print(f"KeyError: {str(e)}")
        return None, None
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Exception: {str(e)}")
        return None, None
