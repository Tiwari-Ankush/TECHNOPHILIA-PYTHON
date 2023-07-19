# conditional statements in python?
# theory>>
'''
if statement:

The "if" statement is used to check a condition and execute a block of code if the condition is true.
if-else statement:

The "if-else" statement extends the "if" statement by providing an alternative block of code to execute if the condition is false.
if-elif-else statement:

The "if-elif-else" statement allows you to check multiple conditions sequentially. It provides a series of "elif" (short for "else if") blocks that are evaluated one by one until a condition is true. If none of the conditions are true, the "else" block is executed.
'''

# if-elif-else Conditional-ladder 
a=int(input("enter number\n"))
if(25<=a<=90):
    print("you choose the right number")
elif(0<=a<=10):
    print("you have chosen the number betn 0 to 10")
else:
    print("you are going outof bound")