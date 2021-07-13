import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import string
import io


def get_data(serial_number, days):
    usage = ['1MIN','15MIN','1H']
    # first thing to do is call api and update the Output.txt file 
    # no api takes in a serial number and number of days to get past data. 
    line_list = call_api(serial_number, days)
    # line_list = []
    # with open("Output.txt", 'r') as text_file:
    #    for line in text_file:
    #        line_list.append(line)
            
    usage_list1 = get_usage(line_list, usage[0], serial_number)
    usage_list2 = get_usage(line_list, usage[1], serial_number)
    usage_list3 = get_usage(line_list, usage[2], serial_number)
    print('usage_list1')
    print(usage_list1)
    data1 = make_df(usage_list1)
    data2 = make_df(usage_list2)
    data3 = make_df(usage_list3)

    return [data1,data2,data3]

#getting date time and usage. 
# emporia app login
# phart@sustainergy.ca
# psswrd: 66hello77

def call_api(serial_number, days ):
    # this is a test call to the api
    #output = subprocess.run('ls')
    #date_proc = subprocess.Popen(['date'], stdout=subprocess.PIPE)
    # this runs on the command line to run the EmporiaEnergyApiClient.java 
    # this file is compiled in the mains folder 
    str_days = str(days)
    string1 = "java -cp lib\*;. mains.EmporiaEnergyApiClient phart@sustainergy.ca hello12345 "+serial_number+" "+str_days+" partner-api.emporiaenergy.com"
    output = subprocess.Popen(string1, shell=True,stdout=subprocess.PIPE)
    #date_proc.stdout.close()

    #print(output.stdout.read())
    st, s = output.communicate()
    # the returned sting is a long single string that is 
    slip = str(st)
    slip = slip.replace('\\n','\n')
    slip = slip.replace('\\t','\t')


    with open("Output.txt", "w") as text_file:
        for line in slip:
            
            text_file.write(line)
    with open("Output.txt", "r") as f:
        list_of_lines = [line.strip() for line in f]

    list_of_lines = [x.replace("\\r","") for x in list_of_lines]
    return list_of_lines





# this function returns a list of lists that is the usage of the device with the serial number given and in the format of 
# 1MIN 15MIN and 1H 
def get_usage(line_list, usage, serial_number):
    r = []
    for i in range(len(line_list)):
        s_list = line_list[i].split(' ')
        try:
            if s_list[0] == 'Usage:' and s_list[4].strip('\n') == usage and s_list[1] == serial_number:
                r.append(s_list)
                for j in line_list[i+1:]:
                    s2_list = j.split(' ')
                    if s2_list[0] == 'Usage:' or s2_list[0] == "'":
                        
                        break
                    else:
                        r.append(s2_list)
            if s_list[0] =='Usage':
                print('worked')
            else:
                print("no Work")
        except:
            continue
    return r


#this function take in a list from get_usage and makes it into a usabel pandas data frame 

def make_df(usage_list):
    time_list = []
    date_list = []
    channel_dict = {}
    for i in usage_list: 
        if i[0] == 'Usage:':
            serial_number = i[1]
            scale = i[4]
        else:
            # make the time formate better 
            time1 = i[0].strip('\t')
            time1 = time1.replace('T',' ')
            time1 = time1.replace('Z:', '')
            t = time1.split(' ')
            date = t[0]
            time = t[1]
            time_list.append(time)
            date_list.append(date)
            # get the number of channels 
            num_channel = int((len(i)-1)/3)
            
            # init the channel dict 
            if channel_dict == {}:
                for e in range(num_channel):
                    e+=1
                    number = i[(e*3 - 1)]
                    number = number.strip('(')
                    number = number.strip(')')
                    channel_string ='channel ' + number
                    channel_dict[channel_string] = []

            
            for c in range(num_channel):
                c+=1
                number = i[(c*3 - 1)]
                number = number.strip('(')
                number = number.strip(')')
                channel_string = 'channel ' + number
                
                d = i[c*3].strip('\n')
                d = d.strip(';')
                channel_dict[channel_string].append(float(d))

    #print(time_list)       
    #print(channel_dict)

    df = pd.DataFrame(channel_dict)
    df.insert(0, "date", date_list)
    df.insert(1,"time", time_list)
    
    # this line shows a basic plot of the data frame 
    #df.plot.line()
    #plt.show()

    # if want to return a data frame just comment out this line. 
    #dd = df.to_dict()
    #dd = df.values.tolist()
    return df

def get_serial_list(line_list):
    r = []
    for i in line_list:
        spit = i.split(' ')
        try:
            if spit[1] == 'devices:':
                for j in spit[2:]:
                    #print(spit)
                    s_number = j
                    s_number = s_number.replace(']', '')
                    s_number = s_number.replace('[', '')
                    s_number = s_number.replace('\n', '')
                    r.append(s_number)
                    
        except:
            continue
    return r


# this takes in the line list and then outputs the token ID
def get_token_id(l):
    token = l[1].split(' ')

    token_id = token[6].rstrip()

    return token_id


