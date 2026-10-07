import pandas as pd

variable = input("Enter a CSV Filename :")
df = pd.read_csv(variable)
print(df)
print(df.shape)
df.info()

print(df.head(5))
print(df.tail(5))

total_revenue = df["Revenue"].sum()
print(total_revenue)

highest_order_index = df["Revenue"].idxmax()
print(highest_order_index)
print(df.loc[highest_order_index])

df["Highest_Revenue"] = df["Revenue"] == df["Revenue"].max()
df.to_csv("sales_analyzed.csv", index=False)

