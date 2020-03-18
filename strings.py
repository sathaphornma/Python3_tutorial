# my comment single line 
' my comment single line '
" my comment single line "

"""
    my conment multiline
    line number 1
    line number 2
    line numbrt 3
    
"""

# single quotes and double qoutes
# ('...') and ("...")
print("--------------------------------")
print("my name is saifah") # (" ")
print("my name is saifah's") # (" ' ")
print('my name is saifah') # (' ')
print('my name is saifah\'s') # (' \' ')

print("\n")
 
# use backslashes
print("--------------------------------")
print("1 C:\saifah\name") #\n
print("2 C:\saifah\tame") #\t
print(r"3 C:\saifah\name") # use r before double quotes for print backslashes

print("\n")


# string concatenated with the + and repeated with *
print("--------------------------------")
print('sai' 'fah')
print('sai' + 'fah')
print(3 * 'sai' + 'fah') # use number for repeated

print("\n")

# strings in variable
print("--------------------------------")
h = "hello" 
name = "saifah"
print(h)
print(h +' '+ name)

g = ("good morning")
print(g + ' ' + name)

print("\n")

#indexs
py = "python"
print(py[0])
print(py[-2])
print("i"+py[-1]+"dexs of saifa"+py[3])

print("\n")

# slicing
"""
    +---+---+---+---+---+---+
    | P | y | t | h | o | n |
    +---+---+---+---+---+---+
     0   1   2   3   4   5   6
    -6  -5  -4  -3  -2  -1
"""

print(py)
print(py[2:5])
print(py[0:2])
print(py[:2])
print(py[:-2])
print(py[-2:])

print("\n")


# built-in function returns the length
print("--------------------------------")
count = len(py)
print(count)