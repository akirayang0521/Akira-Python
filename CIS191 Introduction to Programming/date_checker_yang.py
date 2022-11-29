def date(year, month, day):
    if year < 0 or month < 1 or month > 12:
        return "is not valid"

    else:
        correct_day = 31                # 1,3,5,7,8,10,12 have 31 days
        if month in [4, 6, 9, 11]:
            correct_day = 30            # 4,6,9,11 have 30 days
        elif month == 2:
            correct_day = 28            # 2 has 28 days

        if day < 1 or day > correct_day:
            return "is not valid"

        return "is valid"


if __name__ == '__main__':
    print("This program accepts a date in the form month/day/year and outputs whether or not the date is valid")
    for i in range(5):
        s = input("Please enter a date (mm/dd/yyyy):")
        part = s.split('/')
        for n in range(len(part)):
            part[n] = int(part[n])
        year = part[2];                                   # year = int(s[6:10])
        month = part[0];                                  # month = int(s[0:2])
        day = part[1]                                     # day = int(s[3:5])
        print(s + " " + date(year, month, day))           # print(s + " " + date(year, month, day))