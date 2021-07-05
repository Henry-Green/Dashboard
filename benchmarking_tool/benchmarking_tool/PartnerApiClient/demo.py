from Emporia_Customer import Emporia_Customer
import matplotlib.pyplot as plt
import pandas as pd

serial_number = 'A2107A04B4B8F009A6CEC4'
d = 5

# new way of using the new data
customer = Emporia_Customer(serial_number)

customer.get_data(days= d)
customer.get_schedual()

print(type(customer.chan_min))
print(type(customer.channel_schedual))
print(customer.channel_schedual)
print(customer.chan_min)

'''
this is a key of the dictonary that the channel_schedual returns 
    it is a diconary of data frames 

    a 1.0 represents that the channel was ran for the hour on that day. 
    x axis is the hours in a day 
    y is the day of the month
    to determin if the channel is a 1 or a 0 i use this calc
    ON of hour_usage > (hour_mean + (0.5*standard_deviation_for_that_channel_on_that_hour))
    the hour mean is taken over the total number of days that where passed 
    the standard deviation of that hour is also taken from over the total days that where passed 

{'channel 4':     day: 24  day: 25  day: 26  day: 27  day: 28  day: 29
0       0.0      1.0      0.0      0.0      0.0      0.0
1       0.0      1.0      0.0      0.0      0.0      0.0
2       0.0      1.0      1.0      0.0      1.0      0.0
3       0.0      1.0      0.0      0.0      0.0      0.0
4       0.0      1.0      1.0      0.0      0.0      0.0
5       0.0      1.0      0.0      0.0      0.0      0.0
6       0.0      1.0      0.0      0.0      1.0      0.0
7       0.0      1.0      1.0      0.0      0.0      0.0
8       0.0      1.0      1.0      0.0      0.0      0.0
9       0.0      1.0      1.0      0.0      0.0      0.0
10      0.0      1.0      0.0      0.0      0.0      1.0
11      0.0      1.0      0.0      0.0      0.0      0.0
12      0.0      0.0      1.0      0.0      0.0      0.0
13      0.0      1.0      1.0      0.0      0.0      0.0
14      0.0      0.0      1.0      0.0      0.0      1.0
15      0.0      0.0      0.0      0.0      0.0      0.0
16      0.0      0.0      1.0      0.0      1.0      0.0
17      0.0      0.0      1.0      0.0      1.0      0.0
18      0.0      0.0      1.0      0.0      1.0      0.0
19      1.0      0.0      1.0      0.0      0.0      0.0
20      1.0      0.0      1.0      0.0      0.0      0.0
21      1.0      0.0      0.0      1.0      0.0      0.0
22      0.0      1.0      0.0      1.0      0.0      0.0
23      1.0      0.0      1.0      0.0      0.0      0.0


also cleaned up the average usage data frame that we get so that time is easier to get not columns are shifted over by a tab 

year  month  day  hour  minute  channel 4  channel 5  channel 6  channel 7  channel 8  channel 9  channel 10  channel 11
0     2021      6   24    15      25   0.116657        0.0        0.0   2.159895   3.181727        0.0         0.0         0.0
1     2021      6   24    15      26   0.115903        0.0        0.0   2.160352   3.239830        0.0         0.0         0.0
2     2021      6   24    15      27   0.115051        0.0        0.0   2.161042   3.176345        0.0         0.0         0.0
3     2021      6   24    15      28   0.115676        0.0        0.0   2.160208   3.172801        0.0         0.0         0.0
4     2021      6   24    15      29   0.116044        0.0        0.0   2.156394   3.173785        0.0         0.0         0.0
...    ...    ...  ...   ...     ...        ...        ...        ...        ...        ...        ...         ...         ...
7191  2021      6   29    15      16   0.110835        0.0        0.0   2.302055   4.290187        0.0         0.0         NaN
7192  2021      6   29    15      17   0.105769        0.0        0.0   2.301178   4.207229        0.0         0.0         NaN
7193  2021      6   29    15      18   0.110724        0.0        0.0   2.300801   3.817920        0.0         0.0         NaN
7194  2021      6   29    15      19   0.110410        0.0        0.0   2.300444   3.926082        0.0         0.0         NaN
7195  2021      6   29    15      20   0.110493        0.0        0.0   2.301643   3.957489        0.0         0.0         NaN
'''