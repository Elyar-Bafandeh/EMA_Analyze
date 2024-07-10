import pandas as pd

def findDistance(fileDir):
    df = pd.read_csv(fileDir, sep='\t', header=None)
    grouped = df.groupby(0)
    for key, group in grouped:
        sorted_group = group.sort_values(by=1, ascending=True)
        row_differences_starts = sorted_group[1].diff()
        row_differences_ends = sorted_group[2].diff()
        row_differences = (row_differences_starts + row_differences_ends)/2
        print(sorted_group)
        print(row_differences)
        break
findDistance("EMA_Analyze\pasDistance\pasbed.bed")
    