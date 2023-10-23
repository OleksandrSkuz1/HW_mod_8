from datetime import date, timedelta

# print(datetime.today())

# Поточний та останній день нашого періоду поздоровлень
start_date = date.today()    
end_date = start_date + timedelta(7)
# print(f"{start_date = }, {end_date =}")

def get_period(start_date: date, days: int):
    result = {}
    for _ in range(days + 1):
        result[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)
    return(result)    

# Основна функція
def get_bd(users: list) -> list:
    start_date = date(2023, 12, 29)   
    period = get_period(start_date, 7)
    # end_date = start_date + timedelta(7)
    
    for user in users:
        bd: date = user["birthday"]
        bd = bd.replace(year =)
        # if start_date <= bd <= end_date:
        # date_bd = bd.day, bd.month
        if date_bd in list(period):
            print(user["name"])
            print(period[date_bd])
 
 
if __name__ == "__main__":
   # Список іменинників з ключем date-дата народження
    users = [{"name": "Bill", "birthday": date(1995, 12, 30)},
             {"name": "Kelly", "birthday": date(2000, 1, 2)},
             {"name": "John", "birthday": date(2005, 10, 20)},
             ]
            
                   
    get_bd(users)
    # print(get_period(date(2023, 12, 29), 7))