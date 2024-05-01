import pandas as pd


def update_sku_with_returns(return_data, sku_data):
    """
    Updates the SKU dataframe with a 'Return count' column that reflects the number of unique return instances per SKU.
    It first removes blanks in the 'Sku' column from the return data, aggregates this data, and checks for unique 'ID's
    within each 'Sku' grouping. It then updates the SKU data with these counts, adding to existing counts if necessary.

    Parameters:
        return_data (pd.DataFrame): DataFrame containing return records with 'Sku' and 'ID' columns.
        sku_data (pd.DataFrame): DataFrame containing SKU records with a 'SKU' column.

    Returns:
        pd.DataFrame: Updated SKU dataframe with an additional 'Return count' column reflecting the number of returns.
    """
    try:
        # Remove NA values from 'Sku' and prepare for aggregation
        clean_return_data = return_data.dropna(subset=['Sku'])

        # Group by 'Sku' and count unique 'ID's within each group
        sku_counts = clean_return_data.groupby('Sku')['ID'].nunique()

        # Create or update 'Return count' column in sku_data based on the counts
        sku_data['Return count'] = sku_data['SKU'].map(sku_counts).fillna(0).astype(int)

        return sku_data

    except Exception as e:
        print("An error occurred:", e)
        return None

# Example usage:
# return_data = pd.read_excel('path_to_return_data.xlsx')  # Load your return data
# sku_data = pd.read_excel('path_to_sku_data.xlsx')  # Load your SKU data
# updated_sku_data = update_sku_with_return_counts(return_data, sku_data)
# print(updated_sku_data.head())
