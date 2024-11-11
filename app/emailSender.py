from dotenv import load_dotenv
import os
import smtplib
import datetime

DATE = datetime.datetime.now()

DAY = DATE.strftime("%A")
HOUR = int(DATE.strftime("%H")) * 60
MIN  = int(DATE.strftime("%M"))

load_dotenv('/Users/jakekovinsky/Desktop/WikiWalk/.env')

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')


def sendEmail(name, receiver, content):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        greetings = [f"Good morning {name},", f"Good afternoon {name},", f"Good night {name},"]

        if HOUR >= 0 and (HOUR + MIN <= 60 * 11 + 59):
            greeting = greetings[0]
        elif HOUR >= 12 and (HOUR + MIN <= 60 * 17 + 59):
            greeting = greetings[1]
        else:
            greeting = greetings[2]

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        subject = f"{DAY}'s Article: " + content['title']
        body    = f"{greeting}\n\nHere is your random wikipedia topic for today:\n\n" + content['summary'] + f"\n\nIf you want to read more about {content['title']} follow this link: {content['url']}"
        outro   = f"\n\nKeep learning,\n\nJake Kovinsky"
        msg = f'Subject: {subject}\n\n{body}\n{outro}'

        try:
            encoded_msg = msg.encode("ascii")
            encoded_msg = msg.encode("ascii")
        except UnicodeEncodeError as e:
            print(f"Encoding error: {e}")
            encoded_msg  = msg.encode("utf-8")
            econded_msg   = msg.encode("utf-8")
        
        smtp.sendmail(EMAIL_ADDRESS, receiver, encoded_msg)
        smtp.quit()