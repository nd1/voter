# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:44:26 EDT 2016

@author: nd1

Script to run parsing of multiple csv files and write out to one file.

CURRENT STATUS- script incomplete. parsing the field with name and address.
"""

import csv
import os
import sys

from models.person import Person

def csv_compilation(csv_file):
    with open ('./data/' + csv_file) as csvfile:
        r = csv.reader(csvfile, delimiter=',')
        fields = ['last_name', 'first_name', 'middle_initial', 'suffix', 'address', 'zip_code', 'registration_date', 'party', 'precinct', 'ward', 'smd', 'election_0415', 'election_1114', 'election_0414', 'election_0413', 'election_1112']
        for row in r:
            person = Person(row)
            if row[0].split(',')[0] == "VOTER'S NAME AND RESIDENCE":
                continue
            else:
                with open('./data/dc_voter_file.csv', 'a') as f:
                    writer = csv.writer(f)
                    writer.writerow([
                    person.last_name,
                    person.first_name,
                    person.address,
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
                    ])

if __name__ == '__main__':
    for root, dirs, files in os.walk('data'):
        for name in files:
            if name.endswith('.csv'):
                csv_compilation(name)
