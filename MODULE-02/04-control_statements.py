# loop control statements
'''
>> used when full loop isnot needed
>> basically used to terminate loop permanently
>> there are two statements
   1.break statement
   2.continue statement
   3.pass statement

que >> what is goto statement in python ??


'''

'''
break statement:>>>
The "break" statement is used to exit a loop prematurely. It terminates the loop and transfers control to the statement immediately following the loop.

continue statement:>>>
The "continue" statement is used to skip the remaining code in a loop iteration and move to the next iteration. It returns the control to the beginning of the loop.

pass statement:>>>
The "pass" statement is a placeholder that does nothing. It is often used as a placeholder for code that will be added later or to create empty classes, functions, or loops.

'''
#1.break== immediate terminates loop
#2.continue == immediately, terminates current iteration,and jumps to the next iteration, not a loop

# 1. BREAK STMT 
for i in range(50):
    if(i==25):
        break #terminates the loop at value 25
    print(i)

# 2. CONTINUE STMT
for i in range(50):
    if(i==25):
        continue #terminate the particular / current iteration
    print(i)


for i in range (15):
    for j in range (15):
        print("ankush")
        i=i+1
    print("tiwari")
    j = j+1