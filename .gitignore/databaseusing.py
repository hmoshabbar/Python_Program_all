#import json
import MySQLdb
SQL="select * from user"
Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="hussain", db="user")
cursor=Con.cursor()
cursor.execute(SQL)
data=cursor.fetchall()
Con.commit()
#json_output=json.dumps(data)
#print data
ID=int(input("Enter Your ID:"))
if ID in data[0]:
    print data[0]
elif ID in data[1]:
    print data[1]
elif ID in data[2]:
    print data[2]
elif ID in data[3]:
    print data[3]
elif ID in data[4]:
    print data[4]
elif ID in data[5]:
    print data[5]
elif ID in data[6]:
    print data[6]
elif ID in data[7]:
    print data[7]
elif ID in data[8]:
    print data[8]
elif ID in data[9]:
    print data[9]
elif ID in data[10]:
    print data[10]
elif ID in data[11]:
    print data[11]
elif ID in data[12]:
    print data[12]
elif ID in data[13]:
    print data[13]
elif ID in data[14]:
    print data[14]
elif ID in data[15]:
    print data[15]
elif ID in data[16]:
    print data[16]
elif ID in data[17]:
    print data[17]
else:
    print "Your is not in our Database please Check Aagin..."
    
    
    





