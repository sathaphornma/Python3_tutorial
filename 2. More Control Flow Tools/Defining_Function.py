print("calculate tax")
def calTax(p) :
    tax = 7 / 100
    price = p * tax
    
    return price

print("price = ",calTax(500))

print("-------------------")
print("\n")

print("count word")
def countWord(w) :
    return len(w)

print("count = ",countWord("saifah"))


print("-------------------")
print("\n")

print("add Lists")
def add(a , L = []) :
    L.append(a)
    return L

print(add(1))
print(add(2))
print(add(3))
print(add("AA"))
