def main():
    shorts = shorten(input("Input: "))
    print(shorts)

def shorten(word):
    vowels= ['a','e','i','o','u', 'A','E','I','O','U']
    short = ''
    for char in word:
        if char not in vowels:
            short = short + char
    return short

if __name__ == "__main__":
    main()
