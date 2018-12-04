---
layout: advent-item
title: 4th Advent - Pandas Merge As Of
date: 2018-11-30
advent: 4
description: Merging time series data without resampling. # Add post description (optional)
img: pandas_merge_as_of.png # Add image post (optional)
tags: [Blog, Advent, Data]
author: # Add name author (optional)
---
Merging dataframes with datetime values can be tricky if the time is not exact.
Pandas does a great job working with this.

First DataFrame
{% highlight python %}
>>> quotes
                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03
{% endhighlight %}

Second DataFrame
{% highlight python %}
>>> trades
                     time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.048   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100
{% endhighlight %}

Merging them DataFrame
{% highlight python %}
>>> pd.merge_asof(trades, quotes,
...                       on='time',
...                       by='ticker')
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
{% endhighlight %}

As you can the time index has slight time differences, still they are being merged.

[Read full documentation][pandas-doc]


[pandas-doc]:https://pandas.pydata.org/pandas-docs/stable/generated/pandas.merge_asof.html