import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import os

def case_to_time(column):
    print(f"Graphing {column} to time")
    df = pd.read_csv(f"dfs/corona_dfs/covid_19_indonesia.csv")

    df.drop(df.columns.difference(["Date", column]), axis=1, inplace=True)

    df["Date"]=pd.to_datetime(df["Date"].astype(str), format='%m/%d/%Y')

    x = df["Date"].tolist()
    y = df[column].tolist()

    plt.figure(figsize=(16,9))
    plt.axis((x[0],x[-1],min(y)-(min(y)/1000),max(y)+(min(y)/1000)))
    plt.xticks(x[::10],  rotation=0)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))

    if y[-1]>y[0]: plt.plot(x,y,color='red')
    else: plt.plot(x,y,color='green')

    plt.title(f"Covid-19 {column}")
    plt.xlabel('Date')
    plt.ylabel('Cases')

    plt.subplots_adjust(left=0.06,
                        bottom=0.12,
                        right=0.96,
                        top=0.96,
                        wspace=0.2,
                        hspace=0.2)

    plt.savefig(f"graph/line_chart_corona_{column.lower().replace(' ','_')}.png")

def price_to_time():
    m=1
    for file in os.listdir("dfs/laptop_dfs/series_dfs"):
        print(f"Graphing individual laptop to time ({m}/18)")
        m+=1
        
        df = pd.read_csv(f"dfs/laptop_dfs/series_dfs/{file}")

        df["date"] = pd.to_datetime(df["date"])
        df.sort_values(by="date", ascending=True, inplace=True)

        x = df["date"].tolist()
        y = df["price"].tolist()

        plt.figure(figsize=(16,9))
        plt.axis((x[0],x[-1],min(y)-(min(y)/1000),max(y)+(min(y)/1000)))
        plt.xticks(x[::10],rotation=0)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d %b %Y'))

        if y[-1]>y[0]: plt.plot(x,y,color='red')
        else: plt.plot(x,y,color='green')

        if len(file.split('_')[0])>3:
            plt.title(f"{file.split('_')[0][0].upper()}{file.split('_')[0][1:]} {file.split('_')[1].split('.')[0][0].upper()}{file.split('_')[1].split('.')[0][1:]} Laptop Price")
        else:
            plt.title(f"{file.split('_')[0].upper()} {file.split('_')[1].split('.')[0][0].upper()}{file.split('_')[1].split('.')[0][1:]} Laptop Price")
        plt.xlabel('Date')
        plt.ylabel('Price')

        plt.subplots_adjust(left=0.06,
                            bottom=0.12,
                            right=0.96,
                            top=0.96,
                            wspace=0.2,
                            hspace=0.2)

        plt.savefig(f"graph/line_chart_{file.split('_')[1].split('.')[0]}_price.png")

        plt.clf()
