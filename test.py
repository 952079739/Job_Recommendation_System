import csv
import random


def randon_password():
    password = random.randrange(1000, 3000, 10)
    return password


headers = ['company_id', 'company_name', 'company_email', 'company_photo', 'company_password']
company_list = []
with open('/Users/zmns/PycharmProjects/Job_Recommendation_System/job.csv', 'r') as f:
    reader = csv.reader(f)
    for reading in reader:
        company_list.append({'company_id': reading[0],
                             'company_name': reading[5],
                             'company_email': '{}@123.com'.format(randon_password()),
                             'company_photo':  '',
                             'company_password': randon_password()})

with open('../company.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(company_list)