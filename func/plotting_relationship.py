import matplotlib.pyplot as plt
import pandas as pd
import os

def scatter(column):
    print(f"Graphing {column} scatter plot")
    df = pd.DataFrame(columns=["date","price"])

    laptop_df = pd.read_csv("dfs/laptop_dfs/laptop_avg_price.csv")
    corona_df = pd.read_csv("dfs/corona_dfs/covid_19_indonesia.csv")

    laptop_df["date"] = pd.to_datetime(laptop_df["date"])
    corona_df["Date"] = pd.to_datetime(corona_df["Date"])

    laptop_df.sort_values(by="date", ascending=True, inplace=True)
    corona_df.sort_values(by="Date", ascending=True, inplace=True)

    day_list = laptop_df.date.unique()

    cases = []
    for day in day_list:
        daily_df = laptop_df[laptop_df["date"]==day].copy()
        cases_df = corona_df[corona_df["Date"]==day].copy()
        
        cases_df.drop(cases_df.columns.difference(["Date",column]), axis=1, inplace=True)
        cases_df.sort_values(by="Date", ascending=True, inplace=True)

        daily_df.reset_index(drop=True,inplace=True)
        cases_df.reset_index(drop=True,inplace=True)
        
        data = pd.DataFrame([{"date": day,
                              "price": daily_df["price"].mean()}])
        df = df.append(data)

        cases.append(cases_df[column].mean())

    df["cases"] = cases

    df.sort_values(by="date", ascending=True, inplace=True)

    df.drop(["date"], axis=1, inplace=True)
    df.drop_duplicates(subset=["price"], keep="first", inplace=True)

    x = df["cases"].tolist()
    y = df["price"].tolist()

    plt.figure(figsize=(16,9))
    plt.gca().ticklabel_format(style='plain')

    plt.scatter(x,y)

    plt.title(f"Scatter Plot Relationship between Laptop Price and {column}")
    plt.xlabel('Price')
    plt.ylabel('Cases')

    plt.subplots_adjust(left=0.08,
                        bottom=0.12,
                        right=0.96,
                        top=0.96,
                        wspace=0.2,
                        hspace=0.2)

    plt.savefig(f"graph/scatter_{column.lower().replace(',','_')}_to_prices.png")
