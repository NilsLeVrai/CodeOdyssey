import csv
import datetime
import os
import logging

logging.basicConfig(level=logging.ERROR)
filepath = os.path.dirname(os.path.abspath(__file__))

def check_if_task():
    check_today = 0
    check_tomorrow = 0
    today = datetime.datetime.today().strftime("%d-%m")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m")
    with open(os.path.join(filepath, 'birthday.csv'), newline='') as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)
        for row in reader:
            if len(row) >= 3 and 'x' not in row[2][:5]:
                if row[2][:5] == today:
                    check_today = 1
                elif row[2][:5] == tomorrow:
                    check_tomorrow = 2
    return check_today + check_tomorrow

def check_send(check):
    today = datetime.datetime.today().strftime("%d-%m")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m")
    birthday_boys = []  # personnes dont c'est l'anniv aujourd'hui ou demain
    wishing_boys = []   # tout le monde sauf les birthday_boys
    with open(os.path.join(filepath, 'birthday.csv'), newline='') as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)
        for row in reader:
            if len(row) >= 3 and 'x' not in row[2][:5]:
                entry = {'name': row[0], 'id': int(row[1])}
                if row[2][:5] == today or row[2][:5] == tomorrow:
                    birthday_boys.append(entry)
                else:
                    wishing_boys.append(entry)
    return birthday_boys, wishing_boys
