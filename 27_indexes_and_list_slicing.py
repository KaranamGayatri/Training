#Create a variable and assign it the list [[0, 2], [4, 6], [8, 10], [12, 14]]
List = [[0, 2], [4, 6], [8, 10], [12, 14]]

#Access the first list from the list of lists in step 1 by index then print it
first_list = List[0]
print(first_list)

#Access the 14 from the list in step 1 then print it
print(List[3][1])

#Create a second variable and assign it the list ["chair", "table", "desk", "lamp", "bed"]
Second_List = ["chair", "table", "desk", "lamp", "bed"]

#Use a negative integer to access "chair" from the variable in step 4 by index then print it
print(Second_List[-5])

#Print "Most people own at least 2 chairs." by concatenating the 2 from the list and the "chair" from the second list with "Most people own at least ", a space, and a period
print("Most people own at least " + str(first_list[1]) + " " + Second_List[0]+ "s")

#Create a third variable and assign it the list [0.98, 8.76, 6.54, 4.32]
Third_List = [0.98, 8.76, 6.54, 4.32]

#Print the slice [8.76, 6.54, 4.32] from the variable
print(Third_List[1:])

#Print the slice [8.76, 6.54] from the variable
print(Third_List[1:3])