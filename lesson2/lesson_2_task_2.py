def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2024
leap_year = is_year_leap(year)


print("2024", year, ":", leap_year)
