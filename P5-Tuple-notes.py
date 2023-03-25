#NOTES WEEK 6, COURSE 2
# Tuples
# Are list that are unmutable
#it can be defined with parenthesis.
#once you create it, you can't modify it in anyway, you
#cant introduce, delete or change any value in there
x=("hola",124, [1,2,3]) #this is a tuple
print(x)
print(x[1:]) #you can slice trough the tuple
for y in x:
    print(y)
#you cant use x.sort(), tuple.append(), tupple.reverse()
    #dir(list, or dictionary) show us all the functions
    #that works with that type of data structure
#tuple assignment
(a,b)=(4,"hola") #you cant change the value of a
print(a,b)
# the items() in dictionaries return a list of tuples(key,value)
#tuples are comparable, and starts with the first element
print((0,1,2)<(2,3,2))
print((0,1,2)<(0,2,3))
print((0,1,2)<(0,1,2))
#if we use sorted(tuples or dicts.items()), we can order the dictionary in 
# another variable, it will be orderer in key order.
# sort by value
list1=[]
c={"a":10,"b":3,"c":5}
for k, v in c.items():
    list1.append((v,k)) #we have a list with tuples
print(list1)
list1=sorted(list1, reverse=True) # biggest to smallest
print(list1)
list1=sorted(list1, reverse=False) #smallest to biggest
print(list1)
y=(10,-5,30)
