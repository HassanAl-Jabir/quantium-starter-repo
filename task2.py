import pandas as pd

files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

dataframes = [pd.read_csv(file) for file in files]
df = pd.concat(dataframes, ignore_index=True)

df = df[df["product"] == "pink morsel"].copy()

df["price"] = df["price"].replace("[$,]", "", regex=True).astype(float)

df["sales"] = df["quantity"] * df["price"]

output_df = df[["sales", "date", "region"]]

output_df.to_csv("formatted_sales_data.csv", index=False)

print("formatted_sales_data.csv has been created successfully.")