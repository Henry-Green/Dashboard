from .emporia_structure import ave_channel_usage, Channel, clean_data,get_channels,on_off_usage,UTC_MTN

from .get_data import get_data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

class Emporia_Customer():
    def __init__(self, serial_number):
        self.serial_number = serial_number # string 

        self.address = None
        self.description = None # a description of the channels 

        # need to set all the channels and names on the channels 

        # init all channel classes 
        self.mains = Channel()

        self.channel1 = Channel()
        self.channel2 = Channel()
        self.channel3 = Channel()
        self.channel4 = Channel()
        self.channel5 = Channel()
        self.channel6 = Channel()
        self.channel7 = Channel()
        self.channel8 = Channel()
        self.channel9 = Channel()
        self.channel10 = Channel()
        self.channel11 = Channel()
        self.channel12 = Channel()
        self.channel13 = Channel()
        self.channel14 = Channel()
        self.channel15 = Channel()
        self.channel16 = Channel()
        self.channel17 = Channel()
        self.channel18 = Channel()
        self.channel19 = Channel()
        self.channel20 = Channel()

    def get_data(self, days):
        #mains, channels = get_data(serial_number=self.serial_number, days=days)
        l = get_data(self.serial_number, days)

        mint = l[0]
        fivmin = l[1]
        hour = l[2]

        mains_hours, chan_hours = clean_data(hour)
        mains_fivmin, chan_fivmin = clean_data(fivmin)
        mains_min, chan_min = clean_data(mint)

        self.mains_hours = mains_hours
        self.mains_fivmin = mains_fivmin
        self.mains_min = mains_min

        self.chan_hours = chan_hours
        self.chan_fivmin = chan_fivmin
        self.chan_min = chan_min
    
    def get_schedule(self): 
        # gets the schedule of the pas days 

        self.schedule = on_off_usage(self.chan_hours)
        self.mains_schedule = on_off_usage(self.mains_hours)

    def save_channels(self):  

        # first save the mains 
        self.mains.data_hour = self.mains_hours
        self.mains.data_fivmin = self.mains_fivmin
        self.mains.data_min = self.mains_min
        self.mains.schedule = self.mains_schedule

        # store the channels into a list for the customer
        cols = self.chan_hours.columns.tolist()
        
        for i in cols:
            if i == 'channel 4':
                self.channel4.data_hour = self.chan_hours[i]
                self.channel4.data_fivmin = self.chan_fivmin[i]
                self.channel4.data_min = self.chan_min[i]
                self.channel4.schedule = self.schedule[i]

            if i == 'channel 5':
                self.channel5.data_hour = self.chan_hours[i]
                self.channel5.data_fivmin = self.chan_fivmin[i]
                self.channel5.data_min = self.chan_min[i]
                self.channel5.schedule = self.schedule[i]

            if i == 'channel 6':
                self.channel6.data_hour = self.chan_hours[i]
                self.channel6.data_fivmin = self.chan_fivmin[i]
                self.channel6.data_min = self.chan_min[i]
                self.channel6.schedule = self.schedule[i]

            if i == 'channel 7':
                self.channel7.data_hour = self.chan_hours[i]
                self.channel7.data_fivmin = self.chan_fivmin[i]
                self.channel7.data_min = self.chan_min[i]
                self.channel7.schedule = self.schedule[i]

            if i == 'channel 8':
                self.channel8.data_hour = self.chan_hours[i]
                self.channel8.data_fivmin = self.chan_fivmin[i]
                self.channel8.data_min = self.chan_min[i]
                self.channel8.schedule = self.schedule[i]

            if i == 'channel 9':
                self.channel9.data_hour = self.chan_hours[i]
                self.channel9.data_fivmin = self.chan_fivmin[i]
                self.channel9.data_min = self.chan_min[i]
                self.channel9.schedule = self.schedule[i]

            if i == 'channel 10':
                self.channel10.data_hour = self.chan_hours[i]
                self.channel10.data_fivmin = self.chan_fivmin[i]
                self.channel10.data_min = self.chan_min[i]
                self.channel10.schedule = self.schedule[i]

            if i == 'channel 11':
                self.channel11.data_hour = self.chan_hours[i]
                self.channel11.data_fivmin = self.chan_fivmin[i]
                self.channel11.data_min = self.chan_min[i]
                self.channel11.schedule = self.schedule[i]

            if i == 'channel 12':
                self.channel12.data_hour = self.chan_hours[i]
                self.channel12.data_fivmin = self.chan_fivmin[i]
                self.channel12.data_min = self.chan_min[i]
                self.channel12.schedule = self.schedule[i]
            
            if i == 'channel 13':
                self.channel13.data_hour = self.chan_hours[i]
                self.channel13.data_fivmin = self.chan_fivmin[i]
                self.channel13.data_min = self.chan_min[i]
                self.channel13.schedule = self.schedule[i]

            if i == 'channel 14':
                self.channel14.data_hour = self.chan_hours[i]
                self.channel14.data_fivmin = self.chan_fivmin[i]
                self.channel14.data_min = self.chan_min[i]
                self.channel14.schedule = self.schedule[i]

            if i == 'channel 15':
                self.channel15.data_hour = self.chan_hours[i]
                self.channel15.data_fivmin = self.chan_fivmin[i]
                self.channel15.data_min = self.chan_min[i]
                self.channel15.schedule = self.schedule[i]
            
            if i == 'channel 16':
                self.channel16.data_hour = self.chan_hours[i]
                self.channel16.data_fivmin = self.chan_fivmin[i]
                self.channel16.data_min = self.chan_min[i]
                self.channel16.schedule = self.schedule[i]

            if i == 'channel 17':
                self.channel17.data_hour = self.chan_hours[i]
                self.channel17.data_fivmin = self.chan_fivmin[i]
                self.channel17.data_min = self.chan_min[i]
                self.channel17.schedule = self.schedule[i]

            if i == 'channel 18':
                self.channel18.data_hour = self.chan_hours[i]
                self.channel18.data_fivmin = self.chan_fivmin[i]
                self.channel18.data_min = self.chan_min[i]
                self.channel18.schedule = self.schedule[i]
            
            if i == 'channel 19':
                self.channel19.data_hour = self.chan_hours[i]
                self.channel19.data_fivmin = self.chan_fivmin[i]
                self.channel19.data_min = self.chan_min[i]
                self.channel19.schedule = self.schedule[i]

            if i == 'channel 20':
                self.channel20.data_hour = self.chan_hours[i]
                self.channel20.data_fivmin = self.chan_fivmin[i]
                self.channel20.data_min = self.chan_min[i]
                self.channel20.schedule = self.schedule[i]
        return 


'''
# this should take about 11 seconds 
serial_number = 'A2107A04B4B8F009A6CEC4'
customer = Emporia_Customer(serial_number)

customer.get_data(days= 5)
customer.get_schedule()

customer.save_channels()

print(customer.channel4.data_hour)
print(customer.channel4.schedule)
'''