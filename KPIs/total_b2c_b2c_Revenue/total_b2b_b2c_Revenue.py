
def calculate_revenue_by_category(df):
    """
    This function calculates the total revenue, and the revenue from B2B and B2C sales.
    It sums up the 'Total' column for the entire dataframe, and then for the entries classified as B2B and B2C.

    Args:
        df (pandas.DataFrame): The dataframe containing the data.

    Returns:
        tuple: A tuple containing the total revenue, B2B revenue, and B2C revenue.

    Raises:
        KeyError: If 'Total', 'B2B', or 'B2C' columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.
    """
    try:
        total_column = 'Total'
        b2b_column = 'B2B'
        b2c_column = 'B2C'

        # Check if the required columns exist in the DataFrame
        if any(col not in df.columns for col in [total_column, b2b_column, b2c_column]):
            raise KeyError(f"One or more required columns do not exist in the DataFrame.")

        # Calculate total revenue
        total_revenue = df[total_column].sum()

        # Calculate B2B revenue
        b2b_revenue = df[df[b2b_column].notna()][total_column].sum()

        # Calculate B2C revenue
        b2c_revenue = df[df[b2c_column].notna()][total_column].sum()

        return total_revenue, b2b_revenue, b2c_revenue

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
# total_rev, b2b_rev, b2c_rev = calculate_revenue(df)
# print("Total Revenue:", total_rev)
# print("B2B Revenue:", b2b_rev)
# print("B2C Revenue:", b2c_rev)
