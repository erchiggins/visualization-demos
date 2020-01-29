#include the pyplot subpackage of matplotlib, alias as plt by convention
import matplotlib.pyplot as plt

#prepare list of data for line plot - observe trend in sequential data
#number of batches started per calendar year
years = [2013,2014,2015,2016,2017,2018]
batches = [24,25,31,23,43,79]
plt.plot(years, batches)
plt.title('Batches Started per Year')
plt.xlabel('Year')
plt.ylabel('Number of Batches')

plt.show()