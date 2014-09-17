# Tae Kim
# problem 7
# thk301@nyu.edu
# Sort by area given zip code



import csv
import operator
import datetime
import sys
from operator import itemgetter, attrgetter
import itertools
from collections import defaultdict



def main():
    thisfile=sys.argv[1]
    #thisfile = "sample_data_problem_7.csv"
    zipfile=sys.argv[2]
    #zipfile = "zip_borough.csv"
    f = csv.reader(open(thisfile, "r"))
    next(f, None)
    q = csv.reader(open(zipfile, "r"))
    next(q, None)

    brooklyn=[]
    queen=[]
    bronx=[]
    manhattan=[]
    si=[]
    
    thiscount={"Brooklyn":0, "Queen":0, "Bronx":0, "Manhattan":0, "Staten Island":0}



    for row in q:
        if "BROOKLYN" in row:
            brooklyn.append(row[0])
        elif "QUEENS" in row:
            queen.append(row[0]) 
        elif "BRONX" in row:
            bronx.append(row[0])
        elif "MANHATTAN" in row:
            manhattan.append(row[0])
        else: 
            si.append(row[0]) 
            
    for row in f:
        if row[7] in brooklyn:
           thiscount["Brooklyn"]+=1
        elif row[7] in queen:
           thiscount["Queen"]+=1
        elif row[7] in bronx:
           thiscount["Bronx"]+=1
        elif row[7] in manhattan:
           thiscount["Manhattan"]+=1
        else:
           thiscount["Staten Island"]+=1
                     
    for k,v in sorted(thiscount.items(), key=lambda x: x[1], reverse=True):
        print k, " with ",  v, " complaints"         
        
    
if __name__ == "__main__":
    main()