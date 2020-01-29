#include the pyplot subpackage of matplotlib, alias as plt by convention
import matplotlib.pyplot as plt

#prepare list of data for a histogram - observe distribution
#birthday months of USF trainers
birthday_months = [10, 11, 4, 7, 2, 12, 8, 12, 10, 7, 2, 1]

plt.hist(birthday_months, bins=12)
#default is 10 bins, increase or decrease to change granularity of histogram (histoGRANULARITY, hahaha)
plt.title('Birthday Months of USF Trainers')
plt.xlabel('Month')
plt.ylabel('Number of Birthdays')
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 
'September', 'October', 'November', 'December'])

plt.show()

