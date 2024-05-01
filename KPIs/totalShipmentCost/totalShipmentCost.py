
def calculate_total_shipping(dataframe):
    """
    Calculates the total shipping cost from the 'Shipping' column in a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the 'Shipping' column.

    Returns:
    float: The total shipping cost.

    Raises:
    ValueError: If the 'Shipping' column is missing from the DataFrame.
    """
    try:
        # Ensure the DataFrame contains the 'Shipping' column
        if 'Shipping' not in dataframe.columns:
            raise ValueError("The DataFrame does not contain the 'Shipping' column.")

        # Calculate the sum of the shipping costs
        total_shipping_cost = dataframe['Shipping'].sum()

        return total_shipping_cost

    except Exception as e:
        # Generic exception handling, could be specified further depending on context
        print(f"An error occurred: {e}")
        return None

# Example usage:
# df = pd.read_excel('your_file_path.xlsx')
# shipping_cost = calculate_total_shipping(df)
# print(f"Total shipping cost: {shipping_cost} Euro")
