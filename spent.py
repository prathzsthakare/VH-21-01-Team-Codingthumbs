import sqlite3 as database
from datetime import datetime

def init():
    '''
    Initialize a new database to store the
    expenditures
    '''
    conn = database.connect("spent.db")   #represents the database
    cur = conn.cursor()                   #help u in executing all the sql statements
    sql = '''
    create table if not exists expenses (
        amount number,
        category string,
        message string,
        time string
        )
    '''         #Grocery, Utility, Restaurants, Paper, etc.
    cur.execute(sql)
    conn.commit()

def log(amount, category, message=""):
    '''
    logs the expenditure in the database.
    amount: number
    category: string
    message: (optional) string
    '''
    date = str(datetime.now())
    data = (amount, category, message, date)
    conn = database.connect("spent.database")
    cur = conn.cursor()
    sql = 'INSERT INTO expenses VALUES (?, ?, ?, ?)'
    cur.execute(sql, data)
    conn.commit()

def view(category=None):
    '''
    Returns a list of all expenditure incurred, and the total expense.
    If a category is specified, it only returns info from that
    category
    '''
    conn = database.connect("spent.db")
    cur = conn.cursor()
    if category:
        sql = '''
        select * from expenses where category = '{}'
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses where category = '{}'
        '''.format(category)
    else:
        sql = '''
        select * from expenses
        '''.format(category)
        sql2 = '''
        select sum(amount) from expenses
        '''.format(category)
    cur.execute(sql)
    results = cur.fetchall()
    cur.execute(sql2)
    total_amount = cur.fetchone()[0]

    return total_amount, results
