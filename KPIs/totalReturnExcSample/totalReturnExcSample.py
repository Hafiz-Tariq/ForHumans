import pandas as pd


def process_dataframes(returns_df, test_df):
    """
    Process the returns and test dataframes by matching and filtering specific columns.

    Args:
    returns_df (pd.DataFrame): DataFrame containing returns data.
    test_df (pd.DataFrame): DataFrame containing test data.

    Returns:
    int: Count of unique IDs after processing.

    Raises:
    Exception: If any errors occur during the data processing.
    """
    try:
        # Ensuring unique IDs in returns dataframe
        returns_df_unique = returns_df.drop_duplicates(subset=['ID'])

        # Filtering test dataframe based on unique names and where Sample is True
        test_df_filtered = test_df.drop_duplicates(subset=['Name'])
        test_df_filtered = test_df_filtered[test_df_filtered['Sample'] == True]

        # Merging returns dataframe with the filtered test dataframe based on matching
        # 'Cleaned_Order_Number' with 'Name'
        merged_df = returns_df_unique.merge(test_df_filtered,
                                            left_on='Cleaned_Order_Number', right_on='Name', how='left', indicator=True)

        # Filtering out rows where a match was found
        final_df = merged_df[merged_df['_merge'] == 'left_only']

        # Returning the count of unique IDs where no match was found
        return final_df['ID'].nunique()

    except Exception as e:
        # print(f"An error occurred: {e}")
        return None

# Example usage:
# count_remaining_ids = process_dataframes(returns_df, test_df)
# print("Remaining Unique IDs:", count_remaining_ids)
