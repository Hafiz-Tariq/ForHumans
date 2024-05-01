
def calculate_sku_costs(dataframe):
    """
    Calculates the total costs for 'E-Text' and 'E-Logo' items in the 'Lineitem sku' column
    of a pandas DataFrame based on their quantities and predefined unit prices. Handles NaN values in 'Lineitem sku'.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the 'Lineitem sku' and 'Lineitem quantity' columns.

    Returns:
    tuple: A tuple containing the total cost for 'E-Text' and 'E-Logo', respectively.

    Raises:
    ValueError: If the required columns are missing from the DataFrame.
    """
    try:
        # Ensure the DataFrame contains the necessary columns
        required_columns = {'Lineitem sku', 'Lineitem quantity'}
        if not required_columns.issubset(dataframe.columns):
            missing = required_columns - set(dataframe.columns)
            raise ValueError(f"The DataFrame is missing the following required columns: {missing}")

        # Clean the 'Lineitem sku' column to handle NaN values
        dataframe['Lineitem sku'] = dataframe['Lineitem sku'].fillna('')

        # Filter rows for 'E-Text' and 'E-Logo'
        e_text_filter = dataframe['Lineitem sku'].str.contains('E-Text')
        e_logo_filter = dataframe['Lineitem sku'].str.contains('E-Logo')

        # Calculate costs
        e_text_cost = (dataframe.loc[e_text_filter, 'Lineitem quantity'] * 8).sum()
        e_logo_cost = (dataframe.loc[e_logo_filter, 'Lineitem quantity'] * 15).sum()

        return e_text_cost, e_logo_cost

    except Exception as e:
        # Generic exception handling, could be specified further depending on context
        print(f"An error occurred: {e}")
        return None

# Example usage:
# df = pd.read_excel('your_file_path.xlsx')
# total_costs = calculate_sku_costs(df)
# print(f"Total cost for E-Text: {total_costs[0]} Euro, Total cost for E-Logo: {total_costs[1]} Euro")
