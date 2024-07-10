import matplotlib.pyplot as plt
from findDistance import findDistance
def repeatsHistogram(data):
    repeats = list(map(lambda x:x[0] , data.keys()))
    #print(repeats)
    repeatCounts = list(data.values())

    plt.bar(repeats, repeatCounts , width= 30)
    #plt.yscale('log')
    plt.xlim(0 , 3000)

    plt.xlabel('Repeats')
    plt.ylabel('Repeat Frequencies')
    plt.title('Histogram of Repeats')
    plt.show()

def main():
    data = findDistance("EMA_Analyze\pasDistance\pasbed.bed")
    
    repeatsHistogram(data)

main()

