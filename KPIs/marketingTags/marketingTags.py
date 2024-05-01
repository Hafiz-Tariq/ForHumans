import pandas as pd


def count_names_with_marketing_tags(dataframe):
    """
    Counts the number of unique names associated with tags that contain "Marketing" in a DataFrame.

    Args:
    dataframe (pd.DataFrame): The DataFrame containing at least 'Name' and 'Tags_aggregated' columns.

    Returns:
    int: The count of unique names associated with tags that contain "Marketing".

    Raises:
    ValueError: If the required columns are missing in the DataFrame.
    """
    try:
        # Check if necessary columns exist
        if 'Name' not in dataframe or 'Tags_aggregated' not in dataframe:
            raise ValueError("DataFrame must include 'Name' and 'Tags_aggregated' columns.")

        # Remove duplicates from the "Name" column
        names_deduped = dataframe['Name'].drop_duplicates()

        # Remove blanks from "Tags_aggregated" column and filter for "Marketing"
        names_with_marketing_tags = dataframe[
            dataframe['Tags_aggregated'].str.contains('marketing', case=False, na=False)
        ]['Name'].drop_duplicates()

        # Count the unique names that are left after these filters
        return names_with_marketing_tags.count()

    except Exception as e:
        # Handle unexpected exceptions
        print(f"An error occurred: {e}")
        return None
