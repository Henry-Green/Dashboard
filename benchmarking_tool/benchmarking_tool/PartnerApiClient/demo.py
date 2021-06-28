from get_data import get_data
import matplotlib.pyplot as plt
import pandas as pd

serial_number = 'A2107A04B4B8F009A6CEC4'

l = get_data(serial_number)

min = l[0]
fivmin = l[1]
hour = l[2]
#min fivmin and hour are all data frames to show what the data looks like adn the graphs show how it will be shown 
# to convert the dataframes to anything that makes it easiest use these commands 
# min = min.to_dict() # to a dictionary 
# min = min.values.tolist() # to a list of lists 
# the list one can look a bit messy that is why i have left it like this so it is easy to see

print(min)
print(fivmin)
print(hour)

#min.plot.line()
#fivmin.plot.line()
#hour.plot.line()
#plt.show()