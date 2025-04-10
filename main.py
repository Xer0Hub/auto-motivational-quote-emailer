import smtplib
import datetime as dt
import random

now = dt.datetime.now()
today = now.weekday()
random_quote_chooser = random.randint(0, 102)


my_email = "mike.genaric@gmail.com"
password = "gwhd dqpu jeyg engb"
target = "alice.genaric@yahoo.com"

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

quote_of_day = quotes[random_quote_chooser]


if today == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=target, msg=f"Subject: Morning inspiration \n\n {quote_of_day}")
        print("Sent home boy!")

