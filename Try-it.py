msg = "You got this <3"
print(msg)

# REMEMBER: exit() for inside the terminal

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
