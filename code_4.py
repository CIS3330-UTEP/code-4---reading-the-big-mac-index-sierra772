import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    query = f"(date >= '{year}-01-01'and date <= '{int(year)+1}-12-31' and iso_a3 == '{country_code.upper()}')"
    df_yr = df.query(query)
    mean_price = df_yr['dollar_price'].mean()
    return round(mean_price,2)

def get_big_mac_price_by_country(country_code):
    query = f"(iso_a3 == '{country_code.upper()}')"
    df_country = df.query(query)
    mean_d_price = df_country['dollar_price'].mean()
    return round(mean_d_price,2)

def get_the_cheapest_big_mac_price_by_year(year):
    yr = f"(date >= '{year}-01-01'and date <= '{year}-12-31')"
    df_min = df.query(yr)
    query = df_min['dollar_price'].idxmin()
    min = round(df_min.loc[query]['dollar_price'],2)
    s = df_min.loc[query]
    abv = s['name']
    country_code = s['iso_a3']
    return f"{abv}({country_code}): ${min}"


def get_the_most_expensive_big_mac_price_by_year(year):
    yr = f"(date >= '{year}-01-01' and date <='{year}-12-31')"
    df_max = df.query(yr)
    query = df_max['dollar_price'].idxmax()
    max = round(df_max.loc[query]['dollar_price'],2)
    x = df_max.loc[query]
    abv = x['name']
    country_code = x['iso_a3']
    return f"{abv}({country_code}): ${max}"


if __name__ == "__main__":
    
    mean_price_country = get_big_mac_price_by_year(2010,"jpn")
    print(mean_price_country)

    country_price = get_big_mac_price_by_country("usa")
    print(country_price)

    cheapest_big_mac = get_the_cheapest_big_mac_price_by_year(2012)
    print(cheapest_big_mac)

    expensive_big_mac = get_the_most_expensive_big_mac_price_by_year(2005)
    print(expensive_big_mac)

