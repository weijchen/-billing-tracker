# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
Ver: 1.1 (building enter modules)
Link:
Todo: 
''' 
# --------------------------------------------------- libs
import sqlite3
import re
import time, datetime
from datetime import timedelta
import pandas as pd
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Exp(object):
    """docstring for Exp"""
    def __init__(self, arg):
        super(Exp, self).__init__()
        self.arg = arg
    def enter():
        deal = []
        Show.account()
        check = str(input("To account: "))
        while (Enter.account_check(int(check)) == False):
            print("Title not exist!")
            check = str(input("To account(Q to leave): "))
            if check == 'Q' or 'q':
                return 0
        else:
            account = Enter.account_check(check)

        check = str(input("Today? (Y/N): "))
        date_, time_ = Enter.get_time(check)
        # print(type(Enter.get_id(account, date_)))

        id_ = Enter.get_id(account, date_)
        # print(id_)

        amount = int(input("Amount: "))
        main = Enter.get_main()
        sub = Enter.get_sub(main)
        details = str(input("Details: "))
        if len(details) == 0:
            details = "None"
        invoice = str(input("Invoice: "))
        if len(invoice) == 0:
            invoice = "None"
        
        # date = [_ for _ in datetime.fromtimestamp(js['t'][idx]).strftime("%Y,%m,%d,%H:%M:%S,%a").split(',')]
        # year, month, day, time, weekday = date[0], date[1], date[2], date[3], date[4]
        # id_ = str(ticker)+year+month+day
        # print(id_, year, month, day, time, weekday, volumn, open_, high, low, close, change)
        sqlstr_inc_ent = ("INSERT OR IGNORE INTO income (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
        deal.append((id_, date_, time_, amount, account, main, sub, details, invoice))
        conn.executemany(sqlstr_inc_ent, deal)
        conn.commit()

        # Count the number of records:
        # SELECT COUNT(*) FROM your_table_name
    def get_time(check):
        if check == 'Y' or check == 'y':
            out_1, out_2 = str(datetime.datetime.now()).split(" ")[0], str(datetime.datetime.now()).split(" ")[1]
        else:
            year = str(input("Which year? ")) 
            month = str(input("Which month? ")) 
            day = str(input("Which day? "))
            time = str(datetime.datetime.now()).split(" ")[1]

            out_1 = year+"-"+month+"-"+day
            out_2 = time
        return out_1, out_2
    def get_id(account, date):
        cur = conn.cursor()
        sqlstr = "SELECT Count(*) FROM income"
        cur.execute(sqlstr)
        var = cur.fetchone()
        print(var)

        return var[0]+1
    def get_main():
        cat = ['Food', 'Trafic']

        # Display cat
        for idx in range(len(cat)):
            print('{}.{} '.format(idx+1, cat[idx]), end=' ')
        print("")

        choose = int(input("Which category? "))
        while choose < 0 and choose > len(cat):
            choose = int(input("Which category? "))
        else:
            return cat[choose-1]
    def get_sub(main):
        dic = {
            'Food': {
                '1': 'Breakfast',
                '2': 'Lunch',
                '3': 'Dinner'
            },
            'Trafic':{
                '1': 'Motorcycle',
                '2': 'Gasoline'
            }
        }
        for key, val in enumerate(dic[main]):
            print('{}.{} '.format(key+1, dic[main][val]), end=' ')

        choose = str(input("Which item? "))
        # print(len(dic[main]))
        while int(choose) < 0 and int(choose)-1 == len(dic[main]):
            choose = str(input("Which category? "))
        return dic[main][choose]

class Acc(object):
    """docstring for Acc"""
    def __init__(self, arg):
        super(Acc, self).__init__()
        self.arg = arg
    def enter(check):
        try:
            sqlstr = "SELECT title FROM account WHERE title = {}".format(check)
            n = conn.execute(sqlstr)
        except Exception as e:
            print(e)
        def account():
        accs = []
        id_ = Enter.get_account_length()+1
        date_, time_ = str(datetime.datetime.now()).split(" ")[0], str(datetime.datetime.now()).split(" ")[1]
        title = str(input("Enter account name: "))
        while (Enter.account_check(title) == True):
            print("Title already exist!")
            title = str(input("Enter account name: "))
        amount = int(input("Init value: "))
        details = str(input("Details: "))
        if len(details) == 0:
            details = "None"

        accs.append((id_, date_, time_, title, amount, details))
        # print(accs)

        sqlstr_acc_ent = ("INSERT OR IGNORE INTO account (id, date, time, title, amount, details) VALUES (?,?,?,?,?,?)")
        conn.executemany(sqlstr_acc_ent, accs)
        conn.commit()
    def account_check(check):
        '''check the existence of particular account'''
        if type(check) == int:
            '''income() by int to choose account'''
            cur = conn.cursor()
            sqlstr = "SELECT title FROM account WHERE id = '{}';".format(check)
            cur.execute(sqlstr)
            try:
                var = cur.fetchone()
                return var[0]
            except:
                return False
        if type(check) == str:
            '''account() by string'''
            cur = conn.cursor()
            sqlstr = "SELECT title FROM account WHERE title = '{}';".format(check)
            cur.execute(sqlstr)
            try:
                var = cur.fetchone()
                return (len(var) >= 1)
            except:
                return False
    def get_account_length():
        cur = conn.cursor()
        sqlstr = "SELECT Count(*) FROM account;"
        cur.execute(sqlstr)
        var = cur.fetchone()
        return var[0]

class Inc(object):
    """docstring for Enter"""
    def __init__(self, arg):
        super(Enter, self).__init__()
        self.arg = arg
    def enter():
        deal = []
        Show.account()
        check = str(input("To account: "))
        while (Enter.account_check(int(check)) == False):
            print("Title not exist!")
            check = str(input("To account(Q to leave): "))
            if check == 'Q' or 'q':
                return 0
        else:
            account = Enter.account_check(check)

        check = str(input("Today? (Y/N): "))
        date_, time_ = Enter.get_time(check)
        # print(type(Enter.get_id(account, date_)))

        id_ = Enter.get_id(account, date_)
        # print(id_)

        amount = int(input("Amount: "))
        main = Enter.get_main()
        sub = Enter.get_sub(main)
        details = str(input("Details: "))
        if len(details) == 0:
            details = "None"
        invoice = str(input("Invoice: "))
        if len(invoice) == 0:
            invoice = "None"
        
        # date = [_ for _ in datetime.fromtimestamp(js['t'][idx]).strftime("%Y,%m,%d,%H:%M:%S,%a").split(',')]
        # year, month, day, time, weekday = date[0], date[1], date[2], date[3], date[4]
        # id_ = str(ticker)+year+month+day
        # print(id_, year, month, day, time, weekday, volumn, open_, high, low, close, change)
        sqlstr_inc_ent = ("INSERT OR IGNORE INTO income (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
        deal.append((id_, date_, time_, amount, account, main, sub, details, invoice))
        conn.executemany(sqlstr_inc_ent, deal)
        conn.commit()

        # Count the number of records:
        # SELECT COUNT(*) FROM your_table_name
    def get_time(check):
        if check == 'Y' or check == 'y':
            out_1, out_2 = str(datetime.datetime.now()).split(" ")[0], str(datetime.datetime.now()).split(" ")[1]
        else:
            year = str(input("Which year? ")) 
            month = str(input("Which month? ")) 
            day = str(input("Which day? "))
            time = str(datetime.datetime.now()).split(" ")[1]

            out_1 = year+"-"+month+"-"+day
            out_2 = time
        return out_1, out_2
    def get_id(account, date):
        cur = conn.cursor()
        sqlstr = "SELECT Count(*) FROM income"
        cur.execute(sqlstr)
        var = cur.fetchone()
        print(var)

        return var[0]+1
    def get_main():
        cat = ['Food', 'Trafic']

        # Display cat
        for idx in range(len(cat)):
            print('{}.{} '.format(idx+1, cat[idx]), end=' ')
        print("")

        choose = int(input("Which category? "))
        while choose < 0 and choose > len(cat):
            choose = int(input("Which category? "))
        else:
            return cat[choose-1]
    def get_sub(main):
        dic = {
            'Food': {
                '1': 'Breakfast',
                '2': 'Lunch',
                '3': 'Dinner'
            },
            'Trafic':{
                '1': 'Motorcycle',
                '2': 'Gasoline'
            }
        }
        for key, val in enumerate(dic[main]):
            print('{}.{} '.format(key+1, dic[main][val]), end=' ')

        choose = str(input("Which item? "))
        # print(len(dic[main]))
        while int(choose) < 0 and int(choose)-1 == len(dic[main]):
            choose = str(input("Which category? "))
        return dic[main][choose]

class Show(object):
    """docstring for Show"""
    def __init__(self, arg):
        super(Show, self).__init__()
        self.arg = arg
    
    def account():
        cur = conn.cursor()
        sqlstr = "SELECT title FROM account;"
        cur.execute(sqlstr)
        # try:
        var = cur.fetchall()
        if len(var) == 0:
            print("No account created!")
        else:
            for idx in range(len(var)):
                print('{}.{} '.format(idx+1, var[idx][0]), end=' ')
            print("")
    def income():
        cur = conn.cursor()
        sqlstr = ("SELECT * FROM income ORDER BY date ASC, time ASC;")
        cur.execute(sqlstr)
        # try:
        var = cur.fetchall()
        if len(var) == 0:
            print("No account created!")
        else:
            for idx in range(len(var)):
                print(var[idx])
            print("")

class Modify(object):
    """docstring for Modify"""
    def __init__(self, arg):
        super(Modify, self).__init__()
        self.arg = arg
    def income():
        cur = conn.cursor()
        
class Display(object):
    """docstring for Display"""
    def __init__(self, arg):
        super(Display, self).__init__()
        self.arg = arg

    def main():
        print("-------------------")
        print("Save some Money!")
        print("-------------------")
        print("1. Create table")
        print("2. Enter data")
        print("3. Modify data")
        print("4. Show data")
        print("5. Delete data")
        print("0. End")
        print("-------------------")

    def enter():
        print("-------------------")
        print("Enter data")
        print("-------------------")
        print("1. Enter income")
        print("2. Enter expense")
        print("3. Enter account")
        print("0. End")
        print("-------------------")

    def modify():
        print("-------------------")
        print("Modify data")
        print("-------------------")
        print("1. Modify income")
        print("2. Modify expense")
        print("3. Modify account")
        print("0. End")
        print("-------------------")

    def show():
        print("-------------------")
        print("Show data")
        print("-------------------")
        print("1. Show income")
        print("2. Show expense")
        print("3. Show account")
        print("0. End")
        print("-------------------")

# --------------------------------------------------- Control center
if __name__ == '__main__':
    while True:
        Display.main()
        conn = sqlite3.connect('db/money.sqlite')
        choice = int(input("Choose function: "))
        print("-----------------------------------------")
        # -- 0. Exit program --
        if choice == 0:
            break
        # -- 1. Create table --
        elif choice == 1:
            try:
                sqlstr_exp = "CREATE TABLE expense (id TEXT UNIQUE, date TEXT, time DATETIME, amount NUMERIC, account TEXT, main TEXT, sub TEXT, details TEXT, invoice TEXT)"
                conn.execute(sqlstr_exp)
                conn.commit()
            except Exception as e:
                print(e)
            try:
                sqlstr_inc = 'CREATE TABLE income (id TEXT UNIQUE, date DATETIME, time DATETIME, amount NUMERIC, account TEXT, main TEXT, sub TEXT, details TEXT, invoice TEXT)'
                conn.execute(sqlstr_inc)
                conn.commit()
            except Exception as e:
                print(e)
            try:
                sqlstr_acc = 'CREATE TABLE account (id TEXT UNIQUE, date DATETIME, time DATETIME, title TEXT, amount NUMERIC, details TEXT)'
                conn.execute(sqlstr_acc)
                conn.commit()
            except Exception as e:
                print(e)
            conn.close()
            print('-- Table created --')
        # -- 2. Enter data --
        elif choice == 2:
            Display.enter()
            choice = int(input("Choose function: "))
            print("-----------------------------------------")
            # -- 2-0. Exit program --
            if choice == 0:
                break
            # -- 2-1. Enter income --
            elif choice == 1:
                Inc.enter()
                # conn.close()
            # -- 2-2. Enter expense --
            elif choice == 2:
                Exp.enter()
            # -- 2-3. Enter account --
            elif choice == 3:
                Acc.enter()
        # -- 3. Modify data --
        elif choice == 3:
            Display.modify()
            choice = int(input("Choose function: "))
            print("-----------------------------------------")
            # -- 4-0. Exit program --
            if choice == 0:
                break
            # -- 4-1. Show income --
            elif choice == 1:
                Modify.income()
            # -- 4-2. Show expense --
            elif choice == 2:
                pass
            # -- 4-3. Show all --
            elif choice == 3:
                pass
        # -- 4. Show data --
        elif choice == 4:
            Display.show()
            choice = int(input("Choose function: "))
            print("-----------------------------------------")
            # -- 4-0. Exit program --
            if choice == 0:
                break
            # -- 4-1. Show income --
            elif choice == 1:
                Show.income()
            # -- 4-2. Show expense --
            elif choice == 2:
                pass
            # -- 4-3. Show all --
            elif choice == 3:
                pass