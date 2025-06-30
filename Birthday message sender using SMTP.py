import pandas as pd
import datetime as dt
import smtplib
import random

email = "your_email@example.com"
passw = "your_app_password"

today = dt.datetime.now()
today_month = today.month
today_day = today.day

read = pd.read_csv("birthday\\birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row for _, data_row in read.iterrows()
}

if (today_month, today_day) in birthdays_dict:
    birthday_person = birthdays_dict[(today_month, today_day)]

letter = random.randint(1, 3)
content = f"birthday\\letter_templates\\letter_{letter}.txt"

with open(content) as letter_file:
    letter2 = letter_file.read()

personalized_letter = letter2.replace("[NAME]", birthday_person["name"])

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=email, password=passw)
    connection.sendmail(
        from_addr=email,
        to_addrs=birthday_person["email"],
        msg=f"Subject:Happy Birthday {birthday_person['name']}!\n\n{personalized_letter}"
   )

print("Birthday Message sent")
#Note if there is no birthday on the date it will throw an error
