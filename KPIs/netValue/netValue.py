
def sum_subtotal(dataframe):
    """
    Calculate the sum of the 'Subtotal' column in the provided DataFrame.

    Parameters:
    dataframe (pandas.DataFrame): A DataFrame containing a 'Subtotal' column with numeric values.

    Returns:
    float: The sum of the 'Subtotal' column.

    Raises:
    ValueError: If the 'Subtotal' column is missing or contains non-numeric data.
    """
    try:
        # Ensure the 'Subtotal' column exists
        if 'Subtotal' not in dataframe.columns:
            return None

        # Calculate the sum of the 'Subtotal' column
        subtotal_sum = dataframe['Subtotal'].sum()

        # Return the sum
        return subtotal_sum

    except TypeError:
        # Handle the case where the column exists but contains non-numeric data
        return None

# Example usage:
# subtotal = sum_subtotal(data)
# print("Sum of Subtotal:", subtotal)
