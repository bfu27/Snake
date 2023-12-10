import random

msg = "You got this <3"
print(msg)

# REMEMBER: exit() for inside the terminal
# REMEMBER: Intentation is import! (spaces/allignment)

if 5 > 2:
    print("WOW")
    print("This will work")

print("This is new.")

a = 10
b = "Maybe"

i = 1

while i < a:
    if i % 2 == 0:
        print("next.")
    i = i + 1
print(b)

# Specify the type like this:

a = int(3)

# Get the type with the function "type"

print(type(a))
print(type(b))

# REMEMBER: names are case sensitive so a != A

x, y, z = a, b, i

print(y)

#Lists, kind of?

veggies = ["tomato", "potato", "onion"]
x, y, z = veggies
print(y)

# Printing print(x,y) is the same as print(x+y) but in the second instance, the var have to have the same type

# FUNCTIONS

def awesomeness():
# Right now x is local but we can add "global x" instead of "x" to make it a global variable
    x = "bfu27"
    print(x + " is awesome")

awesomeness()

def general_awesomeness(x):
    print(x + " is awesome")

y = "bfu27"
general_awesomeness(y)


# Data types: complex numbers!

complex_number = 1j

def type_of(x):
    print(type(x))

type_of(complex_number)

# Set and frozenset : probably mutable and immutable sets?

# REMINDER: no random() function but you can use the random module to generate a random number from a given range
print(random.randrange(1,100))

# 3 quotation marks ("""/''') can be used for creating a multi-line string
# Line breaks occur in the same spots as the given format

# REMINDER: Any string in an array and can be used accordingly
# REMINDER: First position starts at 0
a = "Today is sunny."
print(a[2])

# LOOPS

for x in "awesome":
    print(x)

print(len(a))

# Keyword "in" can be used to check if a string is part of another string

print("today" in a) #FALSE
print("Today" in a) #TRUE

# Similarly, "not in" can be used to check the absence of a string in another string

print("today" not in a) #TRUE
print("Today" not in a) #FALSE

# Slicing strings

print(a[0:5]) #Today
print(a[:5])  #"Today", slicing from the start
print(a[5:]) #slicing from the end, " is sunny."

# NEGATIVE INDEX: Use negative indexes to start the slice from the end of the string

print(a[-6:-1]) #sunny

# Modifying strings is also possible

print(a.upper())
print(a.lower())
print(a.strip()) #removes white spaces from the beginning or the end
print(a.replace("y", "i")) #Todai is sunni.
print(a.split(" ")) #["Today","is","sunny."]

#Concatenation

a = "Today is"
b = "cold"
print(a + " " + b)

text = "My coffee is " + b
print(text) 

text = "My age is {}"
print(text.format(22))

# Unlimited number of arguments
text = "I have {} euros and I owe you {} euros"
print(text.format(40,20))

# Position can be established
text = "I have {1} euros and I owe you {0} euros"
print(text.format(40,20))

# Escape characters: \', \\, \n (new line), \r (carriage ret), \t (tab), \b (backsace), \f, \ooo (octo), \xhh (hex)
# REMEMBER: Python offers a large variety of methods regarding strings

# Boolean - most thing yield a True result; exceptions: empty strings, sets, etc.,  null values, __len__ function yielding 0

# OPERATIONS    

x = 9

x += 1
x -= 1

# floor division, for comparison: x /= 2 #4.5
x //= 2  #4
print(x)

# power, exponent
x **= 3 
print(x)

x = frozenset('bce')
x &= set('bac')
print(x)

x = 5
x &= 3
print(x)

# REMINDER: a few operations are binary (>>, <<, ^, |, &, ~)
# To understand how they work, it's best to transform each number
# 5 in binary is 101 and 3 in binary is 011
# For >> and << operations you just "push" the numbers to one side or the other and fill the rest with zeros
# For &, | and ^ (and, or and xor) you are looking at the "similarities" and "differences"
# For & (and) you want both alligned numbers to be 1 in order to assign a 1 in your final value:
# 5     10>1<
# 3     01>1<
# ----------
#       00>1<
# And by transforming the result back, we get the answer (001 = 1)
# Works the same for the rest

# LISTS

mylist = ["egg", "pear", "salt"]

# Lists can be created with the function list()
newlist = list( ("green", "blue") )

# REMINDER:
#       Lists:
#       -> ORDERED
#       -> CHANGEABLE
#       -> allows DUPLICATE

# Print the 3rd element
print(mylist[2])
# Print the last element
print(mylist[-1])

# Reassigning values:
mylist[2] = "pepper"
print(mylist)

# Inserting values is possible with the function insert(position, new_element)
mylist.insert(1, "pringles")
print(mylist)

mylist.append("juice")
print(mylist)

# Appending one list to another can be done with extend()
# Works for any interable object, does not have to be list-list
mylist.extend(newlist)
print(mylist)

# You can remove a value with remove(value)
# Works only with the first occurance, will not remove all instances in the case of duplicates
mylist.remove("pear")
print(mylist)

# Removing a value based on index can be done with pop(index)
mylist.pop(4)
print(mylist)
# pop() without a given index removes the last item

# Removing a value can also be done with the keyword "del"
del mylist[0]
print(mylist)
# You can empty the entire list
newlist.clear()
print(newlist)
# Or just delete it
del newlist

# Loop through all the elements
for x in mylist:
    print(x)
    
print("\n")

# Same thing but it's based on index
for i in range(len(mylist)):
    print(mylist[i])

print("\n")

# We can also use while
i = 0
while i < len(mylist):
    print(mylist[i])
    i += 1

print("\n")

# Short syntax:
[print(x) for x in mylist]

