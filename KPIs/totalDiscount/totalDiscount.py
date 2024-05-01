
def sum_discount_amount(df):
    """
    Calculate the total sum of the 'Discount Amount' column in the given DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing the 'Discount Amount' column.

    Returns:
    float: The sum of the 'Discount Amount' column.

    Raises:
    KeyError: If the 'Discount Amount' column does not exist in the DataFrame.
    TypeError: If the values in the 'Discount Amount' column are not numeric.
    """
    try:
        # Sum the 'Discount Amount' column
        discount_sum = df['Discount Amount'].sum()
        return discount_sum
    except KeyError:
        # Raise an error if the 'Discount Amount' column is missing
        raise KeyError("The 'Discount Amount' column is not present in the DataFrame.")
    except TypeError:
        # Raise an error if the values in the 'Discount Amount' column are not numeric
        raise TypeError("Non-numeric values found in the 'Discount Amount' column.")
    except Exception as e:
        # General exception handling, should there be an unexpected error
        raise Exception(f"An unexpected error occurred: {str(e)}")

# Example usage:
# try:
#     discount_total = sum_discount_amount(data)
#     print(f"The total discount amount is: {discount_total}")
# except Exception as e:
#     print(e)
