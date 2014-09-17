# Tae Kim
# problem 1
# thk301@nyu.edu
# calculates number of complaints and time frame


import csv
import operator
from datetime import *
import sys

class Comp():
    def __init__(self, uniq, created, closed, agency, agname, comptype,  desc,  zip,  stat):
        self.uniq = uniq
        self.created = created
        self.closed = closed
        self.agency = agency
        self.agname = agname
        self.comptype = comptype
        self.desc = desc
        self.zip = zip



def main():
    thisfile=sys.argv[1]
    f = csv.reader(open(thisfile, "r"))
    comp = [Comp(row[0], row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]) for row in f][1::]
    
    #for i in range(len(comp)):
    z= sorted(comp, key=operator.attrgetter('created'))
    print len(comp), " complaints ",
    a = len(comp)
    print "between ",datetime.strptime(z[0].created, '%m/%d/%Y %I:%M:%S %p').strftime('%m/%d/%Y %H:%M:%S').lower()," and ",(datetime.strptime(z[a-1].created, '%m/%d/%Y %I:%M:%S %p').strftime('%m/%d/%Y %H:%M:%S').lower())
     
 
if __name__ == "__main__":
    main()