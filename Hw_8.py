from datetime import date
from copy import deepcopy

users = [
    {"name": "Vitaliy", "birthday": date(2000, 1, 30)},
    {"name": "Ignat", "birthday": date(1994, 2, 1)},
    {"name": "Ivan", "birthday": date(1991, 2, 4)},
    {"name": "Sasha", "birthday": date(1998, 2, 5)},
    {"name": "Lyda", "birthday": date(1993, 2, 6)},
    {"name": "Klim", "birthday": date(1995, 3, 4)},
    {"name": "Bill", "birthday": date(2000, 6, 1)},
    {"name": "Leonid", "birthday": date(2002, 1, 28)},
    {"name": "Danylo", "birthday": date(1994, 8, 23)},
    {"name": "Nikita", "birthday": date(1999, 9, 11)},
    {"name": "Peter", "birthday": date(2001, 11, 30)},
    {"name": "Ivan", "birthday": date(2000, 8, 24)},
    {"name": "Maria", "birthday": date(1998, 3, 19)},
]


def get_birthdays_per_week(users):
    today_date = date.today()
    users_to_wish = []
    result = [{}]
    name_list = []
    # Перетворення дати народження на дату дня народження в поточному році:
    for user in users:
        new_date = date(today_date.year, user["birthday"].month, user["birthday"].day)
        user["birthday"] = new_date
    # Відбір користувачів, день народження в яких, наступного тижня:
    for user in users:
        week_to_date = int(user["birthday"].strftime("%W"))
        if int(today_date.strftime("%W")) == week_to_date - 1:
            users_to_wish.append(user)
    # Заповнення пустого словника ключем - "день тижня" і значенням - пустий список
    for user in users_to_wish:
        if user["birthday"].strftime("%A") in "SaturdaySundayMonday":
            result[0].update({"Monday": name_list})
        else:
            result[0].update({user["birthday"].strftime("%A"): name_list})
    # Заповнення пустого списку імен - значеннями
    for weekday_to_wish in result[0].keys():
        for j in users_to_wish:
            week_day = j["birthday"].strftime("%A")
            if week_day in "SaturdaySunday":
                week_day = "Monday"
            if week_day == weekday_to_wish:
                name_list.append(j["name"])
        buff = deepcopy(name_list)
        result[0].update({weekday_to_wish: buff})
        name_list = []
    # Створення і заповнення результуючого рядка
    result_string = ""
    for key, val in result[0].items():
        result_string += key + ": "
        if len(val) > 1:
            for name_in_list in val[0:-1]:
                result_string += name_in_list + ", "
            result_string += val[-1] + "\n"
        else:
            result_string += val[0] + "\n"
    return result_string


if __name__ == "__main__":
    print(get_birthdays_per_week(users))
