# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:44:26 EDT 2016

@author: nd1

Class for parsing text in voter files converted to csv from pdf.
"""

import re

from datetime import datetime


class Person:
    def __init__(self, voter):
        self.voter = voter

    def __getitem__(self, index):
        # called when a user uses square brackets for indexing
        return self.voter[index]

    @property
    def last_name(voter):
        return voter[0].split(',')[0]

    @property
    def first_name(voter):
        return voter[0].split(',')[1].split()[0]

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
