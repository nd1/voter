# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:44:26 EDT 2016

@author: nd1

Script to run parsing of multiple csv files and write out to one file.
"""

import csv
import sys

from models.person import Person

def csv_compilation():
    with open ('./csv/0001-1000.csv') as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        writer = csv.writer(sys.stdout)
        for row in r:
            person = Person(row)
            if row[0].split(',')[0] == "VOTER'S NAME AND RESIDENCE":
                continue
            else:
                #print(row[0].split(',')[1].split())
                print (row)
                print (row[0].split(',')[1].split()[0])
                print(person.last_name, person.first_name)
                '''writer.writerow([
                person.last_name,
                person.zip_code,
                person.registration_date,
                person.party,
                person.precinct,
                person.ward,
                person.smd,
                person.voted[0],
                person.voted[1],
                person.voted[2],
                person.voted[3],
                person.voted[4]
                ])'''

if __name__ == '__main__':
    csv_compilation()
