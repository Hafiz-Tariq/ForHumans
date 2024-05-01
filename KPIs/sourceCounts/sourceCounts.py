
def source_value_counts(dataframe):
    """
    Returns the count of each source type in the 'Source' column of a DataFrame after removing null values.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing the 'Source' column.

    Returns:
    pd.Series: A Series containing the count of each source type.

    Raises:
    ValueError: If the 'Source' column is missing in the DataFrame.
    """
    try:
        # Check if the 'Source' column exists
        if 'Source' not in dataframe:
            raise ValueError("DataFrame must include a 'Source' column.")

        # Remove null values from the 'Source' column and count each unique value
        source_counts = dataframe['Source'].dropna().value_counts()

        return source_counts

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None
