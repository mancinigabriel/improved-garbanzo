import os
import sqlite3
import pandas as pd

data_url = 'https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv'
headers = ['first_name','last_name','address','city','state','zip']
data_table = pd.read_csv(data_url, header=None, names=headers, converters={'zip': str})

if os.path.exists('example.db'):
    os.remove('example.db')

conn = sqlite3.connect('example.db')

data_table.to_sql('data_table', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'address':'VARCHAR(256)',
    'city':'VARCHAR(256)',
    'state':'VARCHAR(2)',
    'zip':'VARCHAR(5)',
})
