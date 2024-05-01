import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_yearly_cohort_heatmaps(df):
    """
    Generates and saves heatmap visualizations for overall, B2B, and B2C yearly customer retention cohorts from a given DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing customer order data.

    Returns:
    - None: The function saves the heatmap images as files and does not return any values.
    """
    try:
        # Ensure 'Created at' and 'Email' are in the correct format
        df['Created at'] = pd.to_datetime(df['Created at'])
        df['Order Year'] = df['Created at'].dt.to_period('Y')

        # Define a nested function for creating and saving heatmaps
        def create_and_save_heatmap(data, customer_type):
            data = data.copy()  # Make a copy of the data to avoid SettingWithCopyWarning
            data['Cohort Year'] = data.groupby('Email')['Created at'].transform('min').dt.to_period('Y')
            cohort_data = data.groupby(['Cohort Year', 'Order Year']).agg(
                n_customers=('Email', 'nunique')).reset_index()
            cohort_data['Period Number'] = (cohort_data['Order Year'] - cohort_data['Cohort Year']).apply(lambda x: x.n)
            cohort_pivot = cohort_data.pivot_table(index='Cohort Year', columns='Period Number', values='n_customers',
                                                   aggfunc='sum')

            plt.figure(figsize=(10, 6))
            sns.heatmap(cohort_pivot, annot=True, cmap='Blues', fmt='.0f', linewidths=.5, )
            plt.title(f'{customer_type} Yearly Customer Retention Cohort')
            plt.ylabel('Cohort Year')
            plt.xlabel('Years Since First Purchase')
            plt.savefig(f'{customer_type}_yearly_retention_cohort.png')
            plt.close()

        # Generate heatmaps for overall, B2B, and B2C
        create_and_save_heatmap(df, 'Overall')

        if 'B2B' in df.columns:
            b2b_data = df[df['B2B'] == 1]
            create_and_save_heatmap(b2b_data, 'B2B')

        if 'B2C' in df.columns:
            b2c_data = df[df['B2C'] == 1]
            create_and_save_heatmap(b2c_data, 'B2C')

    except Exception as e:
        print(f"An error occurred: {e}")


# # Usage in your main code block
# if __name__ == '__main__':
#     # Assuming 'dataframe' is your DataFrame loaded elsewhere
#     generate_yearly_cohort_heatmaps(dataframe)
#     # The images are saved in the current directory and can be opened with an image viewer
