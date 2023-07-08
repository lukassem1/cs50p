import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
        x = random.randint(1,level)
        if x == int(x) and x >=1:
            print("ok")
            break
        else:
            continue
    except ValueError:
        pass
while True:
    try:
        y = input("Guess: ")
        y = int(y)
        if y == x:
            print("Just right!")
            exit()
        elif y > x:
            print("Too large!")
        elif y < x:
            print("Too small!")
        else:
            print("wrong crazy guy")
    except ValueError:
        pass
