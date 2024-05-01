
def count_warehouse_values(df):
    """
    Counts occurrences of 'COMPLAINT' and 'FOR_SALE' in the 'Target warehouse' column of a dataframe.

    Parameters:
    - df (pd.DataFrame): Dataframe with a 'Target warehouse' column.

    Returns:
    - tuple: Tuple containing counts of 'COMPLAINT' and 'FOR_SALE'.

    Raises:
    - ValueError: If the 'Target warehouse' column is missing from the dataframe or other input errors.
    """

    try:
        # Check if the 'Target warehouse' column is in the dataframe
        if 'Target warehouse' not in df.columns:
            raise ValueError("Dataframe must contain a 'Target warehouse' column.")

        # Remove rows with blank 'Target warehouse' values
        filtered_df = df.dropna(subset=['Target warehouse'])

        # Count occurrences of 'COMPLAINT' and 'FOR_SALE'
        complaint_count = (filtered_df['Target warehouse'] == 'COMPLAINT').sum()
        for_sale_count = (filtered_df['Target warehouse'] == 'FOR_SALE').sum()

        return complaint_count, for_sale_count

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None, None

# Example usage:
# try:
#     counts = count_warehouse_values(returns_data)
#     print(f"COMPLAINT count: {counts[0]}, FOR_SALE count: {counts[1]}")
# except Exception as e:
#     print(f"Error: {e}")
