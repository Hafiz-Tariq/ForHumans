import pandas as pd

data = pd.read_csv('../Data Testing/SKUS (1).csv', delimiter=';', quoting=3)
print(data)
