import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import os

def hr_corona():
    print("Graphing corona cases pie plot")
    df = pd.read_csv("dfs/corona_dfs/covid_19_indonesia_time_series_all.csv")

    new_df = pd.DataFrame(columns=["Location", "New Deaths"])

    for region in df.Location.unique():
        if region != "Indonesia":
            region_df = df[df["Location"]==region].copy()

            region_df.drop(region_df.columns.difference(["Date", "Location", "New Deaths"]), axis=1, inplace=True)
            
            region_df.reset_index(drop=True,inplace=True)
            start = region_df.index[region_df['Date']=="10/1/2020"][0]
            region_df.drop(region_df.index[:start], inplace=True)
            
            region_df.reset_index(drop=True,inplace=True)
            finish = region_df.index[region_df['Date']=="2/1/2021"][0]
            region_df.drop(region_df.index[finish:], inplace=True)

            region_df.drop(["Date"], axis=1, inplace=True)

            data = pd.DataFrame([{"Location": region_df["Location"][0], "New Deaths": region_df["New Deaths"].sum()}])
            new_df = new_df.append(data)

    new_df.sort_values(by="New Deaths", ascending=False, inplace=True)

    plt.figure(figsize=(16,9))
    plt.axis("equal")

    plt.pie(new_df["New Deaths"].tolist(), startangle=90)

    plt.title("Indonesia Corona Death Toll from October 2020 to January 2021")
    plt.legend(labels=[f'{l}, {s:1.1f}%' for l,s in zip(new_df["Location"].tolist(), new_df["New Deaths"].multiply(100).div(new_df["New Deaths"].sum()).tolist())])

    plt.subplots_adjust(left=0,
                        bottom=0,
                        right=0.9,
                        top=0.95,
                        wspace=0.2,
                        hspace=0.2)

    plt.savefig(f"graph/pie_chart_corona.png")

    plt.clf()

def hr_laptop():
    m = 1
    brands = ["acer","asus","dell","hp","lenovo","msi"]

    for series in brands:
        product = []
        sizes = []
        
        print(f"Graphing individual laptop brand pie plot ({m}/6)")
        m+=1
        
        for file in os.listdir("dfs/laptop_dfs/combine_dfs"):
            if file.split('_')[0]==series:
                df = pd.read_csv(f"dfs/laptop_dfs/combine_dfs/{file}")
                
                product.append(file.split('_')[1].split('.')[0][0].upper()+file.split('_')[1].split('.')[0][1:])
                sizes.append(len(df.name.unique()))
            else:
                continue
            
        plt.axis("equal")

        plt.pie(sizes, labels=product, autopct='%1.1f%%', startangle=90)
        
        plt.title(f"{series[0].upper()}{series[1:]} product series")

        plt.savefig(f"graph/pie_chart_{series}_series.png")

        plt.clf()

    amt = [0,0,0,0,0,0]

    print("Graphing laptop brand pie plot")
    
    for file in os.listdir("dfs/laptop_dfs/combine_dfs"):
        for i in range(len(brands)):
            if file.split('_')[0]==brands[i]:
                df = pd.read_csv(f"dfs/laptop_dfs/combine_dfs/{file}")
                amt[i]+=len(df.name.unique())

    plt.axis("equal")

    plt.pie(amt, labels=[brand[0].upper()+brand[1:] for brand in brands], autopct='%1.1f%%', startangle=90)

    plt.title("Amount of Laptop Products in Online Stores")

    plt.savefig(f"graph/pie_chart_laptop_products.png")
