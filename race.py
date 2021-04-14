import pandas as pd
import numpy as np
import bar_chart_race as bcr


# DataFrame 준비 

data = (pd.read_csv('conversation.csv', parse_dates=['date'])).set_index(['date'])
dates = sorted(set(data.index))
people = set(data['person'])

chart = pd.DataFrame(dates).rename(columns={0:'date'}).set_index(['date'])

for person in people:
    # messages = []
    days = []
    for date in dates:
        day_count = np.count_nonzero((data.loc[date,['person']]).values == person)
        days.append(day_count)
    period = 30

    sml_than_period = np.cumsum(days[:period])
    big_than_period = []

    for i in range(1,len(days)+1):
        if i <= period:
            continue
        else:
            big_than_period.append(np.sum(days[i-period:i]))
    
    person_data = np.append(sml_than_period, big_than_period)

    
        # day_count = np.count_nonzero((data.loc[date,['person']]).values == person)
        # if len(messages) >= 3:
        #     recent_two_days = [messages[-1], day_count ]
        #     if len(set(recent_two_days)) == 1:
        #         messages.append(0)
        #     else:
        #         messages.append(messages[-1]+day_count)
        # else:
        #     messages.append(messages[-1]+day_count if len(messages) >= 1 else day_count)
    
    chart[person] = person_data


print(chart)
chart.to_csv('dailyTMI.csv')
title = '제목 적기'


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
                                      's': f'msgs by period: {v.nlargest(6).sum():,.0f}',
                                      'ha': 'right', 'size': 8, 'family': 'Courier New'},
    perpendicular_bar_func='median',
    period_length=500,
    figsize=(5, 3),
    dpi=144,
    cmap='dark12',
    title=title,
    title_size='',
    bar_label_size=7,
    tick_label_size=7,
    shared_fontdict={'family' : 'D2Coding Ligature', 'color' : '.1'},
    scale='linear',
    writer=None,
    fig=None,
    bar_kwargs={'alpha': .7},
    filter_column_colors=True)  