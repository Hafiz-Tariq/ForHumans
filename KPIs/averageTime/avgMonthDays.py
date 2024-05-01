import pandas as pd


def calculate_time_differences(return_data, order_data):
    """
    Calculate the average of the absolute differences in days and full months between 'Created at' date in order_data
    and 'Reception date' in return_data. Assumes specific columns for matching and date calculations.

    Parameters:
        return_data (pd.DataFrame): Dataframe containing return records.
        order_data (pd.DataFrame): Dataframe containing order records.

    Returns:
        tuple: A tuple containing the average of the absolute days difference and the absolute full months difference.
    """
    try:
        # Filter out entries without a valid 'Cleaned_Order_Number' and remove duplicates based on 'ID'
        return_data_filtered = return_data.dropna(subset=['Cleaned_Order_Number'])
        return_data_filtered = return_data_filtered.drop_duplicates(subset=['ID'])

        # Remove duplicates in 'Name' from order data
        order_data_filtered = order_data.drop_duplicates(subset=['Name'])

        # Merge dataframes on matching 'Cleaned_Order_Number' and 'Name'
        merged_data = pd.merge(return_data_filtered, order_data_filtered, left_on='Cleaned_Order_Number',
                               right_on='Name')

        # Convert date columns to datetime
        merged_data['Created at'] = pd.to_datetime(merged_data['Created at'])
        merged_data['Reception date'] = pd.to_datetime(merged_data['Reception date'])

        # Calculate absolute differences in days
        merged_data['Days Difference'] = (merged_data['Created at'] - merged_data['Reception date']).dt.days.abs()

        # Calculate absolute differences in full months
        merged_data['Months Difference'] = (merged_data['Created at'].dt.year - merged_data[
            'Reception date'].dt.year) * 12 + \
                                           (merged_data['Created at'].dt.month - merged_data['Reception date'].dt.month)
        merged_data['Months Difference'] = merged_data['Months Difference'].abs()

        # Calculate averages of the absolute differences
        avg_days = merged_data['Days Difference'].mean()
        avg_months = merged_data['Months Difference'].mean()

        return avg_days, avg_months

    except Exception as e:
        print("An error occurred:", e)
        return None, None

# Example usage:
# avg_days, avg_months = calculate_time_differences(return_data, order_data)
# print("Average Days Difference:", avg_days)
# print("Average Months Difference:", avg_months)
