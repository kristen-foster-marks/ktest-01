import csv

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if "orphan_status_id" in row[4]:
            print(f'\ncommit_id: {row[3]} | {row[4]} | audit: {row[5][0:10]} | author_locale_date: {row[7][0:10]} | sha: {row[8]}')
    
    print('\n')


with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if "orphan_status_id" in row[4]:
            print(f'\ncommit_id: {row[3]} | {row[4]} | audit: {row[5][0:10]} | author_locale_date: {row[7][0:10]} | sha: {row[8]}')
    
    print('\n')

with open('test.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if "orphan_status_id" in row[4]:
            print(f'\ncommit_id: {row[3]} | {row[4]} | audit: {row[5][0:10]} | author_locale_date: {row[7][0:10]} | sha: {row[8]}')
    
    print('\n')