# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
Ver: 1.5 (finish all modules, wait for further optimization)
Link:
Todo: 
''' 
# --------------------------------------------------- libs
import sqlite3
import time, datetime
from datetime import timedelta
import pandas as pd
from income import *
from expense import *
from show import *
from account import *
import snippets as sp
from modify import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Control center
if __name__ == '__main__':
    while True:
        print("")
        sp.Display.main()
        conn = sqlite3.connect('DB of your own'.format(PATH))
        choice = int(input("Choose function: "))
        # print("-----------------------------------------")
        # -- 0. Exit program --
        if choice == 0:
            break
        # -- 1. Enter data --
        elif choice == 1:
            while True:
                sp.Display.enter()
                choice = int(input("Choose function: "))
                # print("-----------------------------------------")
                # -- 1-0. Exit program --
                if choice == 0:
                    break
                # -- 1-1. Enter income --
                elif choice == 1:
                    Inc.enter(conn)
                    input("Press Enter to continue ...")
                # -- 1-2. Enter expense --
                elif choice == 2:
                    Exp.enter(conn)
                    input("Press Enter to continue ...")
                # -- 1-3. Enter account --
                elif choice == 3:
                    Acc.enter(conn)
                    input("Press Enter to continue ...")
        # -- 2. Change data --
        elif choice == 2:
            while True:
                sp.Display.change()
                choice = int(input("Choose function: "))
                # print("-----------------------------------------")
                # -- 2-0. Exit program --
                if choice == 0:
                    break
                # -- 2-1. Change income --
                elif choice == 1:
                    Modify.main(conn, 'income')
                    input("Press Enter to continue ...")
                # -- 2-2. Change expense --
                elif choice == 2:
                    Modify.main(conn, 'expense')
                    input("Press Enter to continue ...")
                # -- 2-3. Change account --
                elif choice == 3:
                    Acc.main(conn)
                    input("Press Enter to continue ...")
        # -- 3. Show data --
        elif choice == 3:
            while True:
                sp.Display.show()
                choice = int(input("Choose function: "))
                # print("-----------------------------------------")
                # -- 3-0. Exit program --
                if choice == 0:
                    break
                # -- 3-1. Show income --
                elif choice == 1:
                    sp.Display.income()
                    check = int(input("Choose function: "))
                    Show.inc_exp(conn, check, 'income')
                # -- 3-2. Show expense --
                elif choice == 2:
                    sp.Display.expense()
                    check = int(input("Choose function: "))
                    Show.inc_exp(conn, check, 'expense')
                # -- 3-3. Show account --
                elif choice == 3:
                    Show.account(conn)
                    input("Press Enter to continue ...")
        # -- 4. Create table --
        elif choice == 4:
            try:
                sqlstr_exp = "CREATE TABLE expense (id TEXT UNIQUE, date TEXT, time DATETIME, amount NUMERIC, account TEXT, main TEXT, sub TEXT, details TEXT, invoice TEXT)"
                conn.execute(sqlstr_exp)
                conn.commit()
            except Exception as e:
                print(e)
            print('-- Table created --')
            try:
                sqlstr_inc = 'CREATE TABLE income (id TEXT UNIQUE, date DATETIME, time DATETIME, amount NUMERIC, account TEXT, main TEXT, sub TEXT, details TEXT, invoice TEXT)'
                conn.execute(sqlstr_inc)
                conn.commit()
            except Exception as e:
                print(e)
            print('-- Table created --')
            try:
                sqlstr_acc = 'CREATE TABLE account (id TEXT UNIQUE, date DATETIME, time DATETIME, title TEXT, initial NUMERIC, amount NUMERIC, details TEXT)'
                conn.execute(sqlstr_acc)
                conn.commit()
            except Exception as e:
                print(e)
            conn.close()
            print('-- Table created --')
        else:
            input("===== Input error, press enter ===== ")
            print("")