from datetime import date, timedelta

# Поточний та останній день нашого періоду поздоровлень
start_date = date.today()    
end_date = start_date + timedelta(7)
print(f"{start_date = }, {end_date =}")

def get_period(start_date: date, day_name: int):
    result = {}
    for _ in range(day_name + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return(result)    

# Основна функція
def get_birthdays_per_week(users: list) -> list:
    start_date = date(2023, 12, 29)   
    period = get_period(start_date, 7)
    end_date = start_date + timedelta(7)
    
    for user in users:
        bd: date = user["birthday"]
        bd = bd.replace(year=start_date.year)
        if start_date <= bd <= end_date:
            bd = bd.day, bd.month
        if bd in list(period):
            
            print(user["name"])
            print(period[bd])
 
 
if __name__ == "__main__":
    users = [
        {"name": "Jan", "birthday": date(1980, 1, 1)},
        {"name": "Bill", "birthday": date(1991, 10, 28)},
        {"name": "Steve", "birthday": date(2002, 2, 24)},
        {"name": "Mark", "birthday": date(2005, 5, 14)},
        {"name": "Elon", "birthday": date(2005, 6, 28)}
    ]
    
    result = get_birthdays_per_week(users)
    
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {', '.join(names)}")
