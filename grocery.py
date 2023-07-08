grocery = {}

while True:
    try:
        item = input()
        item = item.upper()
        if item in grocery:
            grocery[item] += 1
        else:
            grocery[item] = 1
    except EOFError:
        break

sorted_lis = sorted(grocery.items())

for item in sorted_lis:
    print(f"{item[1]} {item[0]}")
