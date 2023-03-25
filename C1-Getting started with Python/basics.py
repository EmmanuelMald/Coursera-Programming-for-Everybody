# Created by Emmanuel Amador Maldonado
# This is the basics of python
# Numeric ezpressions.
"""
    Operator        Operation
       +            addition
       -            substraction
       *            multiplication
       /            division
       **           power
       %            remainder
       
"""
x=2
x+=2 # its the same as x=x+2
print(x)
y=3
print(x+y, x%y, x/y, x**x)
print(f"The variable x has the value {x}") # Allows us to print a message with variable values
print("The variable x has the value ", x) #Another way to use print

"""
    Variable types
    
        int             Gives the integer of a number
        float           Gives a number with decimals
        String          Gives a combination of characters, can be numbers or the 
"""

"""
User input

input("Message to display")  It returns a string 
can be changed into a int, float with
int(input())
float(input())

"""


"""
Functions, codes that can be used in many places of the code to reduce the length 
of a code when that part repeats many times.

def name_of_function(input1, input2...):
    code
    return 
"""
def suma(a,b):
    return a +b

print(suma(2,3))

def sum_sub(a,b):
    c=a+b
    d=a-b
    return c,d

a=2
b=3
j,k = sum_sub(a,b)
print(f"The solution of {a} + {b} = {j}")
print(f"The solution of {a} - {b} = {k}")

#You can also write

print(f"The solution of {a} + {b} = {j} \nThe solution of {a} - {b} = {k}")

def hi():
    print("Hi")
    return

print(hi())