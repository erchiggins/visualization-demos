#include the pyplot subpackage of matplotlib, alias as plt by convention
import matplotlib.pyplot as plt
#include datetime and matplotlib dates subpackage for date handling in scatter plot
import datetime as dt
import matplotlib.dates as mdates
#numpy for additional data processing features
import numpy as np

#prepare data for scatter plot - observe correlations
#batch sizes per start date

#batch start date list construction
jan_dates = ['01/08/2018','01/08/2018','01/22/2018','01/22/2018','01/29/2018']
feb_dates = ['02/05/2018','02/05/2018','02/12/2018','02/26/2018','02/26/2018','02/26/2018']
mar_dates = ['03/12/2018','03/05/2018','03/26/2018','03/19/2018','03/26/2018']
apr_dates = ['04/02/2018','04/09/2018','04/16/2018','04/09/2018','04/16/2018','04/23/2018','04/23/2018','04/30/2018']
may_dates = ['05/07/2018','05/14/2018','05/21/2018','05/21/2018','05/29/2018']
jun_dates = ['06/04/2018','06/04/2018','06/04/2018','06/11/2018','06/11/2018','06/18/2018','06/17/2018','06/18/2018','06/11/2018','06/25/2018','06/25/2018']
dates = jan_dates+feb_dates+mar_dates+apr_dates+may_dates+jun_dates
plot_dates = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]

#batch size list construction
#q1
q1_batch_size = [21,17,10,19,13,28,18,21,13,14,23,13,22,19,28,12]
#q2
q2_batch_size = [25,16,22,15,13,21,11,21,15,12,21,23,19,15,15,20,18,22,12,18,16,11,23,22]
#q3
q3_batch_size = []
#q4
q4_batch_size = []
batch_size = q1_batch_size+q2_batch_size+q3_batch_size+q4_batch_size

#batch location list construction
q1_batch_location = ['USF','Reston','CUNY','Reston','USF','Reston','Reston','USF','CUNY','Reston','Reston','USF','USF','USF','Reston','Reston']
q2_batch_location = ['Reston','Reston','USF','USF','Reston','Reston','USF','Reston','Reston','USF','Reston','USF','WVU','Reston','USF','Reston','USF','WVU','USF','Reston','UTA','USF','Reston','USF']
q3_batch_location = []
q4_batch_location = []
batch_location = q1_batch_location+q2_batch_location+q3_batch_location+q4_batch_location

#size of markers
np_batch_size = np.array(batch_size)
np_batch_size = np_batch_size*10

#color of markers by location
colors = {'Reston':'blue','USF':'green','CUNY':'red','WVU':'yellow','UTA':'orange'}
batch_colors = [colors[loc] for loc in batch_location]

#date format
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.scatter(plot_dates,batch_size,s=np_batch_size,alpha=0.8,c=batch_colors)
plt.gcf().autofmt_xdate()

plt.title('Batch Sizes In 2018 Q1, Q2')
plt.xlabel('Batch Start Date')
plt.ylabel('Batch Size')

x_dates = ['01/01/2018','02/01/2018','03/01/2018','04/01/2018','05/01/2018','06/01/2018','07/01/2018']
plt.xticks([dt.datetime.strptime(d,'%m/%d/%Y').date() for d in x_dates])

plt.show()