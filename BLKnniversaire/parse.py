import csv
import datetime
import os
import logging

"""
Pas le plus palpitant, on parse le csv
"""
logging.basicConfig(level=logging.ERROR) 
filepath = os.path.dirname(os.path.abspath(__file__))

def check_birthday():
    tomorrow_birthday = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m")
    birthday_boys = []
    wishing_boys = []
    with open(os.path.join(filepath, 'birthday.csv'), newline='') as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)
        for row in reader:
            if len(row) >= 3:
                if row[2][:5] == tomorrow_birthday:
                    birthday_boys.append(row[0])
                else:
                    wishing_boys.append(row[0])
    return birthday_boys, wishing_boys
