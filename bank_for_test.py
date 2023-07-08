def main():
    valor = value(input('Greeting: '))
    print(f"${valor}")


def value(greeting):
    greeting = greeting.lower().strip()
    first_letter = greeting[0]
    if greeting[0:5] == 'hello':
        return 0
    elif first_letter == "h":
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()
