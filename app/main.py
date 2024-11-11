from generator import fetchPage
from emailSender import sendEmail
import csv

if __name__ == "__main__":
    user_base = []
    with open('./testing/test_db.csv', mode ='r') as file:
        db_csv = csv.reader(file)
        for idx, row in enumerate(db_csv):
            if idx == 0:
                continue
            user_base.append(row)
    
    for user in user_base:
        wiki_page = fetchPage()
        records = {'email' : user[2], 'article_title' : wiki_page['title'], 'article_url' : wiki_page['url']}
        with open('hist.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(records.values())

        sendEmail(user[1], user[2], wiki_page)