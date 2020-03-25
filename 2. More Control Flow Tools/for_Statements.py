# word 
print("count word")
pets = ["cat","dog","fish"]
for x in pets :
    print(x, len(x))

print("--------------------")
print("\n")

# range() built-in function
# range(start,stop,step) 
# 'float' object cannot be interpreted as an integer

print("range()")

# sum() built-in function
mySum = sum(range(5)) #mySum = 0 + 1 + 2 + 3 + 4
print("mySum = ",mySum)

# list() built-in function
myLists = list(range(20)) # myList = [0,1,2,...,19]
print("myLists = ",myLists)

print("--------------------")
print("\n")

print("range() in loop")
for a in range(5) :
    print("a = ",a)

print("\n")

for b in range(5,10) :
    print("b = ",b)

print("\n")
     

for c in range(5,10,1) :
    print("c = ",c)

print("\n")

for d in range(10,5,-1) :
    print("d = ",d)

print("\n")

print("--------------------")
print("\n")

