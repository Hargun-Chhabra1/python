#LISTS:
#Lists are used to store multiple items in a single variable.
#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change
#If you add new items to a list, the new items will be placed at the end of the list.
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
#Since lists are indexed, lists can have items with the same value:
from re import A


thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#To determine how many items a list has, use the len() function:
print(len(thislist))
#List items can be of any data type:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1, list2, list3)
#A list can contain different data types:
list0 = ["abc", 34, True, 40, "male"]
print(list0)
#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#Using the list() constructor to make a List:
thislist_ghost = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist_ghost)

#TUPLES:
#Tuples are used to store multiple items in a single variable.
#A tuple is a collection which is ordered and unchangeable.
#Tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Tuple items are ordered, unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
#When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
#Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
#Since tuples are indexed, they can have items with the same value:
thistuple_1 = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple_1)
#To determine how many items a tuple has, use the len() function:
thistuple_ghost = ("apple", "banana", "cherry")
print(len(thistuple_ghost))
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple_2 = ("apple",)
print(type(thistuple_2))
#not a tuple
thistuple_not = ("apple")
print(type(thistuple_not))
#Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 2, 3)
tuple3 = (True, False, True)
#A tuple can contain different data types:
tuple_1 = ("apple", 1, True)
#From Python's perspective, tuples are defined as objects with the data type 'tuple':
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#It is also possible to use the tuple() constructor to make a tuple.
tupleghost = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(tupleghost)

#DICTIONARY:
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values:
thisdict = {
    "brand": "ford",
    "model": "mustang",
    "year":1964
}
print(thisdict)
#Dictionary items are ordered, changeable, and does not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
#Print the "brand" value of the dictionary:
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dict["brand"])
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
#Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.
#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values:
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #will be printed out as 2020
}
print(thisdict1)
#To determine how many items a dictionary has, use the len() function:
print(len(thisdict))
#The values in dictionary items can be of any data type:
#String, int, boolean, and list data types:
thisdict2 = {
    "brand": "Ford",
    "electric":False,
    "year":1964,
    "color":["red", "white", "blue"]
}
#From Python's perspective, dictionaries are defined as objects with the data type 'dict':
#eg.
thisdict_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict_1))
#PYTHON CONDITIONALS:
#PYTHON IF ELSE:
#python sypports the usual logical conditions from mathimatics:
a = 100
b = 100
c = 150
#EQUAL:
a == b
#NOT EQUAL:
a != c
#LESS THAN:
a < c
#LESS THAN OR EQUAL TO:
a <= b
#GREATER THAN:
c > a
#GREATER THAN OR EQUAL TO
c >= a
#These conditions can be used in several ways, most commonly in "if statements" and loops.
#An "if statement" is written by using the if keyword.
d = 33
e = 200
if e > d:
  print("e is greater than d")#Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.
#In this example we use two variables, d and e, which are used as part of the if statement to test whether e is greater than d. As d is 33, and e is 200, we know that 200 is greater than 33, and so we print to screen that "e is greater than d".
#PYTHON ELIF
#The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
f = 100
g = 100
if g > f:
  print("g is greater is f")
elif g == f:
  print("g is equal to f")
#In this example a is equal to b, so the first condition is not true, but the elif condition is true, so we print to screen that "a and b are equal".
#ELSE:
#The else keyword catches anything which isn't caught by the preceding conditions.
h = 200
i = 33
if i > h:
  print("i is greater than h")
elif h == i:
  print("h is equal to i")
else:
  print("h is greater than i")
#In this example a is greater than b, so the first condition is not true, also the elif condition is not true, so we go to the else condition and print to screen that "a is greater than b".
#You can also have an else without the elif:
if i > h:
  print("i is greater than")
else:
  print("i is not greater than h")
#SHORTHAND IF:
#If you have only one statement to execute, you can put it on the same line as the if statement.
if h > i: print("h is greater than i")
#SHORTHAND IF.... ELSE
#If you have only one statement to execute, you can put it on the same line as the if statement.
print("I") if i > h else print("H")
#You can also have multiple else statements on the same line:
print("A") if a > b else print("A=B") if a==b else print("B")
#AND:
#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if h is greater than i, AND if j is greater than i:
j = 100
if h > i and j > 1:
  print("both statments are correct")
#OR:
#The or keyword is a logical operator, and is used to combine conditional statements:
#Test if h is greater that i, OR if j is greater than h
if h > i or j > h:
  print("atleast one statment is correct")
#NESTED IF:
#You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten")
  if x > 20:
    print("also above 20")
  else:
    print("but not above 20")
#THE PASS STATMENT:
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if h > a:
  pass
#PYTHON WHILE LOOPS:
#python has 2 primitive commands: while loops and for loops
#With the while loop we can execute a set of statements as long as a condition is true
#Print k as long as k is less than 6:
k = 1
while i < 6:
  print(i)
  i += 1
#The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, k, which we set to 1.
#THE BREAK STAMENT:
#With the break statement we can stop the loop even if the while condition is true:
while k < 6:
  print(k)
  if k == 3:
    break
  k += 1
#THE CONTINUE STATMENT:
#With the continue statement we can stop the current iteration, aand continue with the next:
#continue to the next iteration if l is 3:\
l = 0
while l < 6:
  l += 1
  if l == 3:
    continue
  print(i)
#Wit the else statement we can run a block of code once when the condition no longer is true:
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
#PYTHON FOR LOOPS:
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
#Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#The for loop does not require an indexing variable to set beforehand
#LOOPING THROUGH A STRING
#Even strings are iterable objects, they contain a sequence of characters
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
#THE BREAK STATEMENT:
#With the break statement we can stop the loop before it has looped throu all the iteams:
#Exit the loop with X is "banana":
for x in fruits:
  print(x)
  if x == "banana":
    break
#Exit the loop when x is "banana", but this time the break comes before the print:
for x in fruits:
  if x == "banana":
    break
  print(x)
#THE CONTINUE STATEMENT
