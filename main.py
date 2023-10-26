from datetime import date, timedelta

# first day and last day in our period - 1-ий варінт
# start_date = date.today()
# end_date = start_date + timedelta(7)
# print(f"{start_date = }, {end_date = }")

# first day and last day in our period - 2-ий варінт
def get_period(start_date: date, days: int):
    period = {}
    for _ in range(days + 1):
        period[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return period

# MAIN FUNCTION
def get_birthdays_per_week(users: list) -> dict:
    start_date = date.today()
    period = get_period(start_date, 7)
    
    day_name = {}  # словник для групування користувачів за днями тижня
    
    # MAIN CYCLE    
    # перевіряємо список наших юзерів
    for user in users:
        bd: date = user["birthday"]   # др кожного користувача справжній
        date_bd = bd.day, bd.month # др кожного користувача в цьому році
        
        # Розраховуємо різницю в днях між поточною датою та днем народження 
        days_until_birthday = (bd.replace(year=start_date.year) - start_date).days
        
        # Перевіряємо, чи день народження вже минув у цьому році    
        if days_until_birthday < 0:
            # День народження вже минув, переводимо його на наступний рік 
            bd = bd.replace(year=start_date.year + 1)
            days_until_birthday = (bd - start_date).days

        # Перевіряємо, чи день народження припадає на вихідний (суботу або неділю)
        if bd.weekday() in (5, 6):
            # Переносять день на понеділок
            bd += timedelta(days=(7 - bd.weekday()))
        
        # Перевіряємо, чи день народження входить у визначений період (7 днів)
        if 0 <= days_until_birthday <= 7:
            # Додаємо ім'я користувача до відповідного дня тижня    
            day_of_week = bd.strftime("%A")
            if day_of_week not in day_name:
                day_name[day_of_week] = []
            day_name[day_of_week].append(user["name"])
            
    return day_name

if __name__ == "__main":
    users = [
        {"name": "Jan", "birthday": date(1980, 1, 1)},
        {"name": "Bill", "birthday": date(1991, 10, 28)},
        {"name": "Steve", "birthday": date(2002, 2, 24)},
        {"name": "Mark", "birthday": date(2005, 11, 2)},
        {"name": "Elon", "birthday": date(2005, 10, 27)},
    ]

    result = get_birthdays_per_week(users)
    print(result)






    








