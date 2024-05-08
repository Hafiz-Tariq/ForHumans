import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def generate_yearly_cohort_heatmaps_display(df):
    """
    Generates heatmap visualizations for overall, B2B, and B2C yearly customer retention cohorts from a given DataFrame.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing customer order data.

    Returns:
    - dict: A dictionary containing matplotlib figure objects for each customer type.
    """
    heatmaps = {}
    try:
        df['Created at'] = pd.to_datetime(df['Created at'])
        df['Order Year'] = df['Created at'].dt.to_period('Y')

        def create_heatmap(data, customer_type):
            # Ensure 'Cohort Year' assignment modifies the original DataFrame
            data.loc[:, 'Cohort Year'] = data.groupby('Email')['Created at'].transform('min').dt.to_period('Y')
            cohort_data = data.groupby(['Cohort Year', 'Order Year']).agg(
                n_customers=('Email', 'nunique')).reset_index()
            cohort_data['Period Number'] = (cohort_data['Order Year'] - cohort_data['Cohort Year']).apply(lambda x: x.n)
            cohort_pivot = cohort_data.pivot_table(index='Cohort Year', columns='Period Number', values='n_customers',
                                                   aggfunc='sum')

            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(cohort_pivot, annot=True, cmap='Blues', fmt='.0f', linewidths=.5, ax=ax)
            ax.set_title(f'{customer_type} Yearly Customer Retention Cohort')
            ax.set_ylabel('Cohort Year')
            ax.set_xlabel('Years Since First Purchase')
            return fig

        # Store figures in the dictionary
        heatmaps['Overall'] = create_heatmap(df, 'Overall')
        if 'B2B' in df.columns:
            b2b_data = df[df['B2B'] == 1]
            heatmaps['B2B'] = create_heatmap(b2b_data, 'B2B')
        if 'B2C' in df.columns:
            b2c_data = df[df['B2C'] == 1]
            heatmaps['B2C'] = create_heatmap(b2c_data, 'B2C')

    except Exception as e:
        print(f"An error occurred: {e}")

    return heatmaps
