import pandas as pd


def mark_tag_matches(dataframe):
    """
    Adds a new column 'Sample' to the dataframe where entries in 'Tags_aggregated' match
    a predefined set of tag combinations, after converting both to lowercase. Entries with matching tags
    are marked as True, while others remain blank.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe containing a 'Tags_aggregated' column.

    Returns:
        pd.DataFrame: The dataframe with an additional 'Sample' column.

    Raises:
        ValueError: If the 'Tags_aggregated' column is not present in the dataframe.
    """
    # Define the list of tag combinations to match, all converted to lowercase
    tag_combinations = {
        "b2b, instagram, muster",
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
        # Apply a function to check if each entry in 'Tags_aggregated', converted to lowercase, matches any of the tag combinations
        dataframe['Sample'] = dataframe['Tags_aggregated'].apply(
            lambda tag: True if pd.notna(tag) and tag.lower() in tag_combinations else None
        )
        return dataframe
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        raise

# Example usage:
# Assuming 'df' is your dataframe loaded with data including 'Tags_aggregated' column:
# updated_df = mark_tag_matches(df)
