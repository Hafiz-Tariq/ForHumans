
def source_value_counts(dataframe):
    """
    Returns a DataFrame containing the count of each source type in the 'Source' column of a DataFrame after removing null values.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing the 'Source' column.

    Returns:
    pd.DataFrame: A DataFrame with two columns: 'Source' and 'Count', listing each source and its count.

    Raises:
    ValueError: If the 'Source' column is missing in the DataFrame.
    """
    try:
        # Check if the 'Source' column exists
        if 'Source' not in dataframe.columns:
            raise ValueError("DataFrame must include a 'Source' column.")

        # Remove null values from the 'Source' column and count each unique value
        source_counts = dataframe['Source'].dropna().value_counts()

        # Convert the Series to a DataFrame
        source_counts_df = source_counts.reset_index()
        source_counts_df.columns = ['Source', 'Count']

        return source_counts_df

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None
