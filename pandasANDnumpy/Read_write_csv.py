
import pandas as pd

df = pd.read_csv("stock_data.csv")
print(df)
print("\n")


#to skip header
print("skip header \n")
df = pd.read_csv("stock_data.csv", skiprows=1)
print(df)

# to read only 2 rows
df = pd.read_csv("stock_data.csv",  nrows=2)

print("only two ros from file \n")
print(df)


# to replace na values of multiple cols

df = pd.read_csv("stock_data.csv",  na_values={
        'eps': ['not available'],
        'revenue': [-1],
        'price': ['not available','n.a.',0],
        'people': ['not available','n.a.']
    })

print("replacing na values :\n")
print(df)

#create new csv without header and index
df.to_csv("new.csv", index=False,header=False)

