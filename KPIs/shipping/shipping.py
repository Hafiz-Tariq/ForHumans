def sum_shipping(dataframe):
    """
    Calculate the sum of the 'Shipping' column in the provided DataFrame.

    Parameters:
    dataframe (pandas.DataFrame): A DataFrame containing a 'Shipping' column with numeric values.

    Returns:
    float: The sum of the 'Shipping' column.

    Raises:
    ValueError: If the 'Shipping' column is missing or contains non-numeric data.
    """
    try:
        # Ensure the 'Shipping' column exists
        if 'Shipping' not in dataframe.columns:
            raise ValueError("The dataframe does not contain a 'Shipping' column.")

        # Calculate the sum of the 'Shipping' column
        shipping_sum = dataframe['Shipping'].sum()

        # Return the sum
        return shipping_sum

    except TypeError:
        return None

# Example usage:
# shipping_total = sum_shipping(data)
# print("Sum of Shipping:", shipping_total)
