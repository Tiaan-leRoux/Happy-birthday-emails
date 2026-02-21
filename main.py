import os
import smtplib
import datetime as dt
import pandas
import random

my_email = os.environ.get("MY_EMAIL")
password = os.environ.get("PASSWORD")
date = dt.datetime.now()
today = (date.month, date.day)

birth_days =  pandas.read_csv("birthdays.csv")
b_day_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in birth_days.iterrows()}

if today in b_day_dict:
    folder =  f"letter_templates/letter_{random.randint(1,3)}.txt" # random message

    with open(folder) as letter_file:
        person_index = b_day_dict[today]
        birthday_message = letter_file.read()
        birthday_message = birthday_message.replace("[NAME]", person_index["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person_index["email"],
            msg=f"Subject: Happy Birthday\n\n {birthday_message}"
        )



