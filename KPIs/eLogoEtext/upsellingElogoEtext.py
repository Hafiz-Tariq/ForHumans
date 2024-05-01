
def count_sku_types(dataframe):
    """
    Counts the occurrences of 'E-Text' and 'E-Logo' in the 'Lineitem sku' column of a pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the 'Lineitem sku' column.

    Returns:
    tuple: A tuple containing the counts of 'E-Text' and 'E-Logo', respectively.

    Raises:
    ValueError: If the 'Lineitem sku' column is missing from the DataFrame.
    """
    try:
        # Ensure the DataFrame contains the necessary column
        if 'Lineitem sku' not in dataframe.columns:
            raise ValueError("The DataFrame does not contain the 'Lineitem sku' column.")

        # Count occurrences of 'E-Text' and 'E-Logo'
        e_text_count = dataframe['Lineitem sku'].str.contains('E-Text').sum()
        e_logo_count = dataframe['Lineitem sku'].str.contains('E-Logo').sum()

        return e_text_count, e_logo_count

    except Exception as e:
        # Generic exception handling, could be specified further depending on context
        print(f"An error occurred: {e}")
        return None, None

# Example usage:
# df = pd.read_excel('your_file_path.xlsx')
# result = count_sku_types(df)
# print(result)
