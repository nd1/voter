'''
incomplete script- working on a way to parse in pandas
'''

import os
import pandas as pd

from datetime import datetime


def create_df():
    # create one dataframe from the csv files, drop the rows with header
    # data from the conversion process. update header row.
    df = pd.DataFrame()
    for root, dirs, files in os.walk('data'):
        for name in files:
            if name.endswith('.csv'):
                df = df.append(pd.read_csv(('./data/' + name), header=None))
                print("appended {!s}".format(name))

    df.columns = ['voter', 'registration_date', 'party', 'precinct',
                  'ward', 'smd', 'election_0415', 'election_1114',
                  'election_0714', 'election_0414', 'election_0413',
                  'election_1112']
    df = df[df.voter != "VOTER'S NAME AND RESIDENCE"]
    return df


def format_date(reg_date):
    reg_date = reg_date.str.replace(r'\s+', '')
    reg_date = pd.to_datetime(pd.Series(reg_date), format='%d-%b-%y')
    return reg_date


def parse_name(voter_data):
    last_name = voter_data.str.split(',').str[0]
    first_name = voter_data.str.split(',').str[1].str.split(' ').str[1]
    initial = voter_data.str.split(',').str[1].str.split(' ').str[2]
    return last_name, first_name, initial


def parse_address(voter_data):
    zip_code = voter_data.str.split(',').str[2]
    data = voter_data.str.split(',').str[1].str.split(' ').str[3:]
    print(data.str[0])


def compile_csv():
    voters = create_df()
    voters.registration_date = format_date(voters.registration_date)
    voters['last_name'], voters['first_name'], voters['initial'],  =
    parse_name(voters.voter)
    voters['address'], voters['zip_code'] = parse_address(voters.voter)
    print(voters.shape)
    print(voters.head())

if __name__ == '__main__':
    compile_csv()
