import pandas as pd
import numpy as np
import re


def convert_tags_in_dataframe(df):
    """
    Takes a DataFrame, checks for a 'Tags' column, and converts the values based on specific rules:
    - Convert all values containing "B2b" and "muster" into "Sample"
    - Convert all values containing only "b2b" into "b2b"
    - Everything else is converted into "B2C"
    Missing values are kept unchanged.

    Parameters:
    - df: pandas.DataFrame

    Returns:
    - pandas.DataFrame with updated 'Converted Tags' column

    Note:
    - We are converting Tag column to b2b and b2c and sample, where sample and b2b work as b2b.
      While other work as b2c.
    """
    try:
        # Check if 'Tags' column exists
        if 'Tags' not in df.columns:
            print("The DataFrame does not contain a 'Tags' column.")
            return None

        def convert_tags_with_regex(tag):
            if pd.isna(tag):
                return np.nan  # Keeping NaN values unchanged
            tag_lower = tag.lower()
            if re.search(r'\bb2b\b', tag_lower) and re.search(r'\bmuster\b', tag_lower):
                return "Sample"
            elif re.search(r'\bb2b\b', tag_lower):
                return "b2b"
            else:
                return "B2C"

        # Apply the conversion function to the 'Tags' column
        df['Tags'] = df['Tags'].apply(convert_tags_with_regex)
        return df

    except ValueError as e:
        print(f"ValueError: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None
