# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:44:26 EDT 2016

@author: nd1

Class for parsing text in voter files converted to csv from pdf.
"""

import re

from datetime import datetime


class Person:
    #seperate a row from the voter csv file into its components
    def __init__(self, voter):
        if voter is None:
            voter = []
        self.voter = voter
        self.data = voter
        self.__data__len = len(voter)

    def __getitem__(self, index):
        # called when a user uses square brackets for indexing
        return self.voter[index]

    def __len__(self):
        return self.__data__len

    @property
    def last_name(voter):
        return voter[0].split(',')[0]

    @property
    def first_name(voter):
        street_num = ([s for s in voter[0].split(',')[1].split() if s.isdigit()][0])
        return voter[0].split(',')[1].split(street_num)[0]

    @property
    def address(voter):
        street_num = ([s for s in voter[0].split(',')[1].split() if s.isdigit()][0])
        return (street_num + (voter[0].split(',')[1].split(street_num)[1]))

    @property
    def zip_code(voter):
        return voter[0].split(',')[2]

    @property
    def registration_date(voter):
        text_date = re.sub('[\s+]', '', voter[1])
        return datetime.strptime(text_date, '%d-%b-%y').date()

    @property
    def party(voter):
        return voter[2]

    @property
    def precinct(voter):
        return voter[3]

    @property
    def ward(voter):
        return voter[4]

    @property
    def smd(voter):
        return voter[5]

    @property
    def voted(voter):
        return voter[6:11]
