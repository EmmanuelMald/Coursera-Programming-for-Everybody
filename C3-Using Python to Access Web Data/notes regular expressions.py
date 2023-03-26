#NOTES COURSE 3, WEEK 1
#REGULAR EXPRESSIONS
#It's a more intelligent form of search
#for information
#it's very powerful and quite cryptic
#Are a language into themselves
# it will reduce the code
#you program with characters
# ^  Matches the beginning of a line
# $ Matches the end of the line
# . Matches a character
# \s Matches withespace
# \S Matches any non-whitespace character
# * Repeats a character zero or more times
# *? Repeats a character zero or more times (non-greedy)
# + Repeats a character one or more times
# +? Repeats a character one or more times (non-greedy)
# [aeiou] Matches a single character in the listed set
# [^XYZ] Matches a single character not in the listed set
# [a-z0-9] The set of characters can include a range
# ( Indicates where string extraction is to start
# ) Indicates where string extraction is to end

#to use regular expressions on python we
# must include the library "import re"

# we can use re.search() to see if a string 
# matches a regular expression, similar tu using find()

# we can use re.findall() to extract portions of a string
# that match your regular expression, similar to a 
#combination of find() and slicing var[5:10]

#Example using the library re

import re
print("using regular expressions: \n\n")
hand=open("mbox-short.txt","r", encoding= "utf-8")
for line in hand:
    line=line.rstrip() #cut the righ space at the end of the line
    if re.search("From: ", line): #re.seach("words you want",string where research)
        print(line)
#%%
#Example without using the library to do the same
print('\n\nnot using regular expressions\n\n')
hand=open("mbox-short.txt","r", encoding= "utf-8")
for line in hand:
    line=line.rstrip()
    if "From: " in line:
        print(line)
#%%
#another example 
print("\n Not using regular expressions\n\n")
hand=open("mbox-short.txt","r", encoding= "utf-8")
for line in hand:
    line=line.rstrip()
    if line.startswith("From: "):
        print(line)
#%%
print("\n\n Using regular expressions")
hand=open("mbox-short.txt","r", encoding= "utf-8")
for line in hand:
    line=line.rstrip()
    if re.search("^From: ",line): #if From is at the beginning of the string...
        print(line)
#Wild-Card characters
#The dot character amtches any character
# if you add the asterisk character, the character is "any number of times"
# example
#%%
hand=open("mbox-short.txt")
for line in hand:
    line=line.rstrip()
    if re.search("^X.*:", line): #if X is at the beginning of the string, followed by any character any times and then followed by ":"
        print(line)
#%%
hand=open("mbox-short.txt")
for line in hand:
    line=line.rstrip()
    if re.search("^X-\S+:", line): #if X is at the beginning of the string, followed by "-" followed by a character that is not a whitespace one or more times, and followed by ":"
        print(line)
