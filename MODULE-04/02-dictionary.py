# what is dictionart in python?

# dictionary is basically >>
# built in mapping type 
# it maps keys to values
# it provides useful way to store data
# contains key value pair

# what are dictionary functions? update, delete,clear...

# it is possible that dictionary another dictionary
# like list inside list 

# important- there is no indexing in Dictionary
d = {"name":["Jackson", "Messi"], "followers":666666, "online":True, 34:{"age": 45}}

"""
keys : name, followers, online, 34

values: jackson 666666 True id

"""

for i in d.keys():
    print(d[i])

print(d)
print(type(d))

# print(d.keys())

# print(d.values())

# print(d["online"]) #present then True else key error
# print(d[34])

# print(type(d["name"]))

# print(d[34]["age"]) #dict in dict example

d[True] = 'Football'
print(d["name"][1]+" hii") #name is key and this is dict in dict so value is a list so messi would be accessed by index 1 of list using [1]

# dictionary function 
d.update({"hobby":"painting"})
print(d)

# del d["name"][0]
# print(d)

# clearing a dict 
# d.clear()
# print(d)

# def ping(n):
#     if(n%2==0):
#         return True

#     return False    

# ------------------------ #
# def printing(num):
#     val = ping(num)
#     if (val==True):
#         print("Number is Even")
#     else:
#         print("Number is odd")    


# number = int(input())
# printing(number)        
