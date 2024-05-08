
def summarize_transactions(df):
    """
    Summarize transaction counts, B2B/B2C counts, and calculate percentages of total transactions
    for specified payment methods in the DataFrame.

    Parameters:
    df (pandas.DataFrame): The DataFrame containing transaction data.

    Returns:
    dict: A dictionary containing counts and percentages of transactions for each payment method.

    Raises:
    KeyError: If necessary columns are missing in the DataFrame.
    ValueError: If the DataFrame contains incorrect types that prevent calculations.
    Exception: For unexpected errors during the function execution.
    """
    try:
        # Define the specific payment methods of interest
        payment_methods = ['custom', 'PayPal Express Checkout', 'Shopify Payments']

        # Initialize dictionaries to store the counts
        summary = {
            "payment_counts": {method: 0 for method in payment_methods},
            "b2b_counts": {method: 0 for method in payment_methods},
            "b2c_counts": {method: 0 for method in payment_methods},
            "percentages": {method: {} for method in payment_methods}  # To store percentage calculations
        }

        # Ensure the DataFrame contains necessary columns
        required_columns = ['Payment Method', 'B2B', 'B2C']
        if not all(col in df.columns for col in required_columns):
            raise KeyError(f"DataFrame is missing one of the required columns: {required_columns}")

        # Total transactions count for percentage calculations
        total_transactions = df['Payment Method'].value_counts().sum()

        # Filter the dataframe for each payment method and count B2B, B2C, and percentages
        for method in payment_methods:
            method_df = df[df['Payment Method'] == method]
            payment_count = method_df.shape[0]
            summary['payment_counts'][method] = payment_count
            summary['b2b_counts'][method] = method_df[method_df['B2B'] == True].shape[0]
            summary['b2c_counts'][method] = method_df[method_df['B2C'] == True].shape[0]
            summary['percentages'][method] = round(
                (payment_count / total_transactions * 100) if total_transactions else 0, 2)

        allPaymentMethod = []
        b2bPaymentMethod = []
        b2cPaymentMethod = []
        totalPercentagePaymentMethod = []
        for method, count in summary['payment_counts'].items():
            # print(f"{method}: {count}")
            allPaymentMethod.append(count)
        # print(allPaymentMethod)

        for method, count in summary['b2b_counts'].items():
            # print(f"{method}: {count}")
            b2bPaymentMethod.append(count)
        # print(b2bPaymentMethod)

        for method, count in summary['b2c_counts'].items():
            # print(f"{method}: {count}")
            b2cPaymentMethod.append(count)
        # print(b2cPaymentMethod)

        for method, count in summary['percentages'].items():
            # print(f"{method}: {count}%")
            totalPercentagePaymentMethod.append(count)
        # print(totalPercentagePaymentMethod)

        return (allPaymentMethod[0], allPaymentMethod[1], allPaymentMethod[2], b2bPaymentMethod[0], b2bPaymentMethod[1],
                b2bPaymentMethod[2], b2cPaymentMethod[0], b2cPaymentMethod[1], b2cPaymentMethod[2],
                totalPercentagePaymentMethod[0], totalPercentagePaymentMethod[1], totalPercentagePaymentMethod[2])

    except KeyError as e:
        # Handle missing columns
        return None
    except TypeError as e:
        # Handle incorrect types in DataFrame calculations
        return None
    except Exception as e:
        # Handle any other unexpected errors
        return None
