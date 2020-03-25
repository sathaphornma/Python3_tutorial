# Lists
print("Basic List")
myLists = [50,45,80,12]
print(myLists)
print(myLists[1])
print(myLists[3])

print("--------------------")
print("\n")

# Slicing List
print("Slicing List")
print(myLists[:3])
print(myLists[1:3])
print(myLists[-3:-1])

print("--------------------")
print("\n")

# Add List
print("Add List")
add = myLists + [88,99,55] # New variable for add list to myList.
print("Before = ",myLists)
print("After = ",add)

print("--------------------")
print("\n")


# Add new items at the end of the list, by using the append() 
print("Add by append()")
print("Before = ",myLists)
myLists.append(188)
myLists.append(4 ** 3)
print("After = ",myLists)

print("--------------------")
print("\n")




# Replace some values
print("Replace List")
print("Before = ",myLists)
num = 102
myLists[0] = 300
myLists[1] = 4 ** 3
myLists[3] = num
print("After = ",myLists)

print("--------------------")
print("\n")

# Count List
print("Count List")
print("myLists = ",myLists)
print("Count = ",len(myLists))


print("--------------------")
print("\n")

# Remove List
print("Remove List")
print("Before = ",myLists)
myLists[2:3] = [] # Remove 1 item.
print("After1 = ",myLists)
myLists[:] = [] # Remove all.
print("After2 = ",myLists)


