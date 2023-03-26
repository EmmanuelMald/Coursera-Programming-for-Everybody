#Notes EXTRACTING DATA
# we use the "re" library
# the function re.findall("characters u want",string where search)
1# re.findall gives a list with all the characters that fix with your research
import re
file="Im 20 years old, my sister is 15, and my dog is 6"
y=re.findall("[0-9]+", file) #find one or more character with digits
print(y) 
#WARNING THE (*and +) push outward in both directions (greedy)
# to match the largest possible string
# example
x="From: Using the: characters"
y=re.findall("^F.+:",x)
print(y) # it will return "From: Using the:" it prefers the largest string
# and not just "From:"
# but there's a way to fix this
#we use "+? or *?" to stop at the first character that matches
# it prefer the smallest string
x="From: Using the: characters"
y=re.findall("^F.+?:",x) #stops the string in the first ":" that is found
print(y)

#We can refine our match for re.findall() and separately
# determine which portion of the match is to be extracted
# by using parenthesis
s="From emmanuel_mald@hotmail.com at 10 pm"
y=re.findall("\S+@\S+",s) #look for any non white character followed by @ and stops in a white character
print(y)
#Parenthesis are not part of the match- but they tell where to start and stop what string for extract
y=re.findall("^From (\S+@\S+)",s)
print(y)
s="From stephen.marquard@utc.ac.za Sat Jan 5"
y=re.findall("@([^ ]*)",s) #search for the @ but give me all the non white space characters, stops in the first white space
print(y)
y=re.findall("@(.+?\s)",s) #this form includes the space at the end
y=[y[0].rstrip()]
print(y)  
# so y=re.findall("@([^ ]*)",s) this way is way too easier than y=re.findall("@(.+?\s)",s), y=[y[].rstrip()] this form
# [^ADF] gives all the characters that is not in the square parenthesis
