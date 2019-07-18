#include the pyplot subpackage of matplotlib, alias as plt by convention
import matplotlib.pyplot as plt
#include datetime and matplotlib dates subpackage for date handling in scatter plot
import datetime as dt
import matplotlib.dates as mdates
#numpy for additional data processing features
import numpy as np

#prepare list of data for scatter plot - observe correlations
#batch sizes per start date
dates = ['01/02/1991','01/03/1991','01/04/1991']
plot_dates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
batch_size = [15, 20, 10]
np_batch_size = np.array(batch_size)
np_batch_size = np_batch_size*5
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.scatter(plot_dates,batch_size,s=np_batch_size)
plt.gcf().autofmt_xdate()

plt.title('Batch Sizes Over Time')
plt.xlabel('Batch Start Date')
plt.ylabel('Batch Size')

plt.show()