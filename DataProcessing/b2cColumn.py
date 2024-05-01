import pandas as pd


def mark_b2c_matches(dataframe):
    """
    Adds a new column 'B2C' to the dataframe where entries in 'Tags_aggregated' match
    a predefined set of B2C tag combinations, after converting both to lowercase. Entries with matching tags
    are marked as True, while others remain blank.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe containing a 'Tags_aggregated' column.

    Returns:
        pd.DataFrame: The dataframe with an additional 'B2C' column.

    Raises:
        ValueError: If the 'Tags_aggregated' column is not present in the dataframe.
    """
    # Define the list of B2C tag combinations to match, all converted to lowercase
    b2c_combinations = {
        "has-embroidery", "marketingmuster", "umtausch", "test", "pacura herbsfest",
        "has-embroidery, marketingmuster", "has-embroidery, stickmuster",
        "has-embroidery, schweiz", "gewinnspiel", "marketingmuster, muster",
        "marketing muster, marketingmuster", "return-declined, test", "whatsapp",
        "cp_filtered, return-pending, test", "has-embroidery, test",
        "marketingmuster, muster, produktmuster", "abschreiben, produktmuster",
        "order-problem", "marketing muster", "abschreiben", "b2c"
    }

    # Check if the necessary column exists in the dataframe
    if 'Tags_aggregated' not in dataframe.columns:
        raise ValueError("The dataframe must contain a 'Tags_aggregated' column.")

    try:
        # Apply a function to check if each entry in 'Tags_aggregated',
        # converted to lowercase, matches any of the B2C combinations
        dataframe['B2C'] = dataframe['Tags_aggregated'].apply(
            lambda tag: True if pd.notna(tag) and tag.lower() in b2c_combinations else None
        )
        return dataframe
    except Exception as e:
        print(f"An error occurred while processing the data: {e}")
        raise

# Example usage:
# Assuming 'df' is your dataframe loaded with data including 'Tags_aggregated' column:
# updated_df = mark_b2c_matches(df)
