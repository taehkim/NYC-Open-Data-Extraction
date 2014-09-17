# Tae Kim
# problem 4
# thk301@nyu.edu
# List, sort, and display top N

import csv
import operator
from datetime import *
import sys
from operator import itemgetter, attrgetter
import itertools



def main():
    thisfile=sys.argv[1]
    #thisfile="sample_data_problem_4.csv"
    topK1=sys.argv[2]
    topK = int(topK1) 
    #topK= 3
    f = csv.reader(open(thisfile, "r"))
    next(f, None)
         
    complaints = {}
    for row in f:
        if row[5] in complaints:
            complaints[row[5]] += 1
        else:
            complaints[row[5]] = 1
    
    sortedlist =  sorted(complaints.items(), key=lambda(k,v): (-v,k))
 
    topKlist = sortedlist[:topK]
  
    for i,o in topKlist:  
      print i, " with "   ,  o, " complaints"
    
    
if __name__ == "__main__":
    main()