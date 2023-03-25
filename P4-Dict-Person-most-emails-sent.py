#ASSINGMENT 9.4
#Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail
#messages. The program looks for "From " lines and takes 
#the second word of those lines as the person who sent
#the mail. The program creates a Python dictionary that maps
#the sender's mail address to a count of the number of times
#they appear in the file. After the dictionary is produced
#the program reads trough the dictionary using a maximun loop
#to find the most prolific committer



persons={}
file = open(input("Enter the name file: "),"r")
for line in file:
    if "From" in line: 
        words=line.split()
        if words[1] not in persons:
            persons[words[1]] = persons.get(words[1],1)
        else:
            persons[words[1]] = persons.get(words[1])+1
for key in persons:
    print(f"name: {key} \t number of emails sent: {persons[key]}")
    
print(f"The person who sent the highest number of emails is {max(persons, key=persons.get)} with {max(persons.values())} emails")
            