dictionary = [
    {'month': "january", 'code':"0"},
    {'month': "february", 'code': "3"},
    {'month': "march", 'code': "3"},
    {'month': "april", 'code': "6"},
    {'month': "may", 'code': "1"},
    {'month': "june", 'code': "4"},
    {'month': "july", 'code': "6"},
    {'month': "august", 'code': "2"},
    {'month': "september", 'code': "5"},
    {'month': "october", 'code': "0"},
    {'month': "november", 'code': "3"},
    {'month': "december", 'code': "5"},
]

weekday = [
    {'day': "sunday", 'code': "0", 'female': "Akosuwa", 'male': "Kwasi"},
    {'day': "monday", 'code': "1", 'female': "Adwoa", 'male': "Kadjo"},
    {'day': "tuesday", 'code': "2", 'female': "Abeena", 'male': "Kwabena"},
    {'day': "wednesday", 'code': "3", 'female': "Akwa", 'male': "Kwaku"},
    {'day': "thursday", 'code': "4", 'female': "Yaa", 'male': "Yaw"},
    {'day': "friday", 'code': "5", 'female': "Afia", 'male': "Kofi"},
    {'day': "saturday", 'code': "6", 'female': "Amma", 'male': "Kwame"}
]

def year_code():
    y_code = (year1 + (year1 // 4)) % 7
    print(f"year code is: {y_code}")
    return y_code
year = (input("Year: "))
year1 = int(year[2:])


def leap_year():
    year3 = int(year)
    if year3 // 4 or year3 // 400:
        leap_code = 1
    elif year3 // 100:
        leap_code = 0
    print(f"Leap year code is: {leap_code}")
    return leap_code


def century_code():
    year2 = int(year[:2])
    if year2 == 17:
        c_code = 4
    elif year2 == 18:
        c_code = 2
    elif year2 == 19:
        c_code = 0
    elif year2 == 20:
        c_code = 4
    elif year2 == 22:
        c_code = 2
    elif year2 == 0:
        c_code = 0
    print(f"Century code is: {c_code}")
    return c_code

def month_code():
    for month in dictionary:
        m_code = month['code']
        if month1 == month['month']:
            print(f'The month code is: {m_code}')
        return m_code
month1 = input("Month: ")


birth_date = int(input("Day: "))
def day_code():
    a = month_code()
    b = year_code()
    c = century_code()
    d = leap_year()
    d_code = (birth_date + int(a) + int(b) + int(c) - int(d))%7
    print(f'the day code is: {d_code}')
    return d_code
f = day_code()
for day in weekday:
    if f == int(day['code']):
       g = day['day']
       if f == int(day['code']):
          x = input("Gender: ")
          if x == "female":
             name = day['female']
          elif x == "male":
              name = day['male']
          print(f'You are born on {g} and your name is {name}')


