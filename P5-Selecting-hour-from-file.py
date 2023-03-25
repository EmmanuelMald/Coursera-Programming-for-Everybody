# ASSIGNMENT 10.2
# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out
# from the "From " line by finding the time and then
# splitting the string a second time using a colon.
# From stephen.marquuard@utc.ac.za Sat Jan 5 09:14:16 2008
# Once yoy have accumulated the counts for each hour
# print out the counts, sorted by hour as shown below
dic = {}
lst = []
try:
    file = open(input("Enter file name: "), "r") # se abre el archivo
    for line in file: #lee línea por línea
        if "From " in line: #Encuentra la línea donde tiene las horas
            words = line.split() # Separa las palabras por espacios
            hour = words.split(":") #Separa las horas, minutos y segundos
            print(hour)
            dic[hour[0]] = dic.get(hour[0], 0)+1
    for k, v in dic.items():
        lst.append((k, v))
    lst = sorted(lst)
    print(lst)
except:
    print("File wasn't found, try again")
