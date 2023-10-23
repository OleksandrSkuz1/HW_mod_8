from datetime import date, timedelta

# print(datetime.today())

# Поточний день
start_date = date.today()    
# Останній день нашого циклу поздоровлень
end_date = start_date + timedelta(7)
    
print(f"{start_date = }, {end_date =}")

# Основна функція
def get_bd(users: list) -> list:
    start_date = date.today()
    end_date = start_date + timedelta(7)

    for user in users:
        bd: date = users["birthday"]
        print(bd)
        bd = bd.replace(year=start_date.year)
        print(bd)
 
 
if __name__ == "__main__":
   
  users = [{"name": "Bill", "birthday": date(1995, 10, 17)},
           {"name": "Kelly", "birthday": date(2001, 10, 19)},
            {"name": "John", "birthday": date(2005, 10, 20)},
            
            ]       
   


