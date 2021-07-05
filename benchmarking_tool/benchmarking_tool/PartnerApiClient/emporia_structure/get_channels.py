# this will take out the 3 first channels and get the mains 
import pandas as pd
from .Channel import Channel 
def get_channels(data):
    list_of_series = []
    try: 
        data = data.drop(['date','time'], axis = 1)
    except:
        pass
    total = pd.Series(0,index=range(len(data)),dtype='float64')
    cols = data.columns.tolist()

    #total = np.array(len(data))
    for i in cols:
        if i == 'channel 1' or i == 'channel 2' or i == 'channel 3':
            t = data[i]
            total = total.add(t)
        else:
            channy = Channel()
            channy.data = data[i]
            list_of_series.append(channy)

    t = Channel()
    t.data = total

    return [t, list_of_series]