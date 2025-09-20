from urllib.parse import quote
from date import get_russian_date

date_string = str(get_russian_date())


encoded_string = quote(date_string)

