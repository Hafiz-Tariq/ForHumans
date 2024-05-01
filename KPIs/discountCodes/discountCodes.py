
def discount_codes(df):
    """
    Processes a DataFrame to count occurrences of each discount code and filters for codes used more than once.

    Parameters:
    df (pd.DataFrame): DataFrame containing a column named 'Discount Code'.

    Returns:
    pd.DataFrame: A DataFrame with two columns: 'Discount Code' and 'Count', listing codes that appear more than once.

    Raises:
    KeyError: If the 'Discount Code' column is missing from the input DataFrame.
    """
    try:
        # Check if the 'Discount Code' column exists
        if 'Discount Code' not in df.columns:
            raise KeyError("DataFrame does not contain a 'Discount Code' column.")

        # Drop rows where the 'Discount Code' is NaN and count occurrences of each code
        discount_counts = df['Discount Code'].dropna().value_counts()

        # Filter counts to only include codes used more than once
        discount_counts = discount_counts[discount_counts > 1]

        # Convert the Series to a DataFrame
        result_df = discount_counts.reset_index()
        result_df.columns = ['Discount Code', 'Count']

        return result_df

    except KeyError as e:
        print(f"Error: {str(e)}")
        # Optionally, return an empty DataFrame or re-raise the exception depending on your use case
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None

# Example usage:
# Assuming 'data' is your original DataFrame loaded from the Excel file
# result = count_discount_codes(data)
# print(result)
