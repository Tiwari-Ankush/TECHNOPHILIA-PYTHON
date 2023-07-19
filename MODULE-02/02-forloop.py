# for loops in python>>>
# theory >>

# example of for loop
# for numbers we use range inbuilt function
# from 0 to futher, if we not write 0 then also it takes 0 as a starting index of a range
for i in range(1,51): #here 1 to 51 means 1 to 50 only
    # >>>>> range can be written in mathematical form be like- [1,51)
    print("ankush ",i**2)
    print("tiwari ",i)
    i=i+1

# introducing a difference concept inside a range function of for loop
for i in range (1,90,4): #here 4 is a difference, or we can say       that interval or period
    print(i)
#if  diff is not given, means 3rd parameter is not given then, by default it takes 1 as a increment value or difference


#list object is not callable >>  so error
'''
listt=[12,22,33,44,44,55,50]
i=0
for i in listt():
    print(listt[i])
    i+=1
'''

# buttt >>>
i=0
for i in [12,22,33,44,44,55,50]:
    print([i])
    i+=1

# similarly >>>
print("\n")
for x in "ankush tiwari bro":
    if x==" ":
        continue
    print(x, "", "</>")
    i=i+1
print("\n")

#printing the sum of first 50 numbers
#static
sum=0
for i in range(51):
    sum=sum+i
print(sum)

#dynamic
n=int(input("enter the number"))
summ=0
for i in range (0,n+1):
    summ=summ+i
print(summ)
print("\n")

# for printing the cube
sumc=0
for i in range (1,16):
    print("cube of ",i," ","is >> ",i**3)
    sumc=sumc+(i**3)
print("\n Sum of all above cubes is ->")
print("  ",sumc)

# as like that >>>>
for x in "</> TIWARI ANKUSH BRO </>":
    if x==" ":
        continue
    print(x,"",end="")
    i=i+1



