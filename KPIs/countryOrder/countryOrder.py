
def count_unique_names_by_country(dataframe):
    """
    Counts unique names for each billing country in the provided DataFrame.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing at least 'Billing Country' and 'Name' columns.

    Returns:
    pd.DataFrame: A DataFrame with two columns: 'Billing Country' and 'Unique Names Count',
                   containing counts of unique names for each country.

    Raises:
    ValueError: If the required columns are missing in the DataFrame.
    """
    try:
        # Check if necessary columns exist
        if 'Billing Country' not in dataframe or 'Name' not in dataframe:
            raise ValueError("DataFrame must include 'Billing Country' and 'Name' columns.")

        # Group by 'Billing Country' and count unique names
        result = dataframe.groupby('Billing Country')['Name'].nunique().reset_index()
        result.columns = ['Billing Country', 'Unique Names Count']

        return result

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None
