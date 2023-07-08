month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    date = input("Date: ").strip().title()
    date1 = date.split("/")
    try:
        if len(date1) == 3 and int(date1[2]) and int(date1[0]) <= 12 and int(date1[1]) <= 31:
            print(f"{date1[2]}-{date1[0]:0>2}-{date1[1]:0>2}")
            break
    except ValueError:
        pass
    date2 = date.split("-")
    try:
        if len(date2) == 3 and int(date2[2]) and int(date2[0]) <= 12 and int(date2[1]) <= 31:
            print(f"{date2[2]}-{date2[0]:0>2}-{date2[1]:0>2}")
            break
    except ValueError:
        pass
    date3 = date.replace(",","").split()
    try:
        if len(date3) == 3 and int(date3[2]) and int(date3[0]) <= 12 and int(date3[1]) <= 31:
            print(f"{date3[2]}-{date3[0]:0>2}-{date3[1]:0>2}")
            break
    except ValueError:
        if date3[0].title() in month and int(date3[1]) <= 31 and ',' in date:
            n_month = month.index(date3[0])+1
            print(f"{date3[2]}-{n_month:0>2}-{date3[1]:0>2}")
            break
    else:
        pass
