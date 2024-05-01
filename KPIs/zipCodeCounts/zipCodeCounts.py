
def classify_zip_codes(dataframe):
    """
    Classifies zip codes by their first digit and counts unique names for each class.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing at least 'Billing Zip' and 'Name' columns.

    Returns:
    pd.DataFrame: A DataFrame with two columns: 'Zip Code Class' and 'Unique Names Count',
                   containing counts of unique names for each zip code class from 0 to 9.

    Raises:
    ValueError: If the required columns are missing in the DataFrame.
    """
    try:
        # Check if necessary columns exist
        if 'Billing Zip' not in dataframe or 'Name' not in dataframe:
            raise ValueError("DataFrame must include 'Billing Zip' and 'Name' columns.")

        # Clean and extract the first digit from the 'Billing Zip' column
        dataframe['Billing Zip Cleaned'] = dataframe['Billing Zip'].astype(str).str.extract('(\d+)')
        dataframe['Zip Code Class'] = dataframe['Billing Zip Cleaned'].str[0]

        # Group by the first digit and count unique names
        result = dataframe.groupby('Zip Code Class')['Name'].nunique().reset_index()
        result.columns = ['Zip Code Class', 'Unique Names Count']

        return result

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None
