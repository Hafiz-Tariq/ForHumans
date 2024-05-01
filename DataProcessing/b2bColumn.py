import pandas as pd


def mark_b2b_matches(dataframe):
    """
    Adds a new column 'B2B' to the dataframe where entries in 'Tags_aggregated' match
    a predefined set of B2B tag combinations, after converting both to lowercase. Entries with matching tags
    are marked as True, while others remain blank.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe containing a 'Tags_aggregated' column.

    Returns:
        pd.DataFrame: The dataframe with an additional 'B2B' column.

    Raises:
        ValueError: If the 'Tags_aggregated' column is not present in the dataframe.
    """
    # Define the list of B2B tag combinations to match, all converted to lowercase
    b2b_combinations = {
        "b2b, instagram, muster",
        "b2b",
        "b2b, has-embroidery",
        "b2b, muster",
        "b2b, influencer, instagram, muster",
        "b2b, influencer, muster",
        "b2b, cold calling, muster",
        "muster",
        "cold calling, muster",
        "produktmuster",
        "marketingmuster, produktmuster",
        "muster, produktmuster"
    }

    # Check if the necessary column exists in the dataframe
    if 'Tags_aggregated' not in dataframe.columns:
        raise ValueError("The dataframe must contain a 'Tags_aggregated' column.")

    try:
        # Apply a function to check if each entry in 'Tags_aggregated', converted to lowercase,
        # matches any of the B2B combinations
        dataframe['B2B'] = dataframe['Tags_aggregated'].apply(
            lambda tag: True if pd.notna(tag) and tag.lower() in b2b_combinations else None
        )
        return dataframe
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        raise

# Example usage:
# Assuming 'df' is your dataframe loaded with data including 'Tags_aggregated' column:
# updated_df = mark_b2b_matches(df)
