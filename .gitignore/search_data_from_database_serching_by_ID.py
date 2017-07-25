import time
#import json
import MySQLdb
while True:
    SQL="select * from user"
    Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="hussain", db="user")
    cursor=Con.cursor()
    cursor.execute(SQL)
    data=cursor.fetchall()
    Con.commit()
    #json_output=json.dumps(data)
    #print data
    ID=int(input("Enter Your ID:"))
    if(ID==101 or ID==102 or ID==103 or ID==104 or ID==105 or ID==106 or ID==107 or ID==108 or ID==109 or ID==110 or ID==123 
       or ID==330 or ID==160 or ID==157 or ID==190 or ID==160):
        if ID in data[0]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[0]
        #if you want to part by part result and design you have to write code like below...
            print "Name:",data[0][1]
            print "Email:",data[0][2]
            print "Salary:",data[0][3]
            print "Phone NO:",data[0][4]
            print "State:",data[0][5]
            print "Company:",data[0][6]
        
        elif ID in data[1]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[1]
            
          #if you want to part by part result and design you have to write code like below...  
            print "Name:",data[1][1]
            print "Email:",data[1][2]
            print "Salary:",data[1][3]
            print "Phone NO:",data[1][4]
            print "State:",data[1][5]
            print "Company:",data[1][6]
        
            
        elif ID in data[2]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[2]
            
         #if you want to part by part result and design you have to write code like below...   
            print "Name:",data[2][1]
            print "Email:",data[2][2]
            print "Salary:",data[2][3]
            print "Phone NO:",data[2][4]
            print "State:",data[2][5]
            print "Company:",data[2][6]
        
        elif ID in data[3]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[3]
            
          #if you want to part by part result and design you have to write code like below...  
            print "Name:",data[3][1]
            print "Email:",data[3][2]
            print "Salary:",data[3][3]
            print "Phone NO:",data[3][4]
            print "State:",data[3][5]
            print "Company:",data[3][6]
            
        elif ID in data[4]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[4]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[4][1]
            print "Email:",data[4][2]
            print "Salary:",data[4][3]
            print "Phone NO:",data[4][4]
            print "State:",data[4][5]
            print "Company:",data[4][6]
            
        elif ID in data[5]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[5]
            
            #if you want to part by part result and design you have to write code like below...
            print "Name:",data[5][1]
            print "Email:",data[5][2]
            print "Salary:",data[5][3]
            print "Phone NO:",data[5][4]
            print "State:",data[5][5]
            print "Company:",data[5][6]
        
        elif ID in data[6]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[6]
            
         #if you want to part by part result and design you have to write code like below...   
            print "Name:",data[6][1]
            print "Email:",data[6][2]
            print "Salary:",data[6][3]
            print "Phone NO:",data[6][4]
            print "State:",data[6][5]
            print "Company:",data[6][6]
        
        elif ID in data[7]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[7]
         
         #if you want to part by part result and design you have to write code like below...   
            print "Name:",data[7][1]
            print "Email:",data[7][2]
            print "Salary:",data[7][3]
            print "Phone NO:",data[7][4]
            print "State:",data[7][5]
            print "Company:",data[7][6]
        
        elif ID in data[8]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[8]
         
         #if you want to part by part result and design you have to write code like below...   
            print "Name:",data[8][1]
            print "Email:",data[8][2]
            print "Salary:",data[8][3]
            print "Phone NO:",data[8][4]
            print "State:",data[8][5]
            print "Company:",data[8][6]
            
        elif ID in data[9]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[9]
        
        #if you want to part by part result and design you have to write code like below...    
            
            print "Name:",data[9][1]
            print "Email:",data[9][2]
            print "Salary:",data[9][3]
            print "Phone NO:",data[9][4]
            print "State:",data[9][5]
            print "Company:",data[9][6]
        
        elif ID in data[10]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[10]
         
         #if you want to part by part result and design you have to write code like below...   
            
            print "Name:",data[10][1]
            print "Email:",data[10][2]
            print "Salary:",data[10][3]
            print "Phone NO:",data[10][4]
            print "State:",data[10][5]
            print "Company:",data[10][6]
        
        elif ID in data[11]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[11]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[11][1]
            print "Email:",data[11][2]
            print "Salary:",data[11][3]
            print "Phone NO:",data[11][4]
            print "State:",data[11][5]
            print "Company:",data[11][6]
        
        elif ID in data[12]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[12]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[12][1]
            print "Email:",data[12][2]
            print "Salary:",data[12][3]
            print "Phone NO:",data[12][4]
            print "State:",data[12][5]
            print "Company:",data[12][6]
            
        elif ID in data[13]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[13]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[13][1]
            print "Email:",data[13][2]
            print "Salary:",data[13][3]
            print "Phone NO:",data[13][4]
            print "State:",data[13][5]
            print "Company:",data[13][6]
        
        elif ID in data[14]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[14]
            
         #if you want to part by part result and design you have to write code like below...   
            print "Name:",data[14][1]
            print "Email:",data[14][2]
            print "Salary:",data[14][3]
            print "Phone NO:",data[14][4]
            print "State:",data[14][5]
            print "Company:",data[14][6]
            
        elif ID in data[15]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[15]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[15][1]
            print "Email:",data[15][2]
            print "Salary:",data[15][3]
            print "Phone NO:",data[15][4]
            print "State:",data[15][5]
            print "Company:",data[15][6]
            
        elif ID in data[16]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[16]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[16][1]
            print "Email:",data[16][2]
            print "Salary:",data[16][3]
            print "Phone NO:",data[16][4]
            print "State:",data[16][5]
            print "Company:",data[16][6]
        
        elif ID in data[17]:
            print "Please Wait Your data is Searching from database"
            time.sleep(5)
            #print data[17]
            
        #if you want to part by part result and design you have to write code like below...    
            print "Name:",data[17][1]
            print "Email:",data[17][2]
            print "Salary:",data[17][3]
            print "Phone NO:",data[17][4]
            print "State:",data[17][5]
            print "Company:",data[17][6]
            
            
    else:
        print "Plesae Wait Checking ......"
        time.sleep(5)
        print"We Couldn't Find Your Id from our Database please give Correct Id"  
        

    

    
    
    





