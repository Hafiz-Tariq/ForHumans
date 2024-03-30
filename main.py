# Importing all the libraries
from KPIs.Total_Unique_Customers.totaUniqueCustomers import total_unique_customer
import pandas as pd


# Dataset Defined
orders = pd.read_csv("Data/orders_export_1.csv")

# 1- Total Unique Customer
totalCustomer = total_unique_customer(orders)
if totalCustomer is None:
    print("There is an issue calculating Total Customer!")
    exit()
print("Total Unique Customer: ", totalCustomer)
# ************************
