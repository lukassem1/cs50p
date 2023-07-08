import random


def main(): # define global values
    lvl = get_level()
    print(generate_integer(lvl))


def get_level():
    while True:
        try:
            level = input("Level: ")
            level = int(level)
            x = level #random.randint(1,level)
            if x == int(x) and x >=1 and x <=3 :
                print("ok")
                return level
            else:
                continue
        except ValueError:
            pass



def generate_integer(level):
    correct = 0
    z = 10
    if level == 1:
        while z >= 1:
            x1 = random.randint(0,9)
            x2 = random.randint(0,9)
            soma = x1 + x2
            result = input(f"{x1} + {x2} = ")
            if int(result) == soma:
                correct = correct + 1
            else:
                print("EEE")
                tries = 1
                while tries < 3:
                    result = input(f"{x1} + {x2} = ")
                    if int(result) == soma:
                        correct = correct + 1
                        break
                    print("EEE")
                    tries +=1
                print(f"{x1} + {x2} = {soma}")
            z = z - 1
        return correct

    if level == 2:
        while z >= 1:
            x1 = random.randint(10, 99)
            x2 = random.randint(10, 99)
            soma = x1 + x2
            result = input(f"{x1} + {x2} = ")
            if int(result) == soma:
                correct = correct + 1
            else:
                print("EEE")
                tries = 1
                while tries < 3:
                    result = input(f"{x1} + {x2} = ")
                    if int(result) == soma:
                        correct = correct + 1
                        break
                    print("EEE")
                    tries += 1
                print(f"{x1} + {x2} = {soma}")
            z = z - 1
        return correct

    if level == 3:
        while z >= 1:
            x1 = random.randint(100, 999)
            x2 = random.randint(100, 999)
            soma = x1 + x2
            result = input(f"{x1} + {x2} = ")
            if int(result) == soma:
                correct = correct + 1
            else:
                print("EEE")
                tries = 1
                while tries < 3:
                    result = input(f"{x1} + {x2} = ")
                    if int(result) == soma:
                        correct = correct + 1
                        break
                    print("EEE")
                    tries += 1
                print(f"{x1} + {x2} = {soma}")
            z = z - 1
        return correct

    #if level == 2:
    #if level == 3:


if __name__ == "__main__":
    main()
