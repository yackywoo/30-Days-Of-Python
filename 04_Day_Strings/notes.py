line1 = "hello my name is \'peter\' \nhello i am \"peter\" "
#need \' \' operators to use single quotations within string
#need \" \" operators to use double quotations within string
# \n = new line
# \t = tab (8 spaces)
print(line1)

name = "peter"
hobby = "cooking"
food = "burgers"
goodorbad = "good"
my_sent = "hello my name is {}, i enjoy {} and eating {}. have a {} day!".format(name, hobby, food, goodorbad) #kind of like printf but within the string using format method
print(my_sent)

#reversing the goodorbad day variable
if goodorbad == "good" : goodorbad = "bad"
else : goodorbad = "good"

#can print the formatted string directly without using variable
print("hello, i am not {}, i dont like {} and hate eating {} have a {} day!".format(name, hobby, food, goodorbad))

radius = 1
pi = 3.14
print("C: {}\nA: {:.2f}".format(radius * 2 * pi, radius ** 2 * pi)) #rounding area to 2 decimals

word = "computerscience"
sci_len = len("science")
print(word[:-sci_len]) #starting from beginning ending at : word.length - len(science) = 15 - 7 = 8 so [0:8]
print(word[0:8])
print(word[-sci_len:]) #starting from 8th index, get rest of string
print(word[8:])

print(word[::-1]) ##reverse a word

print(word[::2]) #skip every other character

print(word.capitalize()) #only first char is capitalized

print(word.endswith("asd")) #false
print(word.endswith("ence")) #true

substr = "e"
print(word.split(substr)) #split removes the substr if exists

word = "computer science"
word = word.title()
print(word)
print(word.swapcase())

#=====================
print(word.split())

q = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(q.split(", "))

q2 = 'You cannot end a sentence with because because because is a conjunction'
print(q2.index("because"))
print(q2.rindex("because"))
print(q2[q2.index("because"):])
print(q2[q2.rindex("because"):])
q21 = q2[:q2.index("because")]
q22 = q2[q2.rindex("because") + len("because "):]
print(q21 + q22)

m = '   Coding For All      '
print(m)
index1 = m.index("C")
index2 = m.rindex("l")
print(m[index1:index2+1])
print(m.format())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

p = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
pp = "][".join(p)
ppp = "["
pp += "]"
print(ppp + pp)

'''
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
'''

print("Name\tAge\tCountry\tCity")
print("Peter\t43\tUSA\tRhode Island")

a = 8
b = 6

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b :.2f}") #rouding to 2 decimal places here
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")

radius = 10
pi = 3.14
print(f"radius = {radius}")
print(f"area = {pi} * radius ** 2")
print(f"The area of a cricle with the radius {radius} is {int(radius ** 2 * pi)} meters squared.")