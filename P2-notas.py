#SEMANA 3, CURSO 2
#FILES
# Para abrir un archivo de texto externo se usa open()
# texto=open('nombre del archivo.txt','modo de abrir')
# modo de abrir puede ser 'r'- solo lectura
# modo de escritura 'w'- solo escritura
#si solo se pone open ('nombre.txt'), se ejecutará en modo
#   lectura
#salto de línea funciona como un solo caracter '\n'
#cada línea del texto lo toma como una cadena
#ejemplo
file=open("texto.txt") # abre el archivo
for linea in file:# toma cada salto de linea como una cadena nueva
    print(linea)
#ttambién se puede leer todo el texto como una sola cadena
# si se usa la función variable.read
#rstrip() permite quitar el salto de línea de una cadena, así
# ya no se repite el doble espacio
print ("\nDe nuevo, usando la función rstrip\n")
file=open("texto.txt")
for linea in file:
    linea=linea.strip()#quita el \n de la cadena
    print(linea)#print agrega un \n al final siempre

#nota, para volver a utilizar el archivo abierto,
#se tiene que volver a mandar abrir, una vez que se lee
#completo, parece que se cierra

#también se puede leer el texto completo como si fuera una
# sola cadena, utilizando .read()
#ejemplo
print ("también puede leerse el texto de corrido, como una sola cadena\n")
file=open("texto.txt")
file=file.read()
print(file)
# la función quit() termina el programa cuando ya no 
#tiene sentido continuar
    
    
