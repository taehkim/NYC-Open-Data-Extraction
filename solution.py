# Tae H. Kim
# Output will be saved as tae.db as well as display on terminal.


import sys

db ={}
sorted_keys={}
names=['Agency', '# Of Positions', 'Business Title', 'Civil Service Title', 
       'Salary Range From', 'Salary Range To',  'Salary Frequency', 'Work Location', 
       'Division /Work Unit', 'Job Description', 'Minimum Qual Requirements', 'Preferred Skills',  
       'Additional Information','Posting Date']


def clear():
  db.clear()
  with open("tae.db", "w") as f:
      f.write("")
  
   


# Inserts a job offer into the database.
def insert(fieldValues):
  job_id = fieldValues[0]
  job_descrip = fieldValues[1:]

  if job_id in db:
      pass
  else:
      db[job_id]=job_descrip
    


# Updates all job offers that attend the field_name=old_value pair.
def update_all(params):
    query_field_name = params[0]
    query_field_value = params[1]
    update_field_name = params[2]
    update_field_value = params[3]

    updatedRowCount = 0
    
    
    for row in db:
     if query_field_name in names:
         thisquery = names.index(query_field_name) 
        
         if db[row][thisquery] == query_field_value:
             if update_field_name in names:
                thispoint = names.index(update_field_name) 
                db[row][thispoint]=update_field_value
                updatedRowCount+=1
                
        
        
        
  
    # Prints number of updated rows in the database.
    with open('tae.db', 'a') as f:
     print str(updatedRowCount)
     f.write(str(updatedRowCount)+'\n')
   

# Deletes all job offers that attend the field_name=field_value pair.
def delete_all(params):
  field_name, field_value = params
  
  # TODO Complete with your code and remove print below.
  #print 'delete_all where ' + field_name + '=' + field_value
  
#   for field_name in db.items():
#       if field_value in db:
#           del db[field_value] 
          

  for k,v in db.items():
      if field_name in names:
         thisdel = names.index(field_name) 
         if field_value in db[k][thisdel]:
            del db[k]
      else:
        for field_name in db.items():
          if field_value in db:
            del db[field_value]     
    

  


# Prints all job offers that match the query field_name=field_value, one per
# line, semicolon-separated, with fields in the order defined in the assignment.
def find(params):
  field_name, field_value = params

  with open('tae.db', 'w') as f:
  # TODO Complete with your code and remove print below.
  #print 'find where ' + field_name + '=' + field_value
   for row in db:
     if field_name in names:
         thisfield = names.index(field_name) 
         if db[row][thisfield] == field_value:
            #print db[row]
            output ='' 
            for i in db[row]:
                output = output+ '|'+ i
            print row, output
            f.write(row+output+'\n')





# Prints how many job offers match the query field_name=field_value.
def count(params):
  field_name, field_value = params

  print 'count job offers where ' + field_name + '=' + field_value


# Prints all job offers in the database, one per line, semicolon-separated, with
# fields in the order defined in the assignment.
def dump(params):
     
  sorted_keys=sorted(db.keys())
  with open('tae.db', 'a') as f:
         
   for job_id in sorted_keys:
    job_descrip=db[job_id]
    
    output ='' 
    
    for descrip in job_descrip:
        output = output+ '|'+ descrip
       
    print job_id+output
    f.write(job_id+output+'\n' )
    
      

# Prints all job offers, one per line, semicolon-separated, but only the
# specified fields, in the order specified for the view.
def view(fieldNames):
  thisIndex=[]
  
  for i in fieldNames:
      if i in names:
          thisIndex.append(names.index(i))
 
  output=''
  
  with open('tae.db', 'a') as f:
   for z in sorted(db):
      print db[z][thisIndex[0]],'|', z,'|',
      output=db[z][thisIndex[0]]+'|'+ z+'|'
      for i in xrange(1,len(thisIndex)): 
            print db[z][thisIndex[i]], '|', 
            output=output+db[z][thisIndex[i]]+ '|' 
            i +=0
      print ""
      f.write(output+'\n')
#    

def executeCommand(commandLine):
  tokens = commandLine.split('|') #assume that this symbol is not part of the data
  command = tokens[0]
  parameters = tokens[1:]

  if command == 'insert':
    insert(parameters)
  elif command == 'delete_all':
    delete_all(parameters)
  elif command == 'update_all':
    update_all(parameters)
  elif command == 'find':
    find(parameters)
  elif command == 'count':
    count(parameters)
  elif command == 'count_unique':
    count_unique(parameters)
  elif command == 'clear':
    clear()
  elif command == 'dump':
    dump(parameters)
  elif command == 'view':
    view(parameters)
  else:
    print 'ERROR: Command %s does not exist' % (command,)
    assert(False)

def executeCommands(commandFileName):
  f = open(commandFileName)
  for line in f:
    executeCommand(line.strip())

if __name__ == '__main__':
  
  
  #thisfile="sample_data_problem_6.txt"
  thisfile=sys.argv[1]
  executeCommands(thisfile)
 
