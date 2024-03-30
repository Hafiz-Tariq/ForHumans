# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
from KPIs.b2b_b2c.uniqueCustomer_b2b_b2c import unique_customer_b2b_b2c
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
