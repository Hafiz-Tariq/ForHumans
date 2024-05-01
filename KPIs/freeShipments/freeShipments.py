
def count_free_shipments(dataframe):
    """
    Counts the number of free shipments in the 'Shipping' column of a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the 'Shipping' column.

    Returns:
    int: The count of free shipments (shipping cost is zero).

    Raises:
    ValueError: If the 'Shipping' column is missing from the DataFrame.
    """
    try:
        # Ensure the DataFrame contains the 'Shipping' column
        if 'Shipping' not in dataframe.columns:
            raise ValueError("The DataFrame does not contain the 'Shipping' column.")

        # Count the number of times the shipping cost is zero
        free_shipping_count = (dataframe['Shipping'] == 0).sum()

        return free_shipping_count

    except Exception as e:
        # Generic exception handling, could be specified further depending on context
        print(f"An error occurred: {e}")
        return None

# Example usage:
# df = pd.read_excel('your_file_path.xlsx')
# num_free_shipments = count_free_shipments(df)
# print(f"Number of free shipments: {num_free_shipments}")
