import csv

"""
Pas le plus palpitant, on parse le csv 
"""

check_birthday()
    with open('birthday.csv', newline='') as data:
        reader = csv.reader(data, delimiter=',')
        for row in reader:
            print(row[1])

