import pandas as pd
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c_unique_customer.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c


def main(orders, returns):
    """Main function to process order and return data for dynamic date ranges."""
    # Determine the min and max dates across both datasets
    min_date = min(orders['Created at'].min(), returns['Reception date'].min())
    max_date = max(orders['Created at'].max(), returns['Reception date'].max())

    # Generate monthly and quarterly periods
    monthly_periods = pd.date_range(start=min_date, end=max_date, freq='M')
    quarterly_periods = pd.date_range(start=min_date, end=max_date, freq='Q')

    # Prepare a DataFrame to store results with static rows for each KPI
    results = pd.DataFrame({
        'KPI': ['Total Unique Customers', 'Unique B2B Customers', 'Unique B2C Customers']
    })

    # Calculate KPIs for each period and add as new columns
    for period in monthly_periods:
        month_mask = (orders['Created at'].dt.month == period.month) & (orders['Created at'].dt.year == period.year)
        orders_month = orders[month_mask]
        results[period.strftime('%Y-%m')] = [
            total_unique_customer(orders_month),
            *unique_customer_b2b_b2c(orders_month)
        ]

    for period in quarterly_periods:
        quarter_mask = (orders['Created at'].dt.to_period('Q') == period.to_period('Q'))
        orders_quarter = orders[quarter_mask]
        quarter_format = f"Q{period.quarter}-{period.year}"
        results[quarter_format] = [
            total_unique_customer(orders_quarter),
            *unique_customer_b2b_b2c(orders_quarter)
        ]

    # All time calculations
    results['All Time'] = [
        total_unique_customer(orders),
        *unique_customer_b2b_b2c(orders)
    ]

    return results


# To use the function, load your data and make sure the 'Created at'
# and 'Reception date' columns are in datetime format.
# Then you can call:
# order_data = pd.read_excel("Data/Excel/order_updated.xlsx")
# return_data = pd.read_excel("Data/Excel/return_updated.xlsx")
# results = main(order_data, return_data)
# results.to_excel("Test2.xlsx", index=False)
# print(results)

