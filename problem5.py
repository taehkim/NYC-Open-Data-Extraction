# Tae Kim
# problem 5
# thk301@nyu.edu
# Calculate & sort number of complaints by day


import csv
import operator
import datetime
import sys
from operator import itemgetter, attrgetter
import itertools



def main():
    thisfile=sys.argv[1]
    #thisfile="sample_data_problem_5.csv"
    f = csv.reader(open(thisfile, "r"))
    next(f, None)
 
    week={'Monday':0, 'Tuesday':0, 'Wednesday': 0, 'Thursday':0, 'Friday':0, 'Saturday':0, 'Sunday':0}

    for row in f:
        date = datetime.datetime.strptime(row[1], '%m/%d/%Y %I:%M:%S %p')
        if date.strftime('%A') in week:
            week[date.strftime('%A')] += 1
        else:
            week[date.strftime('%A')] = 1
            
    
    for i in week:
        print i, " == ", week[i] 
        
    
if __name__ == "__main__":
    main()