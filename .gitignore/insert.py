import MySQLdb
import mysql.connector
def insert_data_into_database(ID=raw_input("Enter Your ID:"),
                              NAME=raw_input("Enter Your Name:"),
                              EMAIL=raw_input("Enter Your Email here:"),
                              SALARY=raw_input("Enter Your Salary:"),
                              PHONE=raw_input("Enter Your Phone Number Here:"),
                              ADDRESS=raw_input("Enter Your Address Here:")):
    
                              
  
   
    SQL=("insert into user values("+ID+",'"+NAME+"','"+EMAIL+"',"+SALARY+","+PHONE+",'"+ADDRESS+"')")
    conn=mysql.connector.connect(host="127.0.0.1",  port=3036,  user="root" ,  passed="hussain", db="user")
    cursor=conn.cursor()
    cursor.execute(SQL)
    print "One Row inserted sucessfully"
    conn.commit()
    conn.close()
    cursor.close()
    return "One Row inserted sucessfully"
