#dictionaries
# is a data structure, it allow us to "label" a different
# type of values, in dictionaries, the label must not repeat
# it does not have an order
#to write a dictionary, u must put a word in, and the 
# dictionary will give you a value out
# we define a dictionary with dict(), or with {}
d1= dict()   #define the dictionary dict()
d1['money']=12 #first u must put the word in, and then
                  # the word out
d1["candy"]=3
d1[1]=4
d1["A"]="holaaaa"
print(d1)
# the types of inputs and outputs can be of any type of value
#we can change the inputs and outputs too
d1[1]="Esto cambio"
print(d1)
#to look for a value, we must just put the input word
print(d1["candy"])
#we can also define a dict() with inputs since the beginning
#dictionaries are define with {}, list with []
d2={"input1":"output1", "input2": 2, 3:"output3"}
d3={} #create an empty dictionary
print(d2)
#we can count how many times a word appears in a text or something
d4={"word1":1,"word2":1}
#the key here is that when we look for a word, the value changes
d4["word1"]=d4["word1"]+1
print(d4)
#thats how our brain works!!
list1=["A","B","C","A","A"] #counts how many times sort types of data appears in an arrangement
d5={"C":1}
for x in list1:
    if x not in d5:
        d5[x]=1
    else:
        d5[x]=d5[x]+1
print(d5)
#to see if a key is already in a dictionary, we use the function namedict.get("input", output IF NOT EXIST)
print(d5.get("A"))# if it exist, it return the output value
print(d5.get("D"))#if it doesnt exist, it return None
#if you want another value instead of None, you added at the end
print(d5.get("D","False")) #5 not exist, return False
print(d5.get("D",0)) #5 not exist, return 0
# so we can reewrite the code above
list1=["A","B","C","A","A"] #counts how many times sort types of data appears in an arrangement
d5={"C":1}
for x in list1:
    d5[x]=d5.get(x,0)+1
print(d5)
#DICTIONARIES AND FILES
# we can use for to go through dictionaries
#the for gives us the key, we have to put them in
# in order to give us the output value
count={"A":4,"B":5}
for key in count:
    print(key)
    print(count[key])
#if we have a file and we would like to know all the times
#each word appers in there, we can do the next:
string="Hola, este es una cadena que debería de repetir, hola, hola, hola, repetir"
words=string.split()
dic={}
for word in words:
    dic[word]=dic.get(word,0)+1 #we introduce a value in the dictionary
print(dic)
#if we want to transform a dictionary into a list
# we see that if we make lis(dict), the list will
# give us the input of the dictionary, not the outputs

#If we want only the keys, we can use the function
# namedictionary.keys()
# manedictionary.values() if we want the values
#namedictionary.items() list of tuples with keys and values
print(dic.keys()) #show us a list of keys
print(dic.values()) #show us a list of values
print()
# it also can use for with two iterator
for key, value in dic.items():
    print(key, value)

