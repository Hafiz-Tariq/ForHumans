
def calculate_items_sold_by_category(df):
    """
    First applies forward and backward filling to standardize 'Tags' within each unique 'Name'.
    Then, calculates the total items sold and breaks it down into total B2B+Sample items sold and total B2C items sold.

    Args:
        df (pandas.DataFrame): The dataframe containing the Shopify orders data.

    Returns:
        tuple: A tuple containing the total items sold, total B2B+Sample items sold, and total B2C items sold.

    Raises:
        KeyError: If necessary columns do not exist in the dataframe.
        Exception: For handling unexpected errors that may occur during the function execution.

    Note:
        'Tags' are standardized within each 'Name' group before calculation.
        Uses 'Lineitem Quantity' to calculate total items sold and 'Tags' for categorizing into B2B+Sample and B2C.
    """
    try:
        # Columns to check
        name_column = 'Name'
        tags_column = 'Tags'
        lineitem_quantity_column = 'Lineitem quantity'

        # Ensure necessary columns exist
        if any(col not in df.columns for col in [name_column, tags_column, lineitem_quantity_column]):
            print(f"One or more necessary columns do not exist in the DataFrame.")
            return None, None, None

        # Group by 'Name' and apply logic to 'Tags' for forward and backward filling
        grouped_tags = df.groupby(name_column)[tags_column].transform(lambda x: x.bfill().ffill())
        df['Filled Tags'] = grouped_tags.apply(lambda x: 'B2B' if x in ['B2B', 'Sample'] else 'B2C')

        # Calculate total items sold
        total_items_sold = df[lineitem_quantity_column].sum()

        # Calculate total B2B+Sample items sold
        total_b2b_sample_items_sold = df[df['Filled Tags'] == 'B2B'][lineitem_quantity_column].sum()

        # Calculate total B2C items sold
        total_b2c_items_sold = df[df['Filled Tags'] == 'B2C'][lineitem_quantity_column].sum()

        return total_items_sold, total_b2b_sample_items_sold, total_b2c_items_sold

    except KeyError as e:
        print(f"KeyError: {e}")
        return None, None, None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, None, None
