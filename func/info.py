import pandas as pd
import os

def corona_stat():
    df = pd.read_csv("dfs/corona_dfs/covid_19_indonesia.csv")

    print("Beberapa data baris pertama")
    print(df.head())

    col_list = df.columns.tolist()[1:]
        
    for col in col_list:
        print(f"Beberapa data terkecil pada kolom {col}")
        print(df.sort_values(by=[col], ascending=True).head())
        
        print(f"Beberapa data terbesar pada kolom {col}")
        print(df.sort_values(by=[col], ascending=False).head())

    print(f"Beberapa data random")
    print(df.sample(5))

    col_list = df.columns.tolist()[1:]
    pct_list = [0.1, 0.25, 0.5, 0.75, 0.9]

    for col in col_list:
        print(f"Nilai rata-rata pada kolom {col}: {df[col].mean()}")
        print(f"Nilai standar deviasi pada kolom {col}: {df[col].std()}")
        for pct in pct_list:
            print(f"Nilai percentile {pct*100}% pada kolom {col}: {df[col].quantile(pct)}")
        print(f"Nilai maksimum pada kolom {col}: {df[col].max()}")
        print(f"Nilai minimum pada kolom {col}: {df[col].min()}")    

def laptop_stat():
    for file in os.listdir("dfs/laptop_dfs/series_dfs"):
        df = pd.read_csv(f"dfs/laptop_dfs/series_dfs/{file}")

        print(f"Data pada file {file}\n")

        print("Beberapa data baris pertama")
        print(df.head())

        print(f"Beberapa data terkecil pada kolom price")
        print(df.sort_values(by=["price"], ascending=True).head())
        
        print(f"Beberapa data terbesar pada kolom price")
        print(df.sort_values(by=["price"], ascending=False).head())

        print(f"Beberapa data random")
        print(df.sample(5))

        print("===========================")

    pct_list = [0.1, 0.25, 0.5, 0.75, 0.9]

    file_list = ["msi_prestige.csv", "acer_nitro.csv", "acer_aspire.csv"]

    for file in os.listdir("dfs/laptop_dfs/series_dfs"):
        df = pd.read_csv(f"dfs/laptop_dfs/series_dfs/{file}")
        
        print(f"Pada file {file}: ")
        print(f"Nilai rata-rata pada kolom price: {df['price'].mean()}")
        print(f"Nilai standar deviasi pada kolom price: {df['price'].std()}")
        for pct in pct_list:
            print(f"Nilai percentile {pct*100}% pada kolom price: {df['price'].quantile(pct)}")
        print(f"Nilai maksimum pada kolom price: {df['price'].max()}")
        print(f"Nilai minimum pada kolom price: {df['price'].min()}")
        print("===============================")
