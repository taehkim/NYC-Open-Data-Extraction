# Tae Kim
# problem 6
# thk301@nyu.edu
# Sort by Deptarment & zip code


import csv
import operator
from datetime import *
import sys
from operator import itemgetter, attrgetter
from collections import defaultdict


def main():
    thisfile=sys.argv[1]
    #thisfile="sample_data_problem_6.csv"
    f = csv.reader(open(thisfile, "r"))
    next(f, None)
 
    agencies={}
    for row in f:
        if row[7] in agencies:
            count += 1
            agencies[row[7]] = (row[3], count)
        else:
            count=1
            agencies[row[7]] = (row[3], count)
    
    #print agencies
            
    thislist=defaultdict(list)
    
    
    for key, value in agencies.items():
        thislist[value].append(key)
    
    for k in sorted(thislist):
        print k[0], thislist[k], k[1]
        #print len(thislist[k])
 
    
if __name__ == "__main__":
    main()