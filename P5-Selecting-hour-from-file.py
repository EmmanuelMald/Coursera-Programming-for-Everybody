# ASSIGNMENT 10.2
#Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for 
# each of the messages. You can pull the hour out
#from the "From " line by finding the time and then
#splittiong the string a second time using a colon.
#From stephen.marquuard@utc.ac.za Sat Jan 5 09:14:16 2008
#Once yoy have accumulated the counts for each hour
#print out the counts, sorted by hour as shown below
dic={}
lst=[]

file=open(input("Enter file name: "), "r", encoding = "utf-8") # open the given file
for line in file:       # open line by line
    if "From " in line:  # if "From " is written in line
        words=line.split()   #separate each words that are not spaces
        hour=words[5].split(":") #separete the hour, minutes and seconds
        dic[hour[0]]=dic.get(hour[0],0)+1 #save in a dictionay just the hour
for k, v in dic.items(): #save in a list a tuple with the hour and the histogram
    lst.append((k,v)) 
lst=sorted(lst) #order the list of tuples from smallest to largest 
for x in lst: #open the list, and give me each tuple
    print(x[0],x[1]) #print the values of the tuple
    
#IT WORKS!!!
