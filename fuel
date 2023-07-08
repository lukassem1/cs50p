while True:
    try:
        x, y = input("Fraction: ").split(sep="/")
        if int(x) > int(y):
            x,y = 0,0
        cal = (int(x) / int(y)) * 100
        if cal >= 99:
            print("F")
            exit()
        if cal <= 1:
            print("E")
            exit()
        else:
            print(f"{cal:.0f}%")
        exit()
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
