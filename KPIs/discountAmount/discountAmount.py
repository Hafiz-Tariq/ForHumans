import re


def analyze_discounts_and_names(df):
    """
    Analyzes a DataFrame to compute the sum of 'Discount Amount' for certain 'Discount Code' values
    (excluding those with exactly 6 or 7 digits) and counts unique values in the 'Name' column.

    Parameters:
    df (pd.DataFrame): The DataFrame that contains 'Discount Code', 'Discount Amount', and 'Name' columns.

    Returns:
    tuple: A tuple containing the total sum of the 'Discount Amount' and the number of unique 'Name' values.

    Raises:
    KeyError: If the required columns are not in the DataFrame.
    """
    try:
        # Ensure required columns are present
        required_columns = ['Discount Code', 'Discount Amount', 'Name']
        if not all(column in df.columns for column in required_columns):
            raise KeyError("Missing one or more required columns: 'Discount Code', 'Discount Amount', 'Name'")

        # Step 1: Filter out rows with NaN in 'Discount Code' and codes with exactly 6 or 7 digits
        filtered_df = df.dropna(subset=['Discount Code'])
        filtered_df = filtered_df[~filtered_df['Discount Code'].apply(lambda x: bool(re.match(r'^\d{6,7}$', x)))]

        # Step 2: Sum the 'Discount Amount' in the filtered DataFrame
        total_discount_amount = filtered_df['Discount Amount'].sum()

        # Step 3: Count unique 'Name' values in the filtered DataFrame
        unique_names_count = filtered_df['Name'].nunique()

        return round(total_discount_amount / unique_names_count, 2)

    except KeyError as e:
        print(f"Error: {str(e)}")
        return None

# Example usage:
# Assuming 'data' is your DataFrame loaded from the Excel file
# result = analyze_discounts_and_names(data)
# print("Total Discount Amount:", result[0], "Unique Names Count:", result[1])
