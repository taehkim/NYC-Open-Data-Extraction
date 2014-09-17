# Tae Kim
# problem 2
# thk301@nyu.edu
# displays number of complaints

import csv
import operator
from datetime import *
import sys



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
    
    for i in complaints:  
        print i," with ",  complaints[i], " complaints"
    
 
if __name__ == "__main__":
    main()