import datetime as dt
import smtplib
import random
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()

with open('quotes.txt', 'r') as quote_file:
    all_quotes = quote_file.readlines()
    random_quote = random.choice(all_quotes)
    # print(random_quote)

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)

    message = f"Subject:Motivational Quote!\n\n{random_quote}"

    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=message.encode('utf-8'))

