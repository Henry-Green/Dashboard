# need to get last 7 days usage by 24 hours 
# takes in all channels and then returns 11 data frames that are 24 rows by 7 days 
import numpy as np
import pandas as pd
from .ave_channel_usage import ave_channel_usage
def on_off_usage(channels):
    #print(channels)

    dayz = channels.groupby('day', as_index= False).count()
    #print(d)

    all_days = dayz['day'].values

    t = channels.groupby(['day','hour'], as_index = False).last()
   

    channels = t.drop(columns = ['year','month','minute'])
    
    
    # get the average and the standard diviation of the channels 
    averchan, stdchan = ave_channel_usage(channels)


    # init the data frame the on and off structure will be going  into 
    # make the thing a dict 
    dd = {}
    for i in all_days:
        dd['day: '+ str(i)] = np.zeros(24)

    output_df = pd.DataFrame(dd)

    # now we loop through all the channels usage 
    # if the usage is greater then the mean + (0.5*std) of that time frame. we then assume the circuit is on.

    # need a channel list 
    cols = channels.columns.tolist()
    # drop hours and 
    if (cols[0] == 'day') & (cols[1] == 'hour'):
        cols = cols[2:]


    row_dict = {}

    for c in cols:
        row_dict[c] = output_df.copy()

    for d in all_days: 
        for h in range(24): # hours in a day does not change  
            for c in cols: 
                row = channels[(channels['day'] == int(d)) & (channels['hour'] == int(h))]
                if row.empty:
                    
                    continue

                row = row.reset_index()
                usage = row[c][0]
                std = stdchan[c][h]
                ave = averchan[c][h]
                if usage > (ave + (0.5*std)):
                    # it is on 
                    row_dict[c].at[h, 'day: ' + str(d)] = 1
                    
                else:
                    # it is off
                    pass
    
    return row_dict