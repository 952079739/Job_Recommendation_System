import csv


def load_csv(list):
    header = ['user_id', 'position_id', 'score']
    with open('../position.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writerow(list)





