# helper function to get average and standard deviation 

def ave_channel_usage(channels_hours):
    gpchan = channels_hours.groupby('hour', as_index = False).mean()
    stdchan = channels_hours.groupby('hour', as_index = False).std()

    try:
        gpchan = gpchan.drop(['year','month','day','minute'], axis=1)
        stdchan = stdchan.drop(['year','month','day','minute'], axis=1)
    except:
        pass


    return gpchan, stdchan