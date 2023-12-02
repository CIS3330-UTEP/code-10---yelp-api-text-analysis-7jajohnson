import pandas as pd
df = pd.read_csv('billionaires_orginial.csv')
df_usa = df.loc[df["location.citizenship"] == "United States"]

# print(df_usa)
df_usa = df_usa[['name','location.citizenship','wealth.worth in billions']]
print(df_usa)