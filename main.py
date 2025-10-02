year = input("Enter a year: ")
month = input("Enter a month between 1-12: ")
day = input("Enter a day: ")

year_int = int(year)
month_int = int(month)
day_int = int(day)

january = [3]
february = [28]
march = [14]
april = [4]
may = [9]
june = [6]
july = [11]
august = [8]
september = [5]
october = [10]
november = [7]
december = [12]

months = [january, february, march, april, may, june, july, august, september, october, november, december]

first_two = int(year[0] + year[1])
last_two = int(year[2] + year[3])
is_leap_year = False

special_day = 0
final_day = 0

if first_two > 17:
    while first_two != 17 and first_two != 18 and first_two != 19 and first_two != 20:
        first_two -= 4
else:
    while first_two != 17 and first_two != 18 and first_two != 19 and first_two != 20:
        first_two += 4

if first_two == 18:
    special_day += 5
elif first_two == 19:
    special_day += 3
elif first_two == 20:
    special_day += 2

if last_two != 0:
    if last_two >= 4:
        special_day += last_two + (last_two // 4)
    else:
        special_day += last_two

if year_int % 4 == 0:
    if year_int % 100 == 0:
        if year_int % 400 == 0:
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False

if is_leap_year:
    months[0][0] = 4
    months[1][0] = 29

special_day += 28

temporary_value = 0

if day_int >= months[month_int - 1][0]:
    temporary_value = day_int - months[month_int - 1][0]
    while temporary_value >= 7:
        temporary_value -= 7
    final_day = special_day + temporary_value
else:
    temporary_value = months[month_int - 1][0] - day_int
    final_day = special_day - temporary_value

while final_day >= 7:
    final_day -= 7

if final_day == 1:
    print("Monday")
elif final_day == 2:
    print("Tuesday")
elif final_day == 3:
    print("Wednesday")
elif final_day == 4:
    print("Thursday")
elif final_day == 5:
    print("Friday")
elif final_day == 6:
    print("Saturday")
elif final_day == 0:
    print("Sunday")