#this application is to calculate difference between dates from 2 dates.
#we will use datatime module to import date
from datetime import date
#now we define a function to minus date 2 from date 1
def nume(d1, d2):
	return (d2-d1).days
#no we define dates, formate is ( year, month , day)
d1 = date(2021, 2 , 14 )
d2 = date(2020, 2 , 14 )
#now we print the function
print (nume(d1, d2), "days")
