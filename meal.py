def main():
    time = input("What time is it? ").strip().lower()
    whichtime(convert(time))


def convert(time):
    hours, minutes = time.split(":")
    hours, minutes = float(hours), float(minutes)
    calc = hours + minutes / 60
    return calc

def whichtime(time): #no ampm
    if 7<= time <=8:
        print("breakfast time")
    elif 12<= time <= 13:
        print("lunch time")
    elif 18<= time <= 19:
        print("dinner time")
    return time
if __name__ == "__main__":
    main()
