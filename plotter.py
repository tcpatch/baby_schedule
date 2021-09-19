#!/usr/bin/env python3
import sys
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as patches


def analyze_day(data, date, header=None):
    group = 1
    x_col = 0
    
    df = pd.DataFrame(data)

    if header:
        df.columns = header
        group = header[1]
        x_col = header[0]

    df[['hour', 'minute']] = df[x_col].str.split(':', expand=True)
    df = df.astype({'hour': 'float64', 'minute': 'float64'})
    df['minute'] = df['minute'] / 60.0
    df['time'] = df['hour'] + df['minute']

    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(10)

    # TODO would be nice to normalize inputs/order
    for i, _df in df.groupby(group):
        # TODO for nap start/end put on one track
        ax.scatter(_df[x_col],
                    _df[_df[group] == i][group])

    # formatting...
    ax.set_xlim(0, 24)
    ax.set_xticks(range(0, 25))
    ax.set_title(date)
    n_categories = df[group].nunique()
    # TODO would be nice to use `astral` or something to get actual sunrise and sunset
    rect1 = patches.Rectangle((0, -1), 5.5, n_categories + 1, alpha=0.5, color='grey')
    rect2 = patches.Rectangle((20.0, -1), 4, n_categories + 1, alpha=0.5, color='grey')
    ax.add_patch(rect1)
    ax.add_patch(rect2)
    out_fp = '{}.png'.format(date.replace('/', '-'))
    plt.savefig(out_fp)
    img_tag = '<img src="{}">'.format(out_fp)
    return img_tag


def process_csv(fp):
    with open(fp, 'r') as f:
        lines = f.readlines()

    data = list()
    header = None
    week_number = None
    date = None
    image_tags = list()

    for l in lines:
        if 'week' in l.lower():
            week_number = l.strip()
            continue
        if l.startswith('-'):
            if len(data) == 1:
                header = data[0]
                data = list()
                date = l.strip().replace('-', '')
                continue
            img_tag = analyze_day(data, date, header)
            image_tags.append(img_tag)
            date = l.strip().replace('-', '')
            data = list()
        else:
            d = [i.strip() for i in l.strip().split(',')]
            data.append(d)
    with open('summary.html', 'w') as fp:
        fp.write('<h1>{}</h1>'.format(week_number))
        fp.write('\n'.join(image_tags))


if __name__ == '__main__':
    fp = sys.argv[1]
    process_csv(fp)

