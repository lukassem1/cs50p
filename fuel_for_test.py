def main():
    num = input("Fraction: ")
    percent = convert(num)
    print(gauge(percent))

def convert(num):
    while True:
        try:
            x, y = num.split(sep="/")
            if int(x) > int(y):
                x, y = 0, 0
            cal = (int(x) / int(y)) * 100
            return cal
            exit()
        except ValueError:
            raise
        except ZeroDivisionError:
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"

if __name__ == "__main__":
    main()
