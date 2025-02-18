def days_since_birthday(birthday_str):
    """
    This funtion calculates the total number of days in the complete full years that have passed since your birthday,
    excluding the days in your birth year and the current year. Assuming that every full year has exactly 365 days.

    :param birthday_str: A string representing your birthday in the format "DD-MM-YYYY".
    :return: An integer representing the total number of days in the complete years
             between your birth year and the current year.
    """
    parts = birthday_str.split("-") #this helps split day-month-year
    birth_year = int(parts[2])

    current_year = 2025 #setting current year

    full_years = current_year - birth_year - 1

    total_days = full_years * 365 #multiply each year by 365
    return total_days
birthday = "25-04-2004"
print("Total days in full years since your birthday:", days_since_birthday(birthday))