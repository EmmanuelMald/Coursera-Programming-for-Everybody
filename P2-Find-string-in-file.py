# Assignment 7.2
#Write a program that prompts for a file name, then opens
#that file and reads trough the file, looking for lines of
#the form
#X-DSPAM-Confidence:  0.08475
#Count the lines and extract the floating point values from
#each lines and compute the average of those values
#and produce and output as shown below. Do not use the
#sum() function or a variable named sum in your solution
#when testing below, enter mbox.short.txt


s=0
count=0
try:
    file=open(input("Write the file name: ")) #abre el archivo
    for line in file:               # abre cada linea del archivo
        if "X-DSPAM-Confidence:" in line: #busca dentro de esa línea la frase en verde
            pos=line.find(".") #encuentra la posición del punto decimal del número
            data=float(line[pos-1:pos+6]) #guarda el número 
            s=s+data #suma el número
            count +=1 #cuenta el número de veces que se encontró esa parte del programa
    print("Average spam confidence: ",s/count)
except:
    print("No se encontró el archivo")

#  FUNCIONA CORRECTAMENTE

#Assignment 7.2
#Write a program that prompts for a file name, then opens
#that file and reads through the file, and print contents of the
#file in upper case. Use the file words.txt to produce the output below.  

try:
    file=open(input("Write the file name"))
    for line in file:
        line=line.upper()
        print(line)
except:
    print("El archivo no se encontró")
s="Banana"
s[0]="b"
print(s)