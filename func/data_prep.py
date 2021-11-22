import pandas as pd
import numpy as np
import csv
import os

def corona_cleaning():
    print("Preparing corona dataset")
    df = pd.read_csv("dfs/corona_dfs/covid_19_indonesia_time_series_all.csv")
    indo_df = df[df["Location"]=="Indonesia"].copy()
    indo_df.set_index("Date", inplace=True)
    indo_df.drop(indo_df.index[:213], inplace=True)
    indo_df.drop(indo_df.index[123:], inplace=True)
    indo_df.drop(indo_df.columns.difference(["Date","New Cases","New Deaths","New Recovered","New Active Cases","Total Cases","Total Deaths","Total Recovered","Total Active Cases"]), axis=1, inplace=True)

    indo_df.to_csv("dfs/corona_dfs/covid_19_indonesia.csv")

def laptop_combine():
    print("Preparing laptop dataset (1/2)")
    mtrx = [["January 2021", "January 2021"], ["November 2020", "November 2020"], ["October 2020"]]

    path = "dfs/laptop_dfs/products_dfs/"

    for dir_l in mtrx:
        for dr in dir_l:
            path+=f"{dr}/"
            
        shop_list = ["Shopee", "Tokped"]
        brand_list = ["Acer", "Asus", "Dell", "HP", "Lenovo", "MSI"]

        for shop in shop_list:
            for brand in brand_list:
                new_path = path + f"{shop}/{brand}"
                for file in os.listdir(new_path):
                    df = pd.read_csv(f"{new_path}/{file}")
                    df.drop(["location","link"], axis=1)
                    if "sold" in df.columns:
                        data_list = [[df["name"][i], df["price"][i], df["sold"][i], df["date"][i]] for i in range(len(df))]
                    else:
                        data_list = [[df["name"][i], df["price"][i], np.nan, df["date"][i]] for i in range(len(df))]
                    
                    for row in data_list:
                        if not os.path.exists(f"dfs/laptop_dfs/combine_dfs/{brand.lower()}_{file.split('_')[0]}.csv"):
                            with open(f"dfs/laptop_dfs/combine_dfs/{brand.lower()}_{file.split('_')[0]}.csv","w",encoding="UTF8",newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow(["date", "name", "price", "sold"])
                                writer.writerow([row[3], row[0], row[1], row[2]])
                        else:
                            with open(f"dfs/laptop_dfs/combine_dfs/{brand.lower()}_{file.split('_')[0]}.csv","a",encoding="UTF8",newline='') as f:
                                writer = csv.writer(f)
                                writer.writerow([row[3], row[0], row[1], row[2]])
                                f.close()
                
        path = "dfs/laptop_dfs/products_dfs/"

def laptop_cleaning():
    print("Preparing laptop dataset (2/2)")
    for file in os.listdir("dfs/laptop_dfs/combine_dfs"):
        df = pd.DataFrame(columns=["date","price"])
        brand_df = pd.read_csv(f"dfs/laptop_dfs/combine_dfs/{file}")

        brand_df["price"] = brand_df["price"].str.replace('.','', regex=True)
        brand_df["price"] = pd.to_numeric(brand_df["price"])
        brand_df["date"] = pd.to_datetime(brand_df["date"].astype(str), format='%d-%m-%Y')
        brand_df.sort_values(by="date", ascending=True, inplace=True)

        day_list = sorted(brand_df.date.unique())
        date_list = pd.date_range(day_list[0], day_list[-1])
        last_price = brand_df[brand_df["date"]==day_list[0]]["price"].mean()

        for day in date_list:
            if day in day_list:
                daily_df = brand_df[brand_df["date"]==day].copy()

                daily_df.drop(["name","sold"], axis=1, inplace=True)
                
                daily_df.reset_index(drop=True,inplace=True)
                
                data = pd.DataFrame([{"date": daily_df["date"][0],
                                      "price": daily_df["price"].mean()}])
                last_price = daily_df["price"].mean()
            else:
                data = pd.DataFrame([{"date": day,
                                      "price": last_price}])
            
            df = df.append(data)

        df.to_csv(f"dfs/laptop_dfs/series_dfs/{file}", index=False)

def combine():
    print("Combining all laptop dataset")
    df = pd.DataFrame(columns=["date","price"])
    for file in os.listdir("dfs/laptop_dfs/series_dfs"):
        prod_df = pd.read_csv(f"dfs/laptop_dfs/series_dfs/{file}")

        day_list = prod_df.date.unique()

        for day in day_list:
            daily_df = prod_df[prod_df["date"]==day].copy()
            
            data = pd.DataFrame([{"date": day,
                                  "price": daily_df["price"].mean()}])

            df = df.append(data)

    df.to_csv("dfs/laptop_dfs/laptop_avg_price.csv", index=False)


