# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c_unique_customer.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c
from KPIs.totalOrders.totalOrders import count_total_orders
from KPIs.b2b_b2c_orders.b2b_b2c_orders import categorize_tags_and_count_orders
import pandas as pd


# Dataset Defined
orders = pd.read_csv("Data/orders_export_1.csv")

# 1- Total Unique Customer
totalCustomer = total_unique_customer(orders)
if totalCustomer is None:
    print("There is an issue calculating Total Customer!")
    exit()
# print("Total Unique Customer: ", totalCustomer)
# ************************

# 2,3- Unique B2B & B2C Customers
b2b, b2c = unique_customer_b2b_b2c(orders)
if b2b is None or b2c is None:
    print("There is an issue calculating B2B and B2C Customers!")
    exit()
# print("Unique B2B: ", b2b)
# print("Unique B2C: ", b2c)
# ************************

# 4- Total Orders
totalOrders = count_total_orders(orders)
if totalOrders is None:
    print("There is an issue calculating Total Orders!")
    exit()
# print("Total Number of Orders: ", totalOrders)
# ************************

# 5- Total B2B and B2C Orders
b2b_order, b2c_order = categorize_tags_and_count_orders(orders)
if b2b_order is None or b2c_order is None:
    print("There is an issue with B2B and B2C order count!")
# print("B2B orders: ", b2b_order)
# print("B2C orders: ", b2c_order)
# ************************
