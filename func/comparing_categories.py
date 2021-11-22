from matplotlib import ticker as mticker
import matplotlib.pyplot as plt
import pandas as pd
import os

def laptop_price():
    print("Graphing laptop price histogram")
    
    df = pd.DataFrame(columns=["price"])

    for file in os.listdir("dfs/laptop_dfs/combine_dfs"):
        new_df = pd.read_csv(f"dfs/laptop_dfs/combine_dfs/{file}")
        
        new_df.drop_duplicates(subset=["name"], keep="last", inplace=True)
        new_df.drop(["date", "name", "sold"], axis=1, inplace=True)

        new_df["price"] = new_df["price"].str.replace('.','', regex=True)
        
        new_df["price"] = pd.to_numeric(new_df["price"])

        df = pd.concat([df, new_df])

    df.sort_values(by=["price"],inplace=True)

    plt.figure(figsize=(16,9))

    plt.hist(df["price"],bins=range(1200000,96750001,7450000),rwidth=0.9)

    plt.yscale("log")

    plt.xticks(ticks=range(1200000,96750001,7450000),
               labels=["1.200.000","8.650.000","16.100.000","23.550.000","31.000.000","38.400.000",
                       "45.900.000","53.350.000","60.800.000","68.250.000","75.700.000","83.150.000","96.750.000"],
               rotation = 0)
    plt.yticks(ticks = [1,10,100,1000,10000])
    plt.gca().yaxis.set_major_formatter(mticker.ScalarFormatter())
    plt.minorticks_off()

    plt.axis((0,df["price"].max()+2*df["price"].min(),1,20000))

    plt.title("Laptop Price from October 2020 to January 2021")
    plt.xlabel("Price (IDR)")
    plt.ylabel("Frequency")

    plt.subplots_adjust(left=0.06,
                            bottom=0.12,
                            right=0.98,
                            top=0.96,
                            wspace=0.2,
                            hspace=0.2)

    plt.savefig("graph/histogram_laptop_price.png")

def laptop_sold():
    print("Graphing laptop sold histogram")
    
    df = pd.DataFrame(columns=["sold"])

    for file in os.listdir("dfs/laptop_dfs/combine_dfs"):
        new_df = pd.read_csv(f"dfs/laptop_dfs/combine_dfs/{file}")
        
        new_df.drop_duplicates(subset=["name"], keep="last", inplace=True)
        new_df.drop(["date", "name", "price"], axis=1, inplace=True)

        new_df["sold"] = new_df["sold"].replace(',','', regex=True)
        new_df["sold"] = new_df["sold"].replace('RB','', regex=True)
        new_df["sold"] = new_df["sold"].replace(' rb','', regex=True)
        
        new_df["sold"] = pd.to_numeric(new_df["sold"])

        df = pd.concat([df, new_df])

    df.sort_values(by=["sold"],inplace=True)

    plt.figure(figsize=(16,9))

    plt.hist(df["sold"],bins=range(0,1001,100),rwidth=0.9)

    plt.yscale("log")

    plt.xticks(ticks=range(0,1001,100),
               labels=["0","100","200","300","400","500",
                       "600","700","800","900","1000"],
               rotation=0)
    plt.yticks(ticks = [1,10,100,1000,10000])
    plt.gca().yaxis.set_major_formatter(mticker.ScalarFormatter())
    plt.minorticks_off()

    plt.axis((0,1000,1,20000))

    plt.title("Laptop Sold from October 2020 to January 2021")
    plt.xlabel("Amount")
    plt.ylabel("Frequency")

    plt.subplots_adjust(left=0.06,
                            bottom=0.12,
                            right=0.98,
                            top=0.96,
                            wspace=0.2,
                            hspace=0.2)

    plt.savefig("graph/histogram_laptop_sold.png")

