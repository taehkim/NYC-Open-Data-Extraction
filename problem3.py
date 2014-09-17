# Tae Kim
# problem 3
# thk301@nyu.edu
# List and sort the complaint by number of complaints


import csv
import operator
from datetime import *
import sys
from operator import itemgetter, attrgetter



def main():
    thisfile=sys.argv[1]
    f = csv.reader(open(thisfile, "r"))
    next(f, None)
         
    complaints = {}
    for row in f:
        if row[5] in complaints:
            #print row[6]
            complaints[row[5]] += 1
        else:
            #print row[6]
            complaints[row[5]] = 1
    
    sortedlist =  sorted(complaints.items(), key=lambda(k,v): (-v,k))
 

    
    thisprint = dict(sortedlist)
    
    for i,o in sortedlist:  
      print i, " with "   ,  o, " complaints"
    

 
    
if __name__ == "__main__":
    main()