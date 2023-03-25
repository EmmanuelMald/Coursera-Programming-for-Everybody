"""
Created by Emmanuel Amador Maldonado

On 20/November/2020
"""

#ASSIGNMENT 8.4
#Open the file romeo.txt and read it line by line.
#For each line, split into a list of words using the split() 
#method. The program should build a list of words.
#For each word on each line check to see if the word is
#already in the list and if not append it to the list.
#When the program completes, sort and print the resulting
#words in alphabetical order.
l2=[]
try:
    file=open(input("Enter file name: "),"r")
    for line in file:
        l=line.split()
        for word in l:
            if word not in l2:
                l2.append(word)
    l2.sort()
    print(l2)
except:
    print("File wasn't found, try again")
#IT WORKS!!!
#%%
 
#ASSIGNMENT 8.5
#Open the file mbox-short.txt and read it line by line.
#When you find a line that starts with "From " like the 
#following line:
    # From Stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#You will parse the From line using split() and print out 
#the second word in the line (i.e, the entire adress)
# then print count a count at the end
# Make sure not include the lines that start with "From:"
    # print("There were", count, "lines in the file with From as the first word")
count=0
try: 
    file=open(input("Enter file name "),"r")
    for line in file:
        if line.startswith("From "):
            l2=line.split()
            print(l2[1])
            count+=1
    print("There were", count, "lines in the file with From as the first word")
except:
    print("File wasn't found, try again")
#IT WORKS!!!
    