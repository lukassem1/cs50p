expression = input("Expression: ").strip()
x, y, z = expression.split(" ")
x,z = float(x), float(z)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/" and z != 0:
    print(x / z)
