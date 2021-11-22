import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def corr():
    print("Graphing correlation table")
    df = pd.read_csv("dfs/laptop_dfs/laptop_avg_price.csv")
    crn_df = pd.read_csv("dfs/corona_dfs/covid_19_indonesia.csv")

    for col in crn_df.columns:
        df[col] = crn_df[col]

    df.fillna(-99999)
    df.drop(["date"], axis=1, inplace=True)
    df.drop(["Date"], axis=1, inplace=True)

    alp = df.columns.tolist()

    df_corr = df.corr()

    data = df_corr.values
    fig = plt.figure(figsize=(16,9))
    ax = fig.add_subplot(111)

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)

    ax.set_xticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1])+0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    col_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    plt.title("Heat map of all columns")
    heatmap.set_clim(-1,1)

    plt.subplots_adjust(left=0.12,
                        bottom=0.05,
                        right=1,
                        top=0.92,
                        wspace=0.2,
                        hspace=0.2)

    plt.tight_layout()
    plt.savefig(f"graph/heatmap.png")
