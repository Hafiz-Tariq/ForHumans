import pandas as pd


def aggregate_tags_in_dataframe(dataframe):
    """
    Aggregates tags in a dataframe based on the 'Name' column. For each unique 'Name',
    if there is a consistent non-empty 'Tags' value across its entries, that tag is applied
    to all entries of that 'Name' in a new column 'Tags_aggregated'. If the tag values vary
    or all are empty, 'Tags_aggregated' remains empty for that 'Name'.

    Parameters:
        dataframe (pd.DataFrame): The input dataframe containing at least 'Name' and 'Tags' columns.

    Returns:
        pd.DataFrame: The dataframe with an additional 'Tags_aggregated' column.

    Raises:
        ValueError: If the required columns are not in the dataframe.
    """
    # Check if the necessary columns exist in the dataframe
    if 'Name' not in dataframe.columns or 'Tags' not in dataframe.columns:
        raise ValueError("The dataframe must contain 'Name' and 'Tags' columns.")

    # Define the aggregation function
    def aggregate_tags(tags):
        unique_tags = set(tags.dropna().unique())  # Remove NaN and get unique tags
        if len(unique_tags) == 1:
            return unique_tags.pop()  # If only one unique tag, return it
        return None  # Otherwise, return None (which will become NaN in the dataset)

    try:
        # Apply the aggregation function
        dataframe['Tags_aggregated'] = dataframe.groupby('Name')['Tags'].transform(aggregate_tags)
        return dataframe
    except Exception as e:
        print(f"An error occurred during the aggregation process: {e}")
        raise


# orders = pd.read_csv("../Data/orders_export_1.csv")
# orders = aggregate_tags_in_dataframe(orders)
# orders = mark_tag_matches(orders)
# orders = mark_b2b_matches(orders)
# orders = mark_b2c_matches(orders)
# orders.to_excel("Test.xlsx", index=False)
