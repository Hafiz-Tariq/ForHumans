import pandas as pd


def clean_order_numbers(df):
    """
    Cleans and transforms order numbers in a specified column of a DataFrame.

    Parameters:
    - df: pd.DataFrame, the dataframe containing the order numbers.

    Returns:
    - pd.DataFrame: The DataFrame with an additional column `Cleaned_Order_Number` with the cleaned values.
    """
    def transform_entry(entry):
        if pd.isna(entry):
            return None  # Keeps NaN as NaN (blank)

        entry = str(entry).strip()
        if entry.isdigit() and len(entry) == 4:
            # Transform 4-digit numbers to B-XXXX format
            return f"B-{entry}"
        elif entry.upper().startswith('B-'):
            # Normalize entries starting with B- and ensure correct format
            normalized = entry.upper()
            # Extract first four digits after B- if present
            digits = ''.join(filter(str.isdigit, normalized[2:6]))  # Look at up to four digits following B-
            if len(digits) == 4:
                return f"B-{digits}"
            else:
                return None
        elif entry.upper().startswith('B'):
            # Handle cases where B is followed directly by digits without a hyphen
            normalized = entry.upper().replace('B', 'B-', 1)
            digits = ''.join(filter(str.isdigit, normalized[2:6]))  # Look at up to four digits following B-
            if len(digits) == 4:
                return f"B-{digits}"
            else:
                return None
        else:
            return None  # Leave other formats as blank

    column_name = 'Original order number/Order number'
    return_type_column = 'Return type'

    # Filter the DataFrame where 'Return type' is 'CUSTOMER'
    customer_df = df[df[return_type_column] == 'CUSTOMER'].copy()  # Explicitly create a copy to modify

    # Apply the transformation function to the specified column using loc to avoid SettingWithCopyWarning
    customer_df.loc[:, 'Cleaned_Order_Number'] = customer_df[column_name].apply(transform_entry)
    return customer_df

# Usage example:
# updated_df = clean_order_numbers(input_dataframe)
