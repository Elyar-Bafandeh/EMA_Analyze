import pandas as pd

def findDistance(fileDir):
    df = pd.read_csv(fileDir, sep='\t', header=None)
    grouped = df.groupby([0 , 5])
    distance_dict = {}
    for key, group in grouped:
        sorted_group = group.sort_values(by=1, ascending=True)
        row_differences_starts = sorted_group[1].diff()
        row_differences_ends = sorted_group[2].diff()
        row_differences = (row_differences_starts + row_differences_ends)/2
        row_differences_ranged = findRange(row_differences , 30)
        for distanceRange in row_differences_ranged:
            try:
                distance_dict[distanceRange] += 1
            except KeyError:
                distance_dict[distanceRange] = 1
        
    return distance_dict
        

def findRange(series , n):
    new_series = series.map(lambda x:((x//n)*n , ((x//n )+1)*n))
    return new_series

