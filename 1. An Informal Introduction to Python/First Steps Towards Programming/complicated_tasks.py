# Python for more complicated tasks.
# while loop
print("while loop")
a , b = 0 , 1
while a < 10 :
    print(a) 
    a , b = b, a + b
    
print("------------------------")
print("\n")

# variable for calculate
print("calculate")
i = 100 * 200
a = 2 ** 3
b = (i / 3) - a
print("Value = ",round(b,3))