import inflect
my_list = []
p = inflect.engine()
while True:
    try:
        my_list.append(input("Name: "))
    except EOFError:
        print('\n')
        print("Adieu, adieu, to",p.join(my_list))
        break
    #word = "rat"
    #print("The plural of ", word, " is ", p.plural(word))
