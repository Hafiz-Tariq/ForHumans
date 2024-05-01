
def update_sku_quantities(order_data, sku_data):
    """
    This function updates the SKU data with summed quantities from the order data.
    It cleans and preprocesses the order data to remove unwanted entries and then calculates
    the sum of quantities for each unique SKU that matches with the SKU data. If a summed
    quantity already exists for a SKU, it adds the new quantity to the existing value.

    Parameters:
    - order_data (pd.DataFrame): The order data containing 'Lineitem sku' and 'Lineitem quantity' columns.
    - sku_data (pd.DataFrame): The SKU data containing 'SKU' column where the sums will be updated.

    Returns:
    - pd.DataFrame: Updated SKU data with a new or updated column 'Summed Quantity' that contains the summed
      quantities for matching SKUs.
    """

    try:
        if 'Summed Quantity' not in sku_data.columns:
            sku_data['Summed Quantity'] = 0

        # Filter order data where 'Sample' is None
        order_data = order_data[order_data['Sample'].isna()]

        # Clean and preprocess order data
        # Remove rows where 'Lineitem sku' is NaN or contains 'E-Text' or 'E-Logo'
        order_data = order_data[order_data['Lineitem sku'].notna()]
        order_data = order_data[~order_data['Lineitem sku'].str.contains('E-Text|E-Logo', na=True)]

        # Trim whitespace from 'Lineitem sku'
        order_data['Lineitem sku'] = order_data['Lineitem sku'].str.strip()

        # Sort 'Lineitem sku' and sum 'Lineitem quantity' for each unique SKU
        sku_quantities = order_data.groupby('Lineitem sku')['Lineitem quantity'].sum().reset_index()

        # Match summed quantities to SKU data and update or create 'Summed Quantity' column
        sku_data = sku_data.merge(sku_quantities, left_on='SKU', right_on='Lineitem sku', how='left')
        sku_data['Summed Quantity'] = sku_data['Summed Quantity'].fillna(0) + sku_data['Lineitem quantity'].fillna(0)
        sku_data.drop(columns=['Lineitem sku', 'Lineitem quantity'], inplace=True)

        return sku_data

    except Exception as e:
        # Handle possible exceptions such as wrong column names or missing data
        print(f"An error occurred: {e}")
        return None


# Example usage:
# Load your data
# order_data = pd.read_excel('path_to_order_data.xlsx')
# sku_data = pd.read_excel('path_to_sku_data.xlsx')

# If 'Summed Quantity' column doesn't exist in sku_data, initialize it

# Update the SKU data
# updated_sku_data = update_sku_quantities_v2(order_data, sku_data)
# print(updated_sku_data.head())
