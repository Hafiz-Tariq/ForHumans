
# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c_unique_customer.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c
from KPIs.totalOrders.totalOrders import count_total_orders
from KPIs.b2b_b2c_orders.b2b_b2c_orders import categorize_tags_and_count_orders
from KPIs.itemsSold.total_b2b_b2c2_items_sold import calculate_items_sold_by_category
from KPIs.total_b2c_b2c_Revenue.total_b2b_b2c_Revenue import calculate_revenue_by_category
from KPIs.total_b2c_b2c_Revenue.total_b2b_b2c_Revenue_without_Sample import calculate_revenue_by_category_sample_exc
from KPIs.totalReturnsItems.totalReturnItemsID import total_return_items
# from KPIs.totalReturn_b2b_sample_pacakge.cleanReturnColumn import clean_order_numbers
from KPIs.totalReturn_b2b_sample_pacakge.return_b2b_sample_pkg import count_matched_orders
from KPIs.totalAvgperSample.totalAvgItemPerSamplePkg import calculate_b2b_sample_ratio
from KPIs.totalReturnExcSample.totalReturnExcSample import process_dataframes
from KPIs.totalB2BReturns.totalB2bReturns import match_order_returns_b2b
from KPIs.totalTestConversions.totalTestConversion import analyze_customer_data
from KPIs.totalB2cReturn.totalB2cReturn import match_order_returns
from KPIs.totalReturnCleanDirty.returnCleanDrity import count_warehouse_values
from KPIs.reordersTotal.totalReorders import count_unique_customers_multiple_orders
from KPIs.eLogoEtext.upsellingElogoEtext import count_sku_types
from KPIs.eLogoEtext.revenueElogoEtext import calculate_sku_costs
from KPIs.totalShipmentCost.totalShipmentCost import calculate_total_shipping
from KPIs.freeShipments.freeShipments import count_free_shipments
from KPIs.promoReferralOrders.promoReferral import count_discount_codes
from KPIs.skuFile.skuFile import update_sku_quantities
from KPIs.cohorts.yearlyCohortsDisplay import generate_yearly_cohort_heatmaps_display
from KPIs.keyPaymentOptions.keyPaymentOptions import summarize_transactions
from KPIs.totalDiscount.totalDiscount import sum_discount_amount
from KPIs.newsletterSignUps.newsletterSignUp import count_accepts_marketing
from KPIs.averageTime.avgMonthDays import calculate_time_differences
from KPIs.rejectedShipments.rejectedShipments import analyze_rejected_shipments
from KPIs.returnedProductsSKU.returnedProductsSKU import update_sku_with_returns
from KPIs.netValue.netValue import sum_subtotal
from KPIs.shipping.shipping import sum_shipping
from KPIs.totalOrderValue.totalOrderValue import sum_total
from KPIs.discountCodes.discountCodes import discount_codes
from KPIs.discountAmount.discountAmount import analyze_discounts_and_names
from KPIs.zipCodeCounts.zipCodeCounts import classify_zip_codes
from KPIs.countryOrder.countryOrder import count_unique_names_by_country
from KPIs.marketingTags.marketingTags import count_names_with_marketing_tags
from KPIs.sourceCounts.sourceCounts import source_value_counts
from KPIs.skuDelta.skuDelta import calculate_delta

# Returns
from KPIs.totalReturns.totalReturns import total_returns
# from KPIs.totalReturnRate.returnRate import total_return_rate

# Other
# import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# Total Baskets
def calculated_kpi(df, val1, val2, name):
    total_revenue = df.loc[df['KPI'] == val1].iloc[:, 1:].values
    total_orders = df.loc[df['KPI'] == val2].iloc[:, 1:].values

    # Safely calculate the division to handle divide by zero
    total_average_basket = np.divide(total_revenue, total_orders, out=np.zeros_like(total_revenue, dtype=float),
                                     where=total_orders != 0).round(2)

    # Replace zeros where division was not possible with NaN
    total_average_basket[total_orders == 0] = np.nan

    new_row = pd.DataFrame(total_average_basket, columns=df.columns[1:])
    new_row.insert(0, 'KPI', name)
    df = pd.concat([df, new_row], ignore_index=True)
    return df


def calculated_kpi_sum(df, val1, val2, name):
    # Extract values from the DataFrame where KPI matches val1 and val2
    total_revenue = df.loc[df['KPI'] == val1].iloc[:, 1:].values
    total_orders = df.loc[df['KPI'] == val2].iloc[:, 1:].values

    # Calculate the sum of the two KPI rows
    kpi_sum = np.add(total_revenue, total_orders)

    # Create a new DataFrame row for the calculated sum
    new_row = pd.DataFrame(kpi_sum, columns=df.columns[1:])
    new_row.insert(0, 'KPI', name)

    # Append this new row to the original DataFrame
    df = pd.concat([df, new_row], ignore_index=True)
    return df


def calculated_kpi_difference(df, val1, val2, name):
    # Extract values from the DataFrame where KPI matches val1 and val2
    kpi_val1 = df.loc[df['KPI'] == val1].iloc[:, 1:].values
    kpi_val2 = df.loc[df['KPI'] == val2].iloc[:, 1:].values

    # Calculate the difference of the two KPI rows
    kpi_difference = np.subtract(kpi_val1, kpi_val2)

    # Create a new DataFrame row for the calculated difference
    new_row = pd.DataFrame(kpi_difference, columns=df.columns[1:])
    new_row.insert(0, 'KPI', name)

    # Append this new row to the original DataFrame
    df = pd.concat([df, new_row], ignore_index=True)
    return df


def main(orders, returns, base_return):
    try:
        # Determine the min and max dates across both datasets
        min_date = min(orders['Created at'].min(), returns['Reception date'].min())
        max_date = max(orders['Created at'].max(), returns['Reception date'].max())
        # ************************

        # Generate monthly and quarterly periods
        monthly_periods = pd.date_range(start=min_date, end=max_date, freq='M')
        quarterly_periods = pd.date_range(start=min_date, end=max_date, freq='Q')
        # ************************

        # Preparing Dataframe for final outcome.
        results = pd.DataFrame({
            'KPI': [
                'Total Unique Customers',
                'Unique B2B Customers',
                'Unique B2C Customers',
                'Total Orders',
                'B2B Orders',
                'B2C Orders',
                'B2B without Sample Orders',
                'B2C without Sample Orders',
                'Total Items Sold',
                'Total B2B items Sold',
                'Total B2C items Sold',
                'Total Revenue',
                'Total B2B Revenue',
                'Total B2C Revenue',
                'Total B2B Revenue without Sample',
                'Total B2C revenue without Sample',
                'Total Returns',
                'Total Returns Items(ID)',
                'Total Return B2B Sample Packages',
                'Average Items per Sample Package',
                'Total return Excluding Sample Package',
                'Total B2B return',
                'Total Test Conversion: (B2B and Sample True Customer)',
                'Total Test Conversion: (B2B True Customer)',
                'Total B2C Return',
                'Total Return Clean: For sale items',
                'Total Return Dirty: Not for sale items',
                "Total Reorders",
                'Total B2B Reorders',
                "Total B2C Reorders",
                "Total Sample Reorders",
                "Total Upselling E-Text Count",
                "Total Upselling E-Logo Count",
                'Total E-Text Cost',
                "Total E-Logo Cost",
                'Total Shipment Cost',
                'Total Free Shipment counts',
                'Total B2B free shipments count',
                'Total B2C free shipment counts',
                'Promo Referral Code(All)',
                "Promo Referral Code(6-7 Digit Excluded)",
                'Total Discount',
                'Newsletter Signups: Yes',
                'Newsletter Signups: No',
                'Average Days to return package',
                'Average months to return package',
                'Total Rejected Shipments',
                'Total Percentage of Rejected Shipments',
                'Net Total Order Value in EUR',
                'Total Shipping',
                'B2B Shipping',
                'B2C Shipping',
                'Total Order Value without Sample(EUR)',
                'Average Amount granted for discount',
                'Marketing Orders',
                'All Payment Method: custom',
                'All Payment Method: Paypal Express Checkout',
                'All Payment Method: Shopify Payments',
                'B2B Payment Method: custom',
                'B2B Payment Method: Paypal Express Checkout',
                'B2B Payment Method: Shopify Payments',
                'B2C Payment Method: custom',
                'B2C Payment Method: Paypal Express Checkout',
                'B2C Payment Method: Shopify Payments',
                'Total Percentage Payment Method: custom',
                'Total Percentage Payment Method: Paypal Express Checkout',
                'Total Percentage Payment Method: Shopify Payments'
            ]
        })

        # Calculate KPIs for each period and add as new columns
        for period in monthly_periods:
            month_mask = (orders['Created at'].dt.month == period.month) & (
                        orders['Created at'].dt.year == period.year)
            month_mask_return = (returns['Reception date'].dt.month == period.month) & (
                        returns['Reception date'].dt.year == period.year)
            month_mask_base_return = (base_return['Reception date'].dt.month == period.month) & (
                        base_return['Reception date'].dt.year == period.year)
            orders_month = orders[month_mask]
            return_month = returns[month_mask_return]
            base_return_month = base_return[month_mask_base_return]

            results[period.strftime('%Y-%m')] = [
                total_unique_customer(orders_month),
                *unique_customer_b2b_b2c(orders_month),
                count_total_orders(orders_month),
                *categorize_tags_and_count_orders(orders_month),
                *categorize_tags_and_count_orders(orders_month[orders_month['Sample'] != 1]),
                *calculate_items_sold_by_category(orders_month),
                *calculate_revenue_by_category(orders_month),
                *calculate_revenue_by_category_sample_exc(orders_month[orders_month['Sample'] != 1]),
                total_returns(return_month),
                total_return_items(return_month),
                count_matched_orders(return_month, orders_month),
                calculate_b2b_sample_ratio(orders_month),
                process_dataframes(return_month, orders_month),
                match_order_returns_b2b(return_month, orders_month),
                *analyze_customer_data(orders_month),
                match_order_returns(return_month, orders_month),
                *count_warehouse_values(return_month),
                count_unique_customers_multiple_orders(orders_month),
                count_unique_customers_multiple_orders(orders_month[orders_month['B2B'] == 1]),
                count_unique_customers_multiple_orders(orders_month[orders_month['B2C'] == 1]),
                count_unique_customers_multiple_orders(orders_month[orders_month['Sample'] == 1]),
                *count_sku_types(orders_month),
                *calculate_sku_costs(orders_month),
                calculate_total_shipping(orders_month),
                count_free_shipments(orders_month),
                count_free_shipments(orders_month[orders_month['B2B'] == 1]),
                count_free_shipments(orders_month[orders_month['B2C'] == 1]),
                *count_discount_codes(orders_month),
                sum_discount_amount(orders_month),
                *count_accepts_marketing(orders_month),
                *calculate_time_differences(return_month, orders_month),
                *analyze_rejected_shipments(base_return_month),
                sum_subtotal(orders_month),
                sum_shipping(orders_month),
                sum_shipping(orders_month[orders_month['B2B'] == 1]),
                sum_shipping(orders_month[orders_month['B2C'] == 1]),
                sum_total(orders_month[orders_month['Sample'] != 1]),
                analyze_discounts_and_names(orders_month),
                count_names_with_marketing_tags(orders_month),
                *summarize_transactions(orders_month)
            ]

        for period in quarterly_periods:
            quarter_mask = (orders['Created at'].dt.to_period('Q') == period.to_period('Q'))
            quarter_mask_return = (returns['Reception date'].dt.to_period('Q') == period.to_period('Q'))
            quarter_mask_return_base = (base_return['Reception date'].dt.to_period('Q') == period.to_period('Q'))
            orders_quarter = orders[quarter_mask]
            return_quarter = returns[quarter_mask_return]
            return_quarter_base = base_return[quarter_mask_return_base]
            quarter_format = f"Q{period.quarter}-{period.year}"
            results[quarter_format] = [
                total_unique_customer(orders_quarter),
                *unique_customer_b2b_b2c(orders_quarter),
                count_total_orders(orders_quarter),
                *categorize_tags_and_count_orders(orders_quarter),
                *categorize_tags_and_count_orders(orders_quarter[orders_quarter['Sample'] != 1]),
                *calculate_items_sold_by_category(orders_quarter),
                *calculate_revenue_by_category(orders_quarter),
                *calculate_revenue_by_category_sample_exc(orders_quarter[orders_quarter['Sample'] != 1]),
                total_returns(return_quarter),
                total_return_items(return_quarter),
                count_matched_orders(return_quarter, orders_quarter),
                calculate_b2b_sample_ratio(orders_quarter),
                process_dataframes(orders_quarter, return_quarter),
                match_order_returns_b2b(return_quarter, orders_quarter),
                *analyze_customer_data(orders_quarter),
                match_order_returns(return_quarter, orders_quarter),
                *count_warehouse_values(return_quarter),
                count_unique_customers_multiple_orders(orders_quarter),
                count_unique_customers_multiple_orders(orders_quarter[orders_quarter['B2B'] == 1]),
                count_unique_customers_multiple_orders(orders_quarter[orders_quarter['B2C'] == 1]),
                count_unique_customers_multiple_orders(orders_quarter[orders_quarter['Sample'] == 1]),
                *count_sku_types(orders_quarter),
                *calculate_sku_costs(orders_quarter),
                calculate_total_shipping(orders_quarter),
                count_free_shipments(orders_quarter),
                count_free_shipments(orders_quarter[orders_quarter['B2B'] == 1]),
                count_free_shipments(orders_quarter[orders_quarter['B2C'] == 1]),
                *count_discount_codes(orders_quarter),
                sum_discount_amount(orders_quarter),
                *count_accepts_marketing(orders_quarter),
                *calculate_time_differences(return_quarter, orders_quarter),
                *analyze_rejected_shipments(return_quarter_base),
                sum_subtotal(orders_quarter),
                sum_shipping(orders_quarter),
                sum_shipping(orders_quarter[orders_quarter['B2B'] == 1]),
                sum_shipping(orders_quarter[orders_quarter['B2C'] == 1]),
                sum_total(orders_quarter[orders_quarter['Sample'] != 1]),
                analyze_discounts_and_names(orders_quarter),
                count_names_with_marketing_tags(orders_quarter),
                *summarize_transactions(orders_quarter)
            ]

        # All time calculations
        results['All Time'] = [
            total_unique_customer(orders),
            *unique_customer_b2b_b2c(orders),
            count_total_orders(orders),
            *categorize_tags_and_count_orders(orders),
            *categorize_tags_and_count_orders(orders[orders['Sample'] != 1]),
            *calculate_items_sold_by_category(orders),
            *calculate_revenue_by_category(orders),
            *calculate_revenue_by_category_sample_exc(orders[orders['Sample'] != 1]),
            total_returns(returns),
            total_return_items(returns),
            count_matched_orders(returns, orders),
            calculate_b2b_sample_ratio(orders),
            process_dataframes(returns, orders),
            match_order_returns_b2b(returns, orders),
            *analyze_customer_data(orders),
            match_order_returns(returns, orders),
            *count_warehouse_values(returns),
            count_unique_customers_multiple_orders(orders),
            count_unique_customers_multiple_orders(orders[orders['B2B'] == 1]),
            count_unique_customers_multiple_orders(orders[orders['B2C'] == 1]),
            count_unique_customers_multiple_orders(orders[orders['Sample'] == 1]),
            *count_sku_types(orders),
            *calculate_sku_costs(orders),
            calculate_total_shipping(orders),
            count_free_shipments(orders),
            count_free_shipments(orders[orders['B2B'] == 1]),
            count_free_shipments(orders[orders['B2C'] == 1]),
            *count_discount_codes(orders),
            sum_discount_amount(orders),
            *count_accepts_marketing(orders),
            *calculate_time_differences(returns, orders),
            *analyze_rejected_shipments(base_return),
            sum_subtotal(orders),
            sum_shipping(orders),
            sum_shipping(orders[orders['B2B'] == 1]),
            sum_shipping(orders[orders['B2C'] == 1]),
            sum_total(orders[orders['Sample'] != 1]),
            analyze_discounts_and_names(orders),
            count_names_with_marketing_tags(orders),
            *summarize_transactions(orders)
        ]

        results = calculated_kpi(results, "Total Revenue", "Total Orders", "Average Basket")
        results = calculated_kpi(results, "Total B2B Revenue", "B2B Orders", "Average B2B Basket")
        results = calculated_kpi(results, "Total B2C Revenue", "B2C Orders", "Average B2C Basket")
        results = calculated_kpi(results, "Total B2B Revenue without Sample", "B2B without Sample Orders",
                                 "Average B2B Basket without Sample")
        results = calculated_kpi(results, 'Total B2C revenue without Sample', "B2C without Sample Orders",
                                 "Average B2C Basket without Sample")

        results = calculated_kpi(results, "Total Returns", "Total Orders", "Total Return Rate")
        results.loc[results['KPI'] == 'Total Return Rate', results.columns[1:]] *= 100

        results = calculated_kpi(results, "Total Reorders", "Total Unique Customers",
                                 "Total Reorder Percentage(%)")
        results.loc[results['KPI'] == 'Total Reorder Percentage(%)', results.columns[1:]] *= 100

        results = calculated_kpi(results, "Total B2B Reorders", "Total Unique Customers",
                                 "Total B2B Reorder Percentage(%)")
        results.loc[results['KPI'] == 'Total B2B Reorder Percentage(%)', results.columns[1:]] *= 100

        results = calculated_kpi(results, "Total B2C Reorders", "Total Unique Customers",
                                 "Total B2C Reorder Percentage(%)")
        results.loc[results['KPI'] == 'Total B2C Reorder Percentage(%)', results.columns[1:]] *= 100

        results = calculated_kpi(results, "Total Sample Reorders", "Total Unique Customers",
                                 "Total Sample Reorder Percentage(%)")
        results.loc[results['KPI'] == 'Total Sample Reorder Percentage(%)', results.columns[1:]] *= 100

        results = calculated_kpi_sum(results, "Total E-Text Cost", "Total E-Logo Cost",
                                     "Total of E-Text and E-Logo Cost")

        results = calculated_kpi_difference(results, "Total Test Conversion: (B2B and Sample True Customer)",
                                            "Total Test Conversion: (B2B True Customer)",
                                            "Total Lost Account: B2B Customer who didn't Come back")
        # *****************************--------------------*********************************

        # 90- Which discount have been used the most
        most_codes = discount_codes(orders)
        if most_codes is None:
            print("Unable to find discount codes used most.")
            exit()
        # print("The Discount codes used most are: \n", most_codes)
        # ************************

        # 109- Which districts work the best
        districts = classify_zip_codes(orders)
        if districts is None:
            print("Error calculating Districts.")
            exit()
        # print("Districts working the best are: \n", districts)
        # ************************

        # 110- Number of orders in individual countries
        countries = count_unique_names_by_country(orders)
        if countries is None:
            print("Error calculating Countries orders.")
            exit()
        # print("Number of orders in Individual Countries: ", countries)
        # ************************

        # 118- Customer Order via Web or Shopify
        all_orders_source = source_value_counts(orders, "all")
        b2b_order_source = source_value_counts(orders[orders['B2B'] == 1], "b2b")
        b2c_order_source = source_value_counts(orders[orders['B2C'] == 1], "b2c")
        if all_orders_source is None or b2b_order_source is None or b2c_order_source is None:
            print("Source Error calculation.")
            exit()
        # print("Customer Order via \n", all_orders_source)
        # print("B2B order Source is: \n", b2b_order_source)
        # print("B2C order Source is: \n", b2c_order_source)
        # ************************

        # Flatten each DataFrame and concatenate into a single series
        dataframes = [all_orders_source, b2b_order_source, b2c_order_source, countries, districts, most_codes]

        all_values = pd.concat([pd.Series(df.values.flatten()) for df in dataframes])

        if len(all_values) % 2 != 0:
            all_values = all_values[:-1]
        reshaped_df = pd.DataFrame(all_values.values.reshape(-1, 2), columns=['KPI', 'Counts'])

        # Creating a processed Dataframe
        return results, reshaped_df
        # ************************

    except Exception as e:
        print(e)


def sku_update(orders, returns, sku):
    sku = update_sku_quantities(orders, sku)
    if sku is None:
        print("Error calculating SKU file.")
        exit()

    sku = update_sku_with_returns(returns, sku)
    if sku is None:
        print("Error calculating most product returned.")
        exit()

    sku = calculate_delta(sku)
    if sku is None:
        print("Error Calculating SKU.")

    return sku


def cohorts(orders):
    heatmaps = generate_yearly_cohort_heatmaps_display(orders)
    return heatmaps


# if __name__ == '__main__':
    # Dataset Defined
    # orders = pd.read_csv("Data/orders.csv")
    # returns = pd.read_csv("Data/returns.csv")
    # sku = pd.read_excel("Data/Excel/SKUs.xlsx")

    # heatmaps = cohorts(orders)
    # for key, fig in heatmaps.items():
    #     fig.show()
    # # plt.show()
    # sku = sku_update(orders, returns, sku)
    # results = main(orders, returns, base_return)
