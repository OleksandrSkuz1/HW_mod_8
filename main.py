from datetime import date, timedelta


def get_birthdays_per_week(users):
    # Створюємо словник для зберігання днів народження
    day_name = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
    }

    # Отримуємо поточну дату та останній день поздоровлень
    today = date.today()
    end_date = today + timedelta(7)

    # Перевіряємо, чи список користувачів порожній
    if not users:
        return day_name

    # Цикл обробки користувачів
    for user in users:
        user_birthday = user["birthday"]

        # Розраховуємо різницю в днях між поточною датою та днем народження
        days_until_birthday = (user_birthday - today).days

        # Перевіряємо, чи день народження вже минув у цьому році
        if days_until_birthday < 0:
            # День народження вже минув, переводимо його на наступний рік
            user_birthday = date(today.year + 1, user_birthday.month, user_birthday.day)
            days_until_birthday = (user_birthday - today).days

        # Перевіряємо, чи день народження в наступному тижні
        if days_until_birthday <= 7:
            # Додаємо ім'я користувача до відповідного дня тижня
            day_of_week = user_birthday.strftime("%A")
            day_name[day_of_week].append(user["name"])

    return day_name


if __name__ == "__main__":
    users = [
        {"name": "Jan", "birthday": date(1980, 1, 1)},
        {"name": "Bill", "birthday": date(1991, 10, 28)},
        {"name": "Steve", "birthday": date(2002, 2, 24)},
        {"name": "Mark", "birthday": date(2005, 5, 14)},
        {"name": "Elon", "birthday": date(2005, 10, 27)},
    ]

    result = get_birthdays_per_week(users)

    # Виводимо результат
    for day_name, name in result.items():
        print(f"{day_name}: {', '.join(name)}")
