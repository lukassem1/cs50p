import sys
import pyfiglet
if len(sys.argv) < 2:
    s = input("Input: ")
    print(pyfiglet.figlet_format(s))
else:
    if len(sys.argv[1:]) > 1:
        fs = sys.argv[1:]
        fs = ' '.join(fs)
        s = input("Input: ")
        figlet = pyfiglet.figlet_format(s)
        figlet = pyfiglet.figlet.setFont(font = fs)
    #else:
    #    fs = str(sys.argv[1])
    #    s = input("Input: ")
    #    print(pyfiglet.figlet_format(s, font= f"{fs}"))
