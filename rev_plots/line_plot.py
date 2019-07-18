#include the pyplot subpackage of matplotlib, alias as plt by convention
import matplotlib.pyplot as plt
#include datetime and matplotlib dates subpackage for date handling in scatter plot
import datetime as dt
import matplotlib.dates as mdates
#numpy for additional data processing features
import numpy as np

#prepare list of data for line plot - observe trend in sequential data
#number of batches conducted per calendar year, according to Salesforce
years = []
batches = []
plt.plot(years, batches)
plt.title('Batches Conducted per Year')
plt.xlabel('Year')
plt.ylabel('Number of Batches')

plt.show()