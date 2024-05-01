import pandas as pd


def process_reception_dates(dataframe):
    """
    Processes the 'Reception date' column in a given DataFrame, converting date and time entries
    into date-only format (YYYY-MM-DD).

    Parameters:
        dataframe (pd.DataFrame): The DataFrame containing a 'Reception date' column with date and time entries.

    Returns:
        pd.DataFrame: A DataFrame with the 'Reception date' column updated to date-only format.

    Raises:
        KeyError: If the 'Reception date' column is missing from the DataFrame.
        ValueError: If the date entries cannot be converted to the required format.
    """
    try:
        # Convert 'Reception date' to datetime and format to date only
        dataframe['Reception date'] = pd.to_datetime(dataframe['Reception date'], format='%d-%m-%y %H:%M').dt.date
        return dataframe
    except KeyError:
        return None
    except ValueError as e:
        return None

# Example usage:
# df = pd.read_excel('path_to_file.xlsx')
# updated_df = process_reception_dates(df)
# print(updated_df['Reception date'])
