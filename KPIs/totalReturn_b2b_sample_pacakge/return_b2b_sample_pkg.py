import pandas as pd


def count_matched_orders(df1, df2):
    """
    Counts the number of entries where the unique 'Cleaned_Order_Number' in df1 matches the unique 'Name' in df2
    and both 'B2B' and 'Sample' columns in df2 are True. This function ensures that unique IDs from df1 and unique Names from df2 are considered.

    Parameters:
        df1 (pandas.DataFrame): First dataframe with columns 'Cleaned_Order_Number' and 'ID'.
        df2 (pandas.DataFrame): Second dataframe with columns 'Name', 'B2B', and 'Sample'.

    Returns:
        int: Count of matched rows where both 'B2B' and 'Sample' are True.

    Raises:
        KeyError: If any of the required columns are missing in the input dataframes.
        Exception: For any other issues during function execution.
    """
    try:
        # Filter unique entries based on 'ID' in df1 and 'Name' in df2
        df1_unique = df1.drop_duplicates(subset=['ID'])
        df2_unique = df2.drop_duplicates(subset=['Name'])

        # Merging dataframes on df1['Cleaned_Order_Number'] and df2['Name']
        merged_df = pd.merge(df1_unique, df2_unique, left_on='Cleaned_Order_Number', right_on='Name')

        # Filtering rows where both 'B2B' and 'Sample' are True
        filtered_df = merged_df[(merged_df['B2B'] == True) & (merged_df['Sample'] == True)]

        # Returning the count of rows that meet the condition
        return filtered_df.shape[0]
    except KeyError as e:
        print(f"KeyError: Missing column in the dataframe - {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
