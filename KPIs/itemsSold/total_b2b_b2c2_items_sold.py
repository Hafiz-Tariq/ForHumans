import pandas as pd


def calculate_items_sold_by_category(df):
    """
    This function calculates the total number of items sold, and the items sold in B2B and B2C categories.
    It sums up the 'Lineitem quantity' column for the entire dataframe, and then for the entries classified as B2B and B2C.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.

    Returns:
        tuple: A tuple containing the total items sold, total B2B items sold, and total B2C items sold.

    Raises:
        KeyError: If 'Lineitem quantity', 'B2B', or 'B2C' columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.
    """
    try:
        quantity_column = 'Lineitem quantity'
        b2b_column = 'B2B'
        b2c_column = 'B2C'

        # Check if the required columns exist in the DataFrame
        if any(col not in df.columns for col in [quantity_column, b2b_column, b2c_column]):
            raise KeyError(f"One or more required columns do not exist in the DataFrame.")

        # Calculate total items sold
        total_items_sold = df[quantity_column].sum()

        # Calculate total B2B items sold
        total_b2b_items_sold = df[df[b2b_column].notna()][quantity_column].sum()

        # Calculate total B2C items sold
        total_b2c_items_sold = df[df[b2c_column].notna()][quantity_column].sum()

        return total_items_sold, total_b2b_items_sold, total_b2c_items_sold

    except KeyError as e:
        # Handle the case where the specified columns are not found in the dataframe
        print(f"KeyError: {e}")
        return None, None, None
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Exception: {e}")
        return None, None, None

# Usage example:
# Ensure you load your DataFrame as 'df' before using this function
# df = pd.read_excel('your_data_file.xlsx')
# total_items, total_b2b_items, total_b2c_items = calculate_items_sold(df)
# print("Total items sold:", total_items)
# print("Total B2B items sold:", total_b2b_items)
# print("Total B2C items sold:", total_b2c_items)
