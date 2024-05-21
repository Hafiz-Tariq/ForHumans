
def source_value_counts(dataframe, substr):
    """
    Returns a DataFrame containing the count of each source type in the 'Source' column of a DataFrame
    after removing null values. An optional prefix can be added to each source value.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing the 'Source' column.
    substr (str): The prefix to add to each source value. Default is "all".

    Returns:
    pd.DataFrame: A DataFrame with two columns: 'Source' and 'Count', listing each source and its count
    with the prefix added to the source values.

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

        # Add the prefix to each source value
        source_counts_df['Source'] = source_counts_df['Source'].apply(lambda x: f"{substr}_{x}")

        return source_counts_df

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage:
# df = pd.read_excel('your_file.xlsx')
# updated_counts_df = source_value_counts(df, substr="all")
# print(updated_counts_df.head())
