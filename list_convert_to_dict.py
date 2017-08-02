# How to add two list as a Dictionary format
k=["Name","Age","sex","Address","Salary"]
v=["Moshabbar",27,"Male","Hyderabad",41000]

# Make it As a Dictionary Format
dict_format=dict(zip(k,v))
print dict_format

# O/P:{'Salary': 23000, 'Age': 23, 'Name': 'Mosh', 'Sex': 'Male'}

# i Want To print like keys and values:  name:----,age:---- like

new_value=dict_format.iteritems()
for x,y in new_value:
    print x,y
