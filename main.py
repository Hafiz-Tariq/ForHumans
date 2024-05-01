
# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c_unique_customer.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c
from KPIs.totalOrders.totalOrders import count_total_orders
from KPIs.b2b_b2c_orders.b2b_b2c_orders import categorize_tags_and_count_orders
from DataProcessing.tagAggregatedColumn import aggregate_tags_in_dataframe
from DataProcessing.sampleColumn import mark_tag_matches
from DataProcessing.b2bColumn import mark_b2b_matches
from DataProcessing.b2cColumn import mark_b2c_matches
from KPIs.itemsSold.total_b2b_b2c2_items_sold import calculate_items_sold_by_category
from KPIs.total_b2c_b2c_Revenue.total_b2b_b2c_Revenue import calculate_revenue_by_category
from KPIs.totalReturnsItems.totalReturnItemsID import total_return_items
from KPIs.totalReturn_b2b_sample_pacakge.cleanReturnColumn import clean_order_numbers
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
from KPIs.cohorts.prcosseingDate import convert_created_at_to_date
from KPIs.cohorts.yearlyCohorts import generate_yearly_cohort_heatmaps
from KPIs.keyPaymentOptions.keyPaymentOptions import summarize_transactions
from KPIs.totalDiscount.totalDiscount import sum_discount_amount
from KPIs.newsletterSignUps.newsletterSignUp import count_accepts_marketing
from KPIs.averageTime.returnDateProcessing import process_reception_dates
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

# Returns
from KPIs.totalReturns.totalReturns import total_returns
from KPIs.totalReturnRate.returnRate import total_return_rate

# Other
import pandas as pd


def main():
    try:
        # Dataset Defined
        orders = pd.read_csv("Data/orders_export_1.csv")
        returns = pd.read_csv("Data/returns.csv")
        base_return = returns.copy()
        sku = pd.read_excel("Data/Excel/SKUs.xlsx")
        # orders = st.session_state['order']
        # returns = st.session_state['return']

        # Creating an Empty Dataframe
        columns = ["KPI's", "Calculated Values"]
        kpis = pd.DataFrame(columns=[columns[0], columns[1]])

        # Converting Tag Column to B2B and B2C and Sample + Tag Aggregated column addition
        orders = aggregate_tags_in_dataframe(orders)
        if orders is None:
            print("There is an issue processing Tag Aggregated Column.")
            exit()
        orders = mark_tag_matches(orders)
        if orders is None:
            print("There is an issue processing Sample column.")
            exit()
        orders = mark_b2b_matches(orders)
        if orders is None:
            print("There is an issue processing B2B column.")
            exit()
        orders = mark_b2c_matches(orders)
        if orders is None:
            print("There is an issue processing B2C column.")
            exit()
        # print(orders['Tags'].value_counts())
        # ************************

        # 1- Total Unique Customer
        total_customer = total_unique_customer(orders)
        if total_customer is None:
            print("There is an issue calculating Total Customer!")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Unique Customer ",
                                               columns[1]: total_customer}])], ignore_index=True)

        # print("Total Unique Customer: ", total_customer)
        # ************************

        # 2,3- Unique B2B & B2C Customers
        b2b, b2c = unique_customer_b2b_b2c(orders)
        if b2b is None or b2c is None:
            print("There is an issue calculating B2B and B2C Customers!")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Unique B2B Customer ",
                                               columns[1]: b2b}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Unique B2C Customer ",
                                               columns[1]: b2c}])], ignore_index=True)
        # print("Unique B2B Customer: ", b2b)
        # print("Unique B2C Customer: ", b2c)
        # ************************

        # 4- Total Orders
        total_orders = count_total_orders(orders)
        if total_orders is None:
            print("There is an issue calculating Total Orders!")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Orders ",
                                               columns[1]: total_orders}])], ignore_index=True)
        # print("Total Number of Orders: ", total_orders)
        # ************************

        # 5, 6- Total B2B and B2C Orders
        without_sample_orders = orders[orders['Sample'] != 1]
        b2b_order, b2c_order = categorize_tags_and_count_orders(orders)
        b2b_without_sample, b2c_without_sample = categorize_tags_and_count_orders(without_sample_orders)
        if b2b_order is None or b2c_order is None:
            print("There is an issue with B2B and B2C order count!")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Orders ",
                                               columns[1]: total_orders}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Orders ",
                                               columns[1]: total_orders}])], ignore_index=True)
        # print("B2B orders: ", b2b_order)
        # print("B2C orders: ", b2c_order)
        # print("B2B without sample orders: ", b2b_without_sample)
        # print("B2C without sample orders: ", b2c_without_sample)
        # ************************

        # 7, 8, 9- Total Items sold, Total B2B & Total B2C items Sold
        total_items, b2b_items, b2c_items = calculate_items_sold_by_category(orders)
        if total_items is None or b2b_items is None or b2c_order is None:
            print("There is an error calculating Total Item sold, Total B2B and Total B2C.")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Items Sold ",
                                               columns[1]: total_items}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total B2B Items ",
                                               columns[1]: b2b_items}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total B2C Items  ",
                                               columns[1]: b2c_items}])], ignore_index=True)
        # print("Total Items sold: ", total_items)
        # print("Total B2B items sold: ", b2b_items)
        # print("Total B2C items sold: ", b2c_items)
        # ************************

        # 10, 11, 12- Total Revenue, B2B & B2C Revenue
        total_revenue, b2b_revenue, b2c_revenue = calculate_revenue_by_category(orders)
        _, b2b_without_sample_revenue, b2c_without_sample_revenue = calculate_revenue_by_category(without_sample_orders)
        if total_revenue is None or b2b_revenue is None or b2c_revenue is None:
            print("There is an issue calculating Total, B2B and B2C Revenue.")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Revenue ",
                                               columns[1]: total_revenue}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total B2B Revenue ",
                                               columns[1]: b2b_revenue}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total B2C Revenue ",
                                               columns[1]: b2c_revenue}])], ignore_index=True)
        # print("Total Revenue($): ", int(total_revenue))
        # print("Total B2B Revenue($): ", int(b2b_revenue))
        # print("Total B2C Revenue($): ", int(b2c_revenue))
        # print("Total B2B Revenue without Sample: ", int(b2b_without_sample_revenue))
        # print("Total B2C Revenue without Sample: ", int(b2c_without_sample_revenue))
        # ************************

        # 13, 14, 15- Average Basket, Average B2B Basket & B2C Basket
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Average Basket ",
                                               columns[1]: round(total_revenue/total_orders, 2)}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Average B2B Basket ",
                                               columns[1]: round(b2b_revenue / b2b_order, 2)}])],
                         ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Average B2C Basket ",
                                               columns[1]: round(b2c_revenue / b2c_order, 2)}])],
                         ignore_index=True)
        # print("Total Basket: ", round(total_revenue / total_orders, 2))
        # print("Total B2B Basket: ", round(b2b_revenue / b2b_order, 2))
        # print("Total B2C Basket: ", round(b2c_revenue / b2c_order, 2))
        # print("Total B2B Basket without Sample: ", round(b2b_without_sample_revenue / b2b_without_sample), 2)
        # print("Total b2c Basket without Sample: ", round(b2c_without_sample_revenue / b2c_without_sample), 2)
        # ************************

        # 16- Total Returns
        returns_count = total_returns(returns)
        if returns_count is None:
            print("There is an issue calculating Total Returns!")
            exit()
        # print("Total Returns: ", returns_count)
        # ************************

        # 17- Total Return Rate
        return_rate = total_return_rate(returns_count, total_orders)
        if return_rate is None:
            print("There is an error calculating return rate!")
            exit()
        # print(f"Total return rate: {round(return_rate, 2)}%")
        # ************************

        # 18- Total returned Items
        return_items_id = total_return_items(returns)
        if return_items_id is None:
            print("There  is an error calculating total return items.")
            exit()
        # print("Total Return Items(ID): ", return_items_id)
        # ************************

        # 19- Total return B2B, Sample package
        returns = clean_order_numbers(returns)
        total_return_b2b_sample = count_matched_orders(returns, orders)
        if total_return_b2b_sample is None:
            print("Error in processing Total return B2B and Sample.")
            exit()
        # print("Total return B2B sample packages: ", total_return_b2b_sample)
        # ************************

        # 20- Average items per sample package
        avg_sample_pkg = calculate_b2b_sample_ratio(orders)
        if avg_sample_pkg is None:
            print("Error in solving Average item per sample package.")
            exit()
        # print("Average Item per Sample Package: ", avg_sample_pkg)
        # ************************

        # 21- Total Return Excluding Sample Package
        total_return_excl_sample = process_dataframes(returns, orders)
        if total_return_excl_sample is None:
            print("Issue calculating total return excluding sample.")
            exit()
        # print("Total return excluding Sample package: ", total_return_excl_sample)
        # ************************

        # 22- Total B2B returns
        total_b2b_returns = match_order_returns_b2b(returns, orders)
        if total_b2b_returns is None:
            print("Error calculating total B2B returns.")
            exit()
        # print("Total B2B returns: ", total_b2b_returns)
        # ************************

        # 23- Total Test Conversion: Total Customer B2B and Sample, Total B2B customer continue.
        b2b_sample_customer, b2b_continue_customer = analyze_customer_data(orders)
        if b2b_sample_customer is None or b2b_continue_customer is None:
            print("Issue calculating Test Conversion.")
            exit()
        # print("Total B2B and Sample True: ", b2b_sample_customer)
        # print("Total Return B2B Customer: ", b2b_continue_customer)
        # ************************

        # 24- Total B2C Return Packages
        total_b2c_return = match_order_returns(returns, orders)
        if total_b2c_return is None:
            print("Error Calculating B2C returns.")
            exit()
        # print("Total B2C return: ", total_b2c_return)
        # ************************

        # 25, 26- Return Clean(for sale items), Return Dirty(Not for sale items)
        clean, dirty = count_warehouse_values(returns)
        if clean is None or dirty is None:
            print("Error calculating returns clean and dirty.")
            exit()
        # print("Total Returns Clean(for sale items): ", clean)
        # print("Total Return Dirty(Not for sale items): ", dirty)
        # ************************

        # 27, 28- Total Reorders
        total_reorders = count_unique_customers_multiple_orders(orders)
        b2b_reorders = count_unique_customers_multiple_orders(orders[orders['B2B'] == 1])
        b2c_reorders = count_unique_customers_multiple_orders(orders[orders['B2C'] == 1])
        sample_reorders = count_unique_customers_multiple_orders(orders[orders['Sample'] == 1])
        if total_reorders is None or b2b_reorders is None or b2c_reorders is None or sample_reorders is None:
            print("Error Calculating total Reorders.")
            exit()
        # print("Total Reorders are: ", total_reorders)
        # print("Total Reorders Percentage is: ", round(((total_reorders*100)/total_customer), 2), "%")
        # print("Total B2B Reorders: ", b2b_reorders)
        # print("Total B2B Reorders Percentage is: ", round(((b2b_reorders*100)/total_customer), 2), "%")
        # print("Total B2C Reorders: ", b2c_reorders)
        # print("Total B2C Reorders Percentage is: ", round(((b2c_reorders * 100) / total_customer), 2), "%")
        # print("Total Sample Reorders: ", sample_reorders)
        # print("Total Sample Reorders Percentage is: ", round(((sample_reorders * 100) / total_customer), 2), "%")
        # ************************

        # 30, 31, 32, 33, 34- E-Text, E-Logo Revenue plus count.
        e_text, e_logo = count_sku_types(orders)
        e_text_revenue, e_logo_revenue = calculate_sku_costs(orders)
        if e_logo is None or e_text is None or e_text_revenue is None or e_logo_revenue is None:
            print("Error processing e-logo and e-text.")
            exit()
        # print("Total upselling E-Text is: ", e_text)
        # print("Total upselling E-Logo is: ", e_logo)
        # print("Total E-Text Cost: ", e_text_revenue)
        # print("Total E-Logo Cost: ", e_logo_revenue)
        # print("Total E-Text and E-Logo Cost: ", e_logo_revenue+e_text_revenue)
        # ************************

        # 35- Total Shipment Cost
        total_shipment_cost = calculate_total_shipping(orders)
        if total_shipment_cost is None:
            print('Error calculating total shipment cost.')
            exit()
        # print("Total shipment cost: ", total_shipment_cost)
        # ************************

        # 36- Total Free shipments
        free_shipments = count_free_shipments(orders)
        b2b_free_shipments = count_free_shipments(orders[orders['B2B'] == 1])
        b2c_free_shipments = count_free_shipments(orders[orders['B2C'] == 1])
        if free_shipments is None or b2b_free_shipments is None or b2c_free_shipments is None:
            print("Error calculating free shipment.")
            exit()
        # print("Total Free Shipments are: ", free_shipments)
        # print("Total B2B Free shipments are: ", b2b_free_shipments)
        # print("Total B2C free shipments are: ", b2c_free_shipments)
        # ************************

        # 37- Order with promo referral code
        promo_referral_all, promo_referral_specific = count_discount_codes(orders)
        if promo_referral_all is None or promo_referral_specific is None:
            print("Error calculating promo referral.")
            exit()
        # print("Order with All Promo/Referral: ", promo_referral_all)
        # print("Orders with Promo/Referral not contains 6-7 characters: ", promo_referral_specific)
        # ************************

        # 38- Total Lost Accounts
        if b2b_sample_customer is None or b2b_continue_customer is None:
            print("Error calculating lost accounts.")
            exit()
        # print("B2b Customer who didn't come back: ", b2b_sample_customer - b2b_continue_customer)
        # ************************

        # 40-47 - All SKU and their popularity.
        sku = update_sku_quantities(orders, sku)
        if sku is None:
            print("Error calculating SKU file.")
            exit()
        # print(sku)
        # sku.to_excel("sku_updated.xlsx", index=False)
        # ************************

        # 49- Cohorts
        orders = convert_created_at_to_date(orders)
        # generate_yearly_cohort_heatmaps(orders)
        # ************************

        # 50- Key payment options
        result = summarize_transactions(orders)
        # print("Payment Methods Transaction Counts:")
        # for method, count in result['payment_counts'].items():
        #     print(f"{method}: {count}")
        #
        # print("\nB2B Transaction Counts:")
        # for method, count in result['b2b_counts'].items():
        #     print(f"{method}: {count}")
        #
        # print("\nB2C Transaction Counts:")
        # for method, count in result['b2c_counts'].items():
        #     print(f"{method}: {count}")
        #
        # print("\nTotal Percentage Counts:")
        # for method, count in result['percentages'].items():
        #     print(f"{method}: {count}%")
        # ************************

        # 57- Total Discount
        total_discount = sum_discount_amount(orders)
        # print("Total Discount amount is: ", total_discount)
        # ************************

        # 58- Newsletter signups
        yes, no = count_accepts_marketing(orders)
        if yes is None or no is None:
            print("Error calculating newsletter signup.")
            exit()
        # print("Newsletter Signups Yes: ", yes)
        # print("Newsletter Signups No: ", no)
        # ************************

        # 59, 60- return months, how long customer have package on average
        returns = process_reception_dates(returns)
        if returns is None:
            print("Error calculating date in return data.")
            exit()
        avg_day, avg_month = calculate_time_differences(returns, orders)
        if avg_day is None or avg_month is None:
            print("Error calculating average month and days.")
            exit()
        # print("Average Days return package is: ", round(avg_day, 2))
        # print("Average Month to return package is: ", round(avg_month, 2))
        # ************************

        # 61- Rejected Shipments
        rejected, rejected_percent = analyze_rejected_shipments(base_return)
        if rejected is None or rejected_percent is None:
            print("Issue calculating rejected shipment.")
            exit()
        # print("Total Rejected Shipments are: ", rejected)
        # print("Total percentage of Rejected Shipments are: ", round(rejected_percent, 2))
        # ************************

        # 62, 63- Most products returned
        sku = update_sku_with_returns(returns, sku)
        if sku is None:
            print("Error calculating most product returned.")
            exit()
        # print(sku)
        # sku.to_excel("SKU updated.xlsx", index=False)
        # ************************

        # 74- Net Order Values
        net_value = sum_subtotal(orders)
        if net_value is None:
            print("Error in net value calculation.")
            exit()
        # print("Net total order value in EUR is:", round(net_value, 2))
        # ************************

        # 78, 79, 80 - Total Shipping in Eur, b2b and b2c
        total_shipping = sum_shipping(orders)
        b2b_shipping = sum_shipping(orders[orders['B2B'] == 1])
        b2c_shipping = sum_shipping(orders[orders['B2C'] == 1])
        if total_shipping is None or b2b_shipping is None or b2c_shipping is None:
            print("Error calculating shipping.")
            exit()
        # print("Total Shipping: ", total_shipping)
        # print("B2B shipping: ", b2b_shipping)
        # print("B2C shipping: ", b2c_shipping)
        # ************************

        # 85- Total Order Value in EUR
        total_without_sample = sum_total(orders[orders['Sample'] != 1])
        if total_without_sample is None:
            print("Error calculating Total without sample.")
            exit()
        # print("Total Order Value without Sample is: ", round(total_without_sample, 2))
        # ************************

        # 90- Which discount have been used the most
        most_codes = discount_codes(orders)
        if most_codes is None:
            print("Unable to find discount codes used most.")
            exit()
        # print("The Discount codes used most are: \n", most_codes)
        # ************************

        # 92- Average amount granted for discount
        amount = analyze_discounts_and_names(orders)
        if amount is None:
            print("Error calculating Amount granted for discount.")
            exit()
        # print("Average amount granted for discount: ", amount)
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
            print("Error calculating Counties orders.")
            exit()
        # print("Number of orders in Individual Counties: ", countries)
        # ************************

        # 117- How many orders are marketing orders
        marketing_orders = count_names_with_marketing_tags(orders)
        if marketing_orders is None:
            print("Marketing Orders calculation error.")
            exit()
        # print("Marketing Orders are : ", marketing_orders)
        # ************************

        # 118- Customer Order via Web or Shopify
        all_orders_source = source_value_counts(orders)
        b2b_order_source = source_value_counts(orders[orders['B2B'] == 1])
        b2c_order_source = source_value_counts(orders[orders['B2C'] == 1])
        if all_orders_source is None or b2b_order_source is None or b2c_order_source is None:
            print("Source Error calculation.")
            exit()
        print("Customer Order via \n", all_orders_source)
        print("B2B order Source is: \n", b2b_order_source)
        print("B2C order Source is: \n", b2c_order_source)
        # ************************

        # Creating a processed Dataframe
        # return kpis
        # ************************

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()





















