import pandas as pd
import re


def categorize_tags_and_count_orders(df):
    """
    Group by the 'Name' column and update 'Tags' by combining 'b2b' and 'Sample' as 'B2B',
    and everything else as 'B2C'. It then counts the total orders for 'B2B' and 'B2C',
    without focusing on uniqueness but rather the size of each category.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        dict: A dictionary containing the counts of total orders for 'B2B' (including 'Sample') and 'B2C'.

    Raises:
        KeyError: If the specified columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.
    """
    try:
        name_column = 'Name'
        tags_column = 'Tags'
        # Ensure the required columns exist in the DataFrame
        if name_column not in df.columns or tags_column not in df.columns:
            raise KeyError(f"One or both columns '{name_column}' and '{tags_column}' do not exist in the DataFrame.")

        # Initialize the regular expression pattern for B2B tags
        b2b_pattern = re.compile(r'\b(b2b|Sample)\b', re.IGNORECASE)

        # Group by 'Name' and apply logic to 'Tags' for forward and backward filling
        grouped = df.groupby(name_column)[tags_column].transform(lambda x: x.bfill().ffill())

        # Update df with the new tags, standardizing to 'B2B' if it contains 'b2b' or 'Sample'
        df[tags_column] = grouped.apply(
            lambda x: 'B2B' if pd.notnull(x) and b2b_pattern.search(x) else ('B2C' if pd.notnull(x) else None)
        )

        # Count total orders for each category
        total_b2b_orders = df[df[tags_column] == 'B2B'][name_column].size
        total_b2c_orders = df[df[tags_column] == 'B2C'][name_column].size

        # Return the counts of total orders for 'B2B' and 'B2C'
        return total_b2b_orders, total_b2c_orders

    except KeyError as e:
        print(f"KeyError: {e}")
        return None
    except Exception as e:
        print(f"Exception: {e}")
        return None
