import pandas as pd


def analyze_rejected_shipments(data):
    """
    Analyzes the given DataFrame to determine the count and percentage of rejected shipments.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing return records.

    Returns:
        tuple: A tuple containing the count of unique rejected shipment IDs and their percentage
               of the total unique IDs in the DataFrame.
    """
    try:
        # Ensure 'Return type' and 'ID' columns are present
        if 'Return type' not in data.columns or 'ID' not in data.columns:
            return None, None

        # Calculate total unique IDs for percentage calculation
        total_unique_ids = data['ID'].nunique()

        # Filter for rejected shipments and remove duplicate IDs
        rejected_data = data[data['Return type'] == "REJECTED_SHIPMENT"]
        unique_rejected_ids = rejected_data['ID'].drop_duplicates().count()

        # Calculate percentage of rejected shipments
        if total_unique_ids == 0:
            return None, None

        percentage_rejected = (unique_rejected_ids / total_unique_ids) * 100

        return unique_rejected_ids, round(percentage_rejected, 2)

    except Exception as e:
        print("An error occurred:", e)
        return None, None

# Example usage:
# data = pd.read_excel('path_to_your_excel_file.xlsx')  # Load your data
# rejected_count, rejected_percentage = analyze_rejected_shipments(data)
# print("Rejected Count:", rejected_count)
# print("Percentage of Rejected:", rejected_percentage)
