import sys
import pandas as pd
from matplotlib import pyplot as plt


def analyze_day(data, header=None):
    group = 1
    x_col = 0
    
    df = pd.DataFrame(data)

    if header:
        df.columns = header
        group = header[1]
        x_col = header[0]

    for i, _df in df.groupby(group):
        print(i)
# TODO left off here... plot the groups
#        plt.scatter(_df[_df[group] ==i], _df[x_col])
#    plt.savefig('test.png')


def process_csv(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()

    data = list()
    header = None

    for l in lines:
        if 'week' in l.lower():
            continue
        if l.startswith('-'):
            if len(data) == 1:
                header = data[0]
                data = list()
                continue
            analyze_day(data, header)
            data = list()
        else:
            d = [i.strip() for i in l.strip().split(',')]
            data.append(d)


if __name__ == '__main__':
    fp = sys.argv[1]
    process_csv(fp)

