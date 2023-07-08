s = input("camelCase: ")
aux = 0
print("snake_case: ",end="")
for char in s:
    if char.isupper():
        if aux == 0:
            print(char.lower(),end="")
            aux+=1
            continue
        else:
            print("_",end="")
            print(char.lower(), end="")
            aux += 1
    else:
        print(char, end="")
        aux += 1
