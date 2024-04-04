# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c_unique_customer.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c
from KPIs.totalOrders.totalOrders import count_total_orders
from KPIs.b2b_b2c_orders.b2b_b2c_orders import categorize_tags_and_count_orders
from DataProcessing.b2b_b2c_processing import convert_tags_in_dataframe
from KPIs.itemsSold.total_b2b_b2c2_items_sold import calculate_items_sold_by_category
from KPIs.total_b2c_b2c_Revenue.total_b2b_b2c_Revenue import calculate_revenue_by_category
import pandas as pd
import streamlit as st


def main(orders, returns):
    try:
        # Dataset Defined
        # orders = pd.read_csv("Data/orders_export_1.csv")
        # returns = pd.read_csv("Data/returns.csv")
        # orders = st.session_state['order']
        # returns = st.session_state['return']

        # Creating an Empty Dataframe
        columns = ["KPI's", "Calculated Values"]
        kpis = pd.DataFrame(columns=[columns[0], columns[1]])

        # Converting Tag Column to B2B and B2C and Sample
        orders = convert_tags_in_dataframe(orders)
        if orders is None:
            print("There is an issue processing B2b, Sample and B2C")
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
        b2b_order, b2c_order = categorize_tags_and_count_orders(orders)
        if b2b_order is None or b2c_order is None:
            print("There is an issue with B2B and B2C order count!")
            exit()
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Orders ",
                                               columns[1]: total_orders}])], ignore_index=True)
        kpis = pd.concat([kpis, pd.DataFrame([{columns[0]: "Total Orders ",
                                               columns[1]: total_orders}])], ignore_index=True)
        # print("B2B orders: ", b2b_order)
        # print("B2C orders: ", b2c_order)
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
        # ************************

        # Creating a processed Dataframe
        return kpis
        # ************************

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()





















