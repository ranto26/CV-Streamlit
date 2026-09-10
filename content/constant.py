import datetime

LAST_NAME = "VAOHAVY"
FIRST_NAME = "Arindranto"
BIRTHDAY = datetime.date(2004, 1, 19)
TODAY = datetime.date.today()

AGE = TODAY.year - BIRTHDAY.year
if (TODAY.month < BIRTHDAY.month) or (
    TODAY.month == BIRTHDAY.month and TODAY.day < BIRTHDAY.day
):
    AGE = AGE - 1

NUMBER = "+33649761889"
PLACE = "Lyon"
EMAIL = "vaohavy.arindranto@gmail.com"

TITRE = "Data Scientist / Data Analyst"
