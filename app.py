# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracking, Created Dec. 2017
Ver: 1.0 (project start)
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
class Enter(object):
    """docstring for Enter"""
    def __init__(self, arg):
        super(Enter, self).__init__()
        self.arg = arg
    def income():
        # display all account
        check = int(input("To account: "))
        account = get_account(check)
        # check accessability of this account
        check = str(input("Today? (Y/N)"))
        date_ = self.get_time(check)
        id_ = date_+account+
        amount = int(input("Amount: "))
        primary = self.get_primary()
        secondary = self.get_secondary()
        details = str(input("Details: "))
        invoice = str(input("Invoice: "))


        sqlstr = "SELECT TABLE income ()"
        sqlstr_inc_ent = ("INSERT OR IGNORE INTO income (id, date_, amount, account, primary, secondary, details, invoice) VALUES (?,?,?,?,?,?,?)")

    def get_account(check):
        try:
            sqlstr = "SELECT TABLE account ()"
        except Exception as e:
            print(e)

    def get_time(check):
        if check == 'Y' or check == 'y':
            out = str(datetime.datetime.now())
        else:
            out = str(input("Which day? "))
        return out

    def get_primary():
        pass
    def get_secondary():
        pass


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

    # def modify():
    #     print("-------------------")
    #     print("Modify data")
    #     print("-------------------")
    #     print("1. Enter income")
    #     print("2. Enter expense")
    #     print("3. Enter account")
    #     print("0. End")
    #     print("-------------------")
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
                sqlstr_exp = 'CREATE TABLE expense (id TEXT UNIQUE, date_ TEXT, amount NUMERIC, account TEXT, primary TEXT, secondary TEXT, details TEXT, invoice TEXT)'
                conn.execute(sqlstr_exp)
                conn.commit()
            except Exception as e:
                print(e)
            try:
                sqlstr_inc = 'CREATE TABLE income (id TEXT UNIQUE, date_ TEXT, amount NUMERIC, account TEXT, primary TEXT, secondary TEXT, details TEXT, invoice TEXT)'
                conn.execute(sqlstr_inc)
                conn.commit()
            except Exception as e:
                print(e)
            try:
                sqlstr_acc = 'CREATE TABLE account (id TEXT UNIQUE, date_ TEXT, title TEXT, amount NUMERIC, details TEXT)'
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
                Enter.income()

                print("-- Crawl Comp: {} --".format(tickr))
                try:
                    crawler(tickr)
                except Exception as e:
                    print(e)
                conn.close()
            # -- 2-2. Enter expense --
            elif choice == 2:
                for row in querylis:
                    time.sleep(0.5)
                    tickr, comp_name = row[0], row[1]
                    conn = sqlite3.connect('db/{}.sqlite'.format(tickr))
                    print("-- Crawl Comp: {} --".format(tickr))
                    try:
                        crawler(tickr)
                    except Exception as e:
                        print(e)
                    conn.close()
            # -- 2-3. Enter account --
            elif choice == 2:
                for row in querylis:
                    time.sleep(0.5)
                    tickr, comp_name = row[0], row[1]
                    conn = sqlite3.connect('db/{}.sqlite'.format(tickr))
                    print("-- Crawl Comp: {} --".format(tickr))
                    try:
                        crawler(tickr)
                    except Exception as e:
                        print(e)
                    conn.close()
        # # -- 3. Modify data --
        # elif choice == 3:
        #     disp_menu_3()
        #     choice = int(input("Choose function: "))
        #     print("-----------------------------------------")
        #     # -- 3-0. Exit program --
        #     if choice == 0:
        #         break
        #     # -- 3-1. Clear table (single) --
        #     elif choice == 1:
        #         tickr = str(input("Clear which company? "))
        #         confirm = str(input("Delete {}? (Y/N) ".format(comp_name)))
        #         if confirm == 'Y' or confirm == 'y':
        #             conn = sqlite3.connect('db/{}.sqlite'.format(tickr))
        #             sqlstr = 'DELETE * from info'
        #             cursor = conn.execute(sqlstr)
        #             conn.execute(sqlstr)
        #             conn.commit()
        #         print('-- Tables is cleared --')
        #     # -- 3-2. Clear table (all) --
        #     elif choice == 2:
        #         confirm = str(input("Clear all tables? (Y/N) "))
        #         if confirm == 'Y' or confirm == 'y':
        #             for row in querylis:
        #                 tickr = row[0]
        #                 conn = sqlite3.connect('db/{}.sqlite'.format(tickr))
        #                 sqlstr = 'DELETE * from info'
        #                 cursor = conn.execute(sqlstr)
        #                 conn.execute(sqlstr)
        #                 conn.commit()
        #         print('-- Tables are cleared --')