"""
Created on Thu Nov 19 19:13:37 2020

@author: Emmanuel Amador Maldonado
"""

# COLLECTIONS
# LIST
#A list is a sort of collection
# A collection allow is to put many  values in a single
# 'variable'
# A list can be rewritten or even being expanded or contracted
# you can combine different types of variables in a list
# strings are not mutable
#the function ranfe returns a list of numbers that range
#from zero to one less than the parameter

list=[1,2,"Hiii", 1.4]
print(list)
#also you can know the length of a list
print(len(list))
#or you can know the length of a string inside
print(len(list[2]))
#u can change a part of the list
list[2]="this change"
print(list)
#the function range make a list in sequence
a=range(4)
print(a)
for i in range(10):
    print(i) #it shows the from 0 to (n-1) parameters
#as you can concatenate strings, you can  also concatenate list
a=[1,2,3]
b=['hi, im new',4,5,6]
c=a+b
print(c)
#we can slicing trough the list also, remember, the last
# is up but not included
print(c[2:-1])
#if u wanna include the last last term, just use
print(c[2:]) #instead of print(c[2:-1])

#if we create an empty list
l2=[]
#and we wanna put a new element in, we use the function

# nameofthelist.append(what you want to put)
l2.append("this is the first element")
print(l2)
l2.append(342)
print(l2)
# as u can see, the element u introduce apper at the last of the list
# FIRST IN FIRST OUT
#also you can delete part of the list with remove
l2.remove(342)
print(l2)
#if you want to look for a specific part in a string
# or a part in a list, you can use the function in
print(20 in list)
# max(lista o cadena) gives the maximun value of the string 
# min(lista o cadena) gives the minimun value of the string 
# sum (lista) gives the sum of all the collection
#con nombredelalista.sort() it gets sorted from min to max value


# con nombredelacadena.split(), it creates a list that split the words it has into and separete them in a list
s1="Esto es una cadena"
listas1=s1.split()
print(listas1) # it gives a list with the separate values 
# No matter how much blank space does it has, always splits different character to the blank space
s2= "hola                como       estas?"
print(s2.split()) #it only separates the words.
#also you can choose the character wich will be splitted.
l3="Esto.es.una.cadena"
print(l3.split(".")) #separates list into (Esto es una cadena)
f=["Josep","Glenn","Sally"]
f.sort()
print(f[0])


