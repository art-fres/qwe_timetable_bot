from datetime import datetime

russian_months = {
    1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля',
    5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа',
    9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
}
now = datetime.now()
weekdays_ru = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]

ww = weekdays_ru[now.weekday()]


if ww == "суббота":

    def get_russian_date(date_obj=None):
        if date_obj is None:
            date_obj = datetime.now()
        
        day = date_obj.day
        month = russian_months[date_obj.month]
        
        
        return f"{day + 2} {month}"

else:
    def get_russian_date(date_obj=None):
        if date_obj is None:
            date_obj = datetime.now()
        
        day = date_obj.day
        month = russian_months[date_obj.month]
        
        
        return f"{day + 1} {month}"