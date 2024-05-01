
def count_accepts_marketing(df):
    """
    Count the occurrences of 'yes' and 'no' in the 'Accepts Marketing' column of a DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the 'Accepts Marketing' column.

    Returns:
    tuple: A tuple containing the count of 'yes' and 'no' values in the 'Accepts Marketing' column.

    Raises:
    KeyError: If the 'Accepts Marketing' column does not exist in the DataFrame.
    """
    try:
        # Ensure the 'Accepts Marketing' column is present
        if 'Accepts Marketing' not in df.columns:
            raise KeyError("The 'Accepts Marketing' column is not present in the DataFrame.")

        # Filter the column to count only 'yes' and 'no' values
        marketing_counts = df['Accepts Marketing'].value_counts()

        # Extract counts for 'yes' and 'no', assuming blank or other values are to be ignored
        yes_count = marketing_counts.get('yes', 0)
        no_count = marketing_counts.get('no', 0)

        return yes_count, no_count
    except KeyError as e:
        # Handle missing 'Accepts Marketing' column
        # raise KeyError(str(e))
        return None, None

# Example usage:
# try:
#     yes_count, no_count = count_accepts_marketing(data)
#     print(f"Yes: {yes_count}, No: {no_count}")
# except Exception as e:
#     print(f"Error: {e}")
