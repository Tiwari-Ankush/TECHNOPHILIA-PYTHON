# why list in python?
# >>
# we can store multiple data type in list !

# student1 = "Ankush"
# Student2 = "salman"
# student3 = "shahrukh"
# .
# .
# .
# student60 = "angela"

# above formart is diff, so we use a list 
# ls = ["Ankush", "salman", "shahrukh", . . . . . "angela"]

ls = ["name", True , 66.7, 23]
print(ls)
print(type(ls))

ls = ["Name", ["place", 70], True]
print(ls)


# what is indexing in list?  and how it is possible in python list? positive and negative indexing?
# >>

"""
indexing in list >> 
ls = ["Ankush", "salman", "shahrukh", "angela", "Akanshu", "Neeraj", "Vinay"]

        0          1        2          3            4         5         6
        -7        -6       -5         -4           -3        -2        -1

"""        
ls = [False, "Ankush", "salman", "Kunaaal", 99.9, "angela", "Akanshu", True, "Neeraj", 78, "Vinay", 45, "Saksham"]

# print(ls[2])
# print(ls[-2])
# print(ls[7])
# print(ls[-6])

# print(ls[4], ls[-4])

# print(ls[10], ls[6])
# print(ls)
# ls[3] = "shahrukh"
# print(ls)

# ls[-6] = "Thor"


# various operations on list?
# >>


# if data is of same type in list then sorting is possible else none 
# ls.sort()
# print(ls)

# ls.append(999)
# print(ls)

# ls.insert(2,"Cheetah")
# print(ls)

# del(ls[-9])
# print(ls)

# print(ls[3:9])
# print(ls[3:])

# print(ls[:9])

# print(ls[:])

ls = [1,3,5,56,86,23,898,0,27,90]

print(ls[:]) #it prints all the list items
# count = 0
# for i in ls:
#     count+=1

# print(count)    

# for i in range(len(ls)):
#     print(ls[i])

# maximum = -1
# for i in ls:
#     if maximum < i:
#         maximum = i

# print(maximum)        
# print(max(ls))


# for i in ls:
#     print(ls)

# for i in ls:
#     if i < ls:
#         print(i)
"""
10 times list print -> Shiyan, shahrukh, Omesh, salman, Meghna, 

values of i --> Shiyan, 

"""
