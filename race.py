import pandas as pd
import numpy as np
import bar_chart_race as bcr


# DataFrame 준비 

data = (pd.read_csv('e.csv', parse_dates=['date'])).set_index(['date'])
dates = sorted(set(data.index))
people = set(data['person'])

chart = pd.DataFrame(dates).rename(columns={0:'date'}).set_index(['date'])

for person in people:
    messages = []
    for date in dates:
        day_count = np.count_nonzero((data.loc[date,['person']]).values == person)
        if len(messages) >= 7:
            lastweek = sum([messages[-(i+1)] for i in range(6)])
            if lastweek != 0:
                messages.append(messages[-1]+day_count)
            else:
                messages.append(0)
        else:
            messages.append(messages[-1]+day_count if len(messages) >= 1 else day_count)
    chart[person] = messages


print(chart)
# bar_chart_race 그리기

import bar_chart_race as bcr
bcr.bar_chart_race(
    df=chart,
    filename='race.mp4',
    orientation='h',
    sort='desc',
    n_bars=10,
    fixed_order=False,
    fixed_max=True,
    steps_per_period=20,
    interpolate_period=False,
    label_bars=True,
    bar_size=.95,
    period_label={'x': .99, 'y': .25, 'ha': 'right', 'va': 'center'},
    period_fmt='%B %d, %Y',
    period_summary_func=lambda v, r: {'x': .99, 'y': .18,
                                      's': f'Total msgs: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title='TMI 순위',
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'D2Coding Ligature', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=False)  