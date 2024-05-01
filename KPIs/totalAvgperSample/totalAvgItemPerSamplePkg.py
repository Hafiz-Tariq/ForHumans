
def calculate_b2b_sample_ratio(df):
    """
    This function calculates the ratio of the total line item quantity to the number of unique names
    in a DataFrame where both 'B2B' and 'Sample' columns are true.

    Parameters:
    - df (pd.DataFrame): The DataFrame containing the business data with 'B2B', 'Sample', 'Lineitem quantity', and 'Name' columns.

    Returns:
    - int: The rounded up value of the division of total line item quantity by the number of unique names.
    """
    try:
        # Filter the DataFrame where both 'B2B' and 'Sample' are True
        filtered_df = df[(df['B2B'] == 1) & (df['Sample'] == 1)]

        # Sum the 'Lineitem quantity' for the filtered DataFrame
        total_quantity = filtered_df['Lineitem quantity'].sum()

        # Count the unique 'Name' values in the filtered DataFrame
        unique_names_count = filtered_df['Name'].nunique()

        # Calculate the ratio and round up
        ratio = total_quantity / unique_names_count

        return round(ratio, 2)
    except KeyError as e:
        # Handle the case where one of the necessary columns does not exist in the DataFrame
        print(f"Missing column: {e}")
        return None
    except ZeroDivisionError:
        # Handle division by zero if there are no unique names
        print("Division by zero encountered due to no unique names.")
        return None
    except Exception as e:
        # Handle any other unforeseen exceptions
        print(f"An error occurred: {e}")
        return None

# Example usage:
# Assuming `data` is your DataFrame loaded from an Excel file.
# result = calculate_b2b_sample_ratio(data)
# print(result)
