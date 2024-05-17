# Numbers

#Write an equation that uses multiplication, division, an exponent, 
#addition, and subtraction that is equal to 100.25.

print(((6 * 5) / 10) ** 4 + 117.50 - 98.25)

#What is the value of the expression 4 * (6 + 5)

print(4 * (6 + 5) ) #Output:44

#What is the value of the expression 4 * 6 + 5 

print(4 * 6 + 5) #Output:29

#What is the value of the expression 4 + 6 * 5 

print(4 + 6 * 5) #Output:34

#What is the type of the result of the expression 3 + 1.5 + 4?

A = 3 + 1.5 + 4
print(A)       #Output:8.5
print(type(A)) #Output:float

#What would you use to find a number’s square root, as well as its square?

print(81**0.5) #Output:9.0
print(9**2)    #Output:81

# Strings

#Given the string 'hello' give an index command that returns 'e'.
#Enter your code in the cell below:

str = 'hello'
print(str[1])

#Reverse the string 'hello' using slicing:

print(str[::-1])

#Given the string 'hello', give two methods of producing the letter 'o' using indexing.

print(str[-1])
print(str[4])

# Lists

#Build this list [0,0,0] two separate ways.

list1 =[0,0,0]
print([0]*3)
print(list1)

#Reassign 'hello' in this nested list to say 'goodbye' instead:

list3 = [1,2,[3,4,'hello']]
list3[2][2]="goodbye"
print(list3)

#Sort the list below:

list4 = [5,3,4,6,1]
print(sorted(list4))

# Dictionaries

#Using keys and indexing, grab the 'hello' from the following dictionaries:

d = {'simple_key':'hello'}
# Grab 'hello'
print(d['simple_key'])

d = {'k1':{'k2':'hello'}}
# Grab 'hello'
print(d['k1']['k2'])

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
#Grab 'hello'
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#Grab 'hello'
print(d['k1'][2]['k2'][1]['tough'][2][0])

# Tuples

#How do you create a tuple?
t=(1,2,3)

# Set

#Use a set to find the unique values of the list below:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
print(set(list5))

# Booleans

#What will be the resulting Boolean of the following pieces of code 
#(answer fist then check by typing it in!)

#Answer before running cell
2 > 3
print(2 > 3) #False

#Answer before running cell
3 <= 2
print(3 <= 2) #False

#Answer before running cell
3 == 2.0
print(3 == 2.0) #False

#Answer before running cell
3.0 == 3
print(3.0 == 3) #True

#Answer before running cell
4**0.5 != 2
print(4**0.5 != 2) #False

# Final Question:

#What is the boolean output of the cell block below?
#two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]
#True or False?
if l_one[2][0] >= l_two[2]['k1']: #False
    print("True")
else:
    print("False")