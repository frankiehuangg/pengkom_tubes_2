import func.data_prep as dp
import func.comparing_categories as cc
import func.sot as sot
import func.hierarchy as hr
import func.plotting_relationship as pr
import func.corr as corr
import os

def make_folder(path):
    print(f"Making a folder in {path}")
    if not os.path.exists(path):
        os.makedirs(path)

make_folder("graph")

dp.corona_cleaning()

make_folder("dfs/laptop_dfs/combine_dfs")
dp.laptop_combine()

make_folder("dfs/laptop_dfs/series_dfs")
dp.laptop_cleaning()

cc.laptop_price()
cc.laptop_sold()

sot.case_to_time("New Cases")
sot.case_to_time("New Deaths")
sot.case_to_time("New Recovered")
sot.case_to_time("New Active Cases")
sot.case_to_time("Total Cases")
sot.case_to_time("Total Deaths")
sot.case_to_time("Total Recovered")
sot.case_to_time("Total Active Cases")
sot.price_to_time()

dp.combine()

hr.hr_corona()
hr.hr_laptop()

pr.scatter("New Cases")
pr.scatter("New Deaths")
pr.scatter("New Recovered")
pr.scatter("New Active Cases")
pr.scatter("Total Cases")
pr.scatter("Total Deaths")
pr.scatter("Total Recovered")
pr.scatter("Total Active Cases")

corr.corr()
