import pandas as pd
def get_full_name(row):
    # print(row
    full_name = row['name'].split()
    new_data = {'f_name':full_name[0], "l_name":" ".join(full_name[1:])}
    return pd.Series(new_data)
df = pd.read_csv("billionaires_orginial.csv")
df_usa = df.loc[df['location.citizenship'] == "United States"]
df_usa[['f_name','l_name']] = df_usa.apply(get_full_name,axis=1)
print(df_usa[['f_name','l_name']])


# # for item in df_usa['name']:
# #     print(item)
# for index, row in df_usa.iterrows():
#     full_name  = row['name'].split()
#     # print(full_name[0])
#     # # print(full_name[1:])
#     # print(' '.join(full_name[1:]))
#     df_usa.at[index,'f_name'] = full_name[0]
#     df_usa.at[index,'l_name'] = ' '.join(full_name[1:])
# print(df_usa[['name','f_name','l_name']])

