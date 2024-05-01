import pandas as pd


def categorize_tags_and_count_orders(df):
    """
    This function counts the total B2B and B2C orders based on unique entries in the 'Name' column.
    It checks how many of these unique names have associated non-null entries in 'B2B' and 'B2C' columns.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.

    Returns:
        tuple: A tuple containing the count of B2B orders and B2C orders associated with unique names.

    Raises:
        KeyError: If the 'Name', 'B2B', or 'B2C' columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.
    """
    try:
        name_column = 'Name'
        b2b_column = 'B2B'
        b2c_column = 'B2C'

        # Check if the required columns exist in the DataFrame
        if any(col not in df.columns for col in [name_column, b2b_column, b2c_column]):
            raise KeyError(f"One or more required columns do not exist in the DataFrame.")

        # Create a grouped DataFrame based on unique 'Name'
        grouped_data = df.drop_duplicates(subset=[name_column])

        # Count the B2B and B2C orders
        total_b2b_orders = grouped_data[b2b_column].notna().sum()
        total_b2c_orders = grouped_data[b2c_column].notna().sum()

        return total_b2b_orders, total_b2c_orders

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
# total_b2b, total_b2c = count_unique_b2b_b2c_orders(df)
# print("Total B2B Orders:", total_b2b)
# print("Total B2C Orders:", total_b2c)
