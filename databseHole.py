import json
import MySQLdb
while True:
    SQL=raw_input(str("Enter Your Query:"))
    Con = MySQLdb.Connect(host="127.0.0.1", port=3306, user="root", passwd="hussain", db="user")
    cursor=Con.cursor()
    cursor.execute(SQL)
    data=cursor.fetchall()
    Con.commit()
    #json_output=json.dumps(data)
    #print json_output
    for r in data:
        print r



        
    
