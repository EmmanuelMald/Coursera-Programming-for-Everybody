#semana 1, curso 2
#programa python
#WRITE CODE USING find() to extract the number at the end of the line 
#below, convert it to a float variable and print it
text="X-DSPAM-Confidence:    0.8475"
start=text.find('.')
number=float(text[start-1:])
print(number) #FUNCIONAAAAA!!!
