
def count_discount_codes(dataframe):
    """
    Counts the total non-blank discount codes and those with lengths not equal to 6 or 7 in the 'Discount Code' column.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame containing the 'Discount Code' column.

    Returns:
    tuple: A tuple containing the total count of non-blank discount codes and the count of codes with lengths not 6 or 7.

    Raises:
    ValueError: If the 'Discount Code' column is missing from the DataFrame.
    """
    try:
        # Ensure the DataFrame contains the 'Discount Code' column
        if 'Discount Code' not in dataframe.columns:
            raise ValueError("The DataFrame does not contain the 'Discount Code' column.")

        # Drop null values and count total non-blank discount codes
        valid_discount_codes = dataframe['Discount Code'].dropna()
        total_count = valid_discount_codes.count()

        # Count discount codes whose length is not 6 or 7
        specific_count = valid_discount_codes.apply(lambda x: len(x) not in [6, 7]).sum()

        return total_count, specific_count

    except Exception as e:
        # Generic exception handling, could be specified further depending on context
        print(f"An error occurred: {e}")
        return None, None

# Example usage:
# df = pd.read_excel('your_file_path.xlsx')
# total_discount_codes, specific_discount_codes = count_discount_codes(df)
# print(f"Total non-blank discount codes: {total_discount_codes}")
# print(f"Discount codes neither 6 nor 7 in length: {specific_discount_codes}")
