def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    while True:
        x = len(s)
        s1 = s[:2]
        s2 = s[2:]
        s3 = s[:]
        if x > 6 or x < 4:
            return False
        if s1.isnumeric():
            return False
        if s3.isalpha():
            return True
        for char in s:
            if char in "'.,;:?!":
                return False
        if s[-1].isalpha() or s[-2].isalpha():
            return False
        if s[-2] == "0" and s[-3].isalpha():
            return False
        else:
            return True

main()
