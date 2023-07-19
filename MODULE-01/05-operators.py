# operators in python 

# important>> there is no long and double in python and char also

'''
arithmetic operators 
+  addition
-  substraction
*  multiply
=  value assign
/  division 

comparison operators >> boolean answers >> true or false 
==  comparison operator
>  greater than
<  less than
or || either
and && must means both compulsory
%  modulus operator >> remainder of division
**  power operator >> a**b >> a raised to b
'''

a=3
b=44
a+b
print((a+b),a/b,a-b,a*b)

# division(/) in python
'''two types;
1. float division [/]
2. integer division [//]
'''
# float division
a=10
b=23
print(a/b) #>> 0.4347826 means float number

# int division 
a=20
b=9
print(a//b) #>> 2

# divide exception 
a=20
b=int(input("enter number\n"))
#if b=0 then exception will occur (zero division error)
print(a/b)

# comparisons
c=20 
d=22
print(c>d) #false

print(c%d) #remainder
'''
# ----------------------------
Python provides a wide range of operators that allow you to perform various operations on values and variables. Here are the different types of operators in Python:

1. Arithmetic Operators:
   - Addition: +
   - Subtraction: -
   - Multiplication: *
   - Division: /
   - Floor Division: //
   - Modulus: %
   - Exponentiation: **

2. Assignment Operators:
   - Assignment: =
   - Addition Assignment: +=
   - Subtraction Assignment: -=
   - Multiplication Assignment: *=
   - Division Assignment: /=
   - Modulus Assignment: %=
   - Exponentiation Assignment: **=
   - Floor Division Assignment: //=

3. Comparison Operators:
   - Equal to: ==
   - Not equal to: !=
   - Greater than: >
   - Less than: <
   - Greater than or equal to: >=
   - Less than or equal to: <=

4. Logical Operators:
   - Logical AND: and
   - Logical OR: or
   - Logical NOT: not

5. Bitwise Operators:
   - Bitwise AND: &
   - Bitwise OR: |
   - Bitwise XOR: ^
   - Bitwise NOT: ~
   - Left Shift: <<
   - Right Shift: >>

6. Membership Operators:
   - in: Returns True if a value is found in a sequence.
   - not in: Returns True if a value is not found in a sequence.

7. Identity Operators:
   - is: Returns True if two variables refer to the same object.
   - is not: Returns True if two variables refer to different objects.

These operators allow you to perform mathematical calculations, assign values, compare values, combine logical conditions, manipulate bits, and check membership and identity relationships between values.
'''
# Here's an example that demonstrates some of these operators:

a = 10
b = 5

# Arithmetic operators
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division

# Comparison operators
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to

# Logical operators
x = True
y = False
print(x and y)  # Logical AND
print(x or y)  # Logical OR
print(not x)  # Logical NOT


'''
These are the basic operators available in Python. Understanding and utilizing these operators will enable you to perform a wide range of operations in your Python programs.
# ----------------------------'''