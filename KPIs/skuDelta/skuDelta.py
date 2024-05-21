import pandas as pd


def calculate_delta(df):
    """
    Calculate the delta between 'Summed Quantity' and 'Return count' columns in a DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame containing 'Summed Quantity' and 'Return count' columns.

    Returns:
    pd.DataFrame: The updated DataFrame with a new 'Delta' column.

    Raises:
    ValueError: If required columns are not found in the DataFrame.
    TypeError: If input is not a DataFrame.
    """
    try:
        # Check if the input is a DataFrame
        if not isinstance(df, pd.DataFrame):
            print("The input should be a pandas DataFrame.")
            return None

        # Check if the required columns are in the DataFrame
        required_columns = ['Summed Quantity', 'Return count']
        for column in required_columns:
            if column not in df.columns:
                print(f"Missing required column: '{column}'")
                return None

        # Calculate the delta
        df['Delta'] = df['Summed Quantity'] - df['Return count']

        return df

    except TypeError as e:
        print(f"TypeError: {e}")
        return None
    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
# df = pd.read_excel('your_file.xlsx')
# updated_df = calculate_delta(df)
# print(updated_df.head())
