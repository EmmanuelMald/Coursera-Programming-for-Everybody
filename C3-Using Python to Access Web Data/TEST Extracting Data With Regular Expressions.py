#Extracting Data With Regular Expressions TEST
# extract the numbers and give the sum 
import re 
sum=0
file=open("actualdata.txt")
for line in file: #open each line of the text
    if re.search("[0-9]+", line): #if there is a number in the line
        s=re.findall("[0-9]+", line) #save the numbers in a list of strings
        for n in range(len(s)): #gives the list of the length of the list
            sum=sum+int(s[n]) #sum the value in integer value of the string
            
print(sum)
    