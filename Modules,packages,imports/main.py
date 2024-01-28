from datetime import datetime

import emoji
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == "__main__":
    calculate_salary()
    get_employees()
    date_time = datetime.now()
    formatted_string = date_time.strftime("Сегодня %d-%m-%Y %H:%M")
    print(formatted_string)
    print(emoji.emojize(":purple_heart:"))
