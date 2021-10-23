nicNo = (input("Input Your NIC number: "))
global year
global daynum
global date
global gender

def checkLeap():
    global year
    if (year)%4 == 0:
        if (year)%100 == 0:
            if (year)%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def nic():

    dateandmonth()
    
    print(f"Your Birth Year is {year}")    
    print(f"Your Birth Month is {month}")
    print(f"Your Birth date is {date}")
    print(f"You are a {gender}")


def dateandmonth():
    global daynum
    global day
    global gender
    
    if daynum > 500:
        day = daynum - 500
        gender = "Female"
    else:
        day = daynum
        gender = "Male"

    global month
    global date
    if day <= 31:
        month = "January"
        date = day
    elif day <=59:
        month = "February"
        date = day - 31
    elif day <= 90:
        month = "March"
        date = day - 59
    elif day <= 120:
        month = "April"
        date = day - 90
    elif day <= 151:
        month = "May"
        date = day - 120
    elif day <= 181:
        month = "June"
        date = day - 151
    elif day <= 212:
        month = "July"
        date = day - 181
    elif day <= 243:
        month = "August"
        date = day - 212
    elif day <= 273:
        month = "September"
        date = day - 243
    elif day <= 304:
        month = "October"
        date = day - 273
    elif day <= 334:
        month = "November"
        date = day - 304
    elif day <= 365:
        month = "December"
        date = day - 334
    else:
        print("Enter a valid NIC number")


if len(nicNo) == 10:
    year = 1900 + int(nicNo[0:2])
    daynum = int(nicNo[2:5])-1
    nic()
elif len(nicNo) == 12:
    year = int(nicNo[0:4])
    daynum = int(nicNo[4:7])-1
    nic()
else:
    print("Enter valid NIC number")

print("\nTap enter to close")
input("")
