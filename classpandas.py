import pandas as pd

file_name = "big-mac-full-index.csv"

dr = pd.read_csv(file_name)

# print(dr.columns)

# print(type(dr['dollar_price']))

# print(dr['name'])

query_f = f"(iso_a3 =='ARG')"
dr_arg = dr.query(query_f)

#print(dr_arg)
print(dr_arg['dollar_price'].median()) # median price for dollar amt