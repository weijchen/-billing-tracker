# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
Ver: 1.4 (finish modify modules)
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
from snippets import *
from modify import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
# class Modify(object):
#     """docstring for Modify"""
#     def __init__(self, arg):
#         super(Modify, self).__init__()
#         self.arg = arg
#     def income():
#         cur = conn.cursor()
        
class Display(object):
    """docstring for Display"""
    def __init__(self, arg):
        super(Display, self).__init__()
        self.arg = arg
    def main():
        print("-------------------")
        print("| Save more Money!|")
        print("-------------------")
        print("1. Enter data")
        print("2. Change data")
        print("3. Show data")
        print("4. Create table")
        print("0. End")
        print("-------------------")
    def enter():
        print("-------------------")
        print("Main -> Enter data ")
        print("-------------------")
        print("1. Enter income")
        print("2. Enter expense")
        print("3. Enter account")
        print("0. End")
        print("-------------------")
    def show():
        print("-------------------")
        print(" Main -> Show data ")
        print("-------------------")
        print("1. Show income")
        print("2. Show expense")
        print("3. Show account")
        print("0. End")
        print("-------------------")
    def income():
        print("-------------------")
        print("   Show -> Income  ")
        print("-------------------")
        print("1. Today")
        print("2. Specific")
        print("3. All")
        print("0. End")
        print("-------------------")
    def expense():
        print("-------------------")
        print("  Show -> Expense  ")
        print("-------------------")
        print("1. Today")
        print("2. Specific")
        print("3. All")
        print("0. End")
        print("-------------------")
    def change():
        print("-------------------")
        print("   Main -> Change  ")
        print("-------------------")
        print("1. Change income")
        print("2. Change expense")
        print("3. Change account")
        print("0. End")
        print("-------------------")
# --------------------------------------------------- Control center
if __name__ == '__main__':
    while True:
        print("")
        Display.main()
        conn = sqlite3.connect('db/money.sqlite')
        choice = int(input("Choose function: "))
        # print("-----------------------------------------")
        # -- 0. Exit program --
        if choice == 0:
            break
        # -- 1. Enter data --
        elif choice == 1:
            while True:
                Display.enter()
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
        # # -- 2. Modify data --
        # elif choice == 2:
        #     while True:
        #         Display.change()
        #         choice = int(input("Choose function: "))
        #         # print("-----------------------------------------")
        #         # -- 2-0. Exit program --
        #         if choice == 0:
        #             break
        #         # -- 2-1. Modify income --
        #         elif choice == 1:
        #             Inc.change(conn)
        #         # -- 2-2. Modify expense --
        #         elif choice == 2:
        #             Mod.run(conn)
        #         # -- 2-3. Modify account --
        #         elif choice == 3:
        #             Mod.run(conn)
        # -- 2. Change data --
        elif choice == 2:
            while True:
                Display.change()
                choice = int(input("Choose function: "))
                # print("-----------------------------------------")
                # -- 3-0. Exit program --
                if choice == 0:
                    break
                # -- 3-1. Delete income --
                elif choice == 1:
                    Inc.change(conn)
                    # Delete.income()
                # -- 3-2. Delete expense --
                elif choice == 2:
                    Exp.change(conn)
                # -- 3-3. Delete account --
                elif choice == 3:
                    Acc.change(conn)
        # -- 3. Show data --
        elif choice == 3:
            while True:
                Display.show()
                choice = int(input("Choose function: "))
                # print("-----------------------------------------")
                # -- 4-0. Exit program --
                if choice == 0:
                    break
                # -- 4-1. Show income --
                elif choice == 1:
                    Display.income()
                    check = int(input("Choose function: "))
                    Show.income(conn, check)
                # -- 4-2. Show expense --
                elif choice == 2:
                    Display.expense()
                    check = int(input("Choose function: "))
                    Show.expense(conn, check)
                # -- 4-3. Show account --
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
            try:
                sqlstr_inc = 'CREATE TABLE income (id TEXT UNIQUE, date DATETIME, time DATETIME, amount NUMERIC, account TEXT, main TEXT, sub TEXT, details TEXT, invoice TEXT)'
                conn.execute(sqlstr_inc)
                conn.commit()
            except Exception as e:
                print(e)
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