import json
class Main(dict):
    def __init__(self):
        self=dict()
    def Create_dict(self,key,value):
        self[key]=value


Dict=[]        
new_dict=Main()
new_dict.Create_dict("Name","Moshabbar")
new_dict.Create_dict("Age",28)
new_dict.Create_dict("Sex","Male")
#print new_dict
json_output=json.dumps(new_dict)
print json_output
Dict.append(json_output)
print Dict

if __name__=="__main__":
    Main()

    
    
    
    
    
ANOTHER WAY TO DO THIS CODING.......  

import json
key=raw_input("Enter Your Key:")
value=raw_input("Enter Your Value:")
class Main(dict):
    def __init__(self):
        self=dict()
    def Create_dict(self,key,value):
        self[key]=value


Dict=[]        
new_dict=Main()
new_dict.Create_dict(key,value)

#print new_dict
json_output=json.dumps(new_dict)
print json_output
Dict.append(json_output)
print Dict

if __name__=="__main__":
    Main()

