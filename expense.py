# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
Link:
Todo: 
''' 
# --------------------------------------------------- libs
import sqlite3
import time, datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
from income import *
from show import *
from account import *
from delete import *
from modify import *
import snippets as sp
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Exp(object):
    """docstring for Exp"""
    def __init__(self, arg):
        super(Exp, self).__init__()
        self.arg = arg
    def change(conn):
        Exp.show()
        check = int(input("Choose function: "))
        if check == 1:
            cMonth, nMonth = Show.month_init()
            end = True
            while end == True:
                print("===== {1} list (Month: {0}) =====".format(str(cMonth)[0:7], 'Income'))
                Show.show_monthly(conn, check, cMonth, nMonth, 'expense')
                print("--------------------------------------------------------------------------------------")
                print("1. Prev")
                print("2. Back")
                print("3. Modify")
                print("4. Delete")
                print("5. Quit")
                choose = int(input("Choose function: "))
                if choose == 1:
                    nMonth = cMonth
                    cMonth -= relativedelta(months=1)
                elif choose == 2:
                    cMonth = nMonth
                    nMonth += relativedelta(months=1)
                elif choose == 3:
                    id_ = int(input("Modify item(id): "))
                    Modify.run(conn, id_, cMonth, nMonth, 'expense')
                elif choose == 4:
                    id_ = int(input("Delete item(id): "))
                    Delete.run(conn, id_, cMonth, nMonth, 'expense')
                elif choose == 5:
                    end = False
                else:
                    print("Input error")
        elif check == 2:
            cyear = int(input("Which year: "))
            nyear = cyear
            cmonth = int(input("Which month: "))
            nmonth = cmonth + 1
            if nmonth > 12:
                nyear += 1
                nmonth = 1
            cMonth = str(cyear)+'-'+str(cmonth)
            nMonth = str(nyear)+'-'+str(nmonth)
            print("===== {1} list (Month: {0}) =====".format(str(cMonth)[0:7], 'Income'))
            Show.show_monthly(conn, check, cMonth, nMonth, 'expense')
            print("--------------------------------------------------------------------------------------")
            print("1. Modify")
            print("2. Delete")
            print("3. Quit")
            choose = int(input("Choose function: "))
            if choose == 1:
                id_ = int(input("Delete item(id): "))
                Modify.run(conn, id_, cMonth, nMonth, 'expense')
                end = False
            elif choose == 2:
                id_ = int(input("Delete item(id): "))
                Delete.run(conn, id_, cMonth, nMonth, 'expense')
                end = False
            elif choose == 3:
                end = False
            else:
                print("Input error")
    def show():
        print("-------------------")
        print("   Delete -> Expense  ")
        print("-------------------")
        print("1. Monthly")
        print("2. Specific month")
        print("0. End")
        print("-------------------")

    def enter(conn):
        deal = []
        Show.account(conn)

        acc = input("To account (No.): ")
        while (Acc.account_check(int(acc), conn) == False):
            print("Title not exist!")
            acc = input("To account (No., Q to leave): ")
            if acc == 'Q' or acc == 'q':
                return 0
        else:
            account = Acc.account_check(int(acc), conn)
            check = input("Today? (Y/N): ")
            date_, time_ = sp.Tools.get_time(check)
            id_ = sp.Tools.get_id(account, 'expense', conn)
            amount = int(input("Amount: "))
            print("========================================")
            main = sp.Category_exp.get_main()
            sub = sp.Category_exp.get_sub(main)
            details = str(input("Details: ") or "None")
            invoice = str(input("Invoice: ") or "None")
            sqlstr_inc_ent = ("INSERT OR IGNORE INTO expense (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
            deal.append((id_, date_, time_[0:8], amount, account, main, sub, details, invoice))
            conn.executemany(sqlstr_inc_ent, deal)
            conn.commit()
            Acc.adjust(acc, conn, 'expense', amount)
            print("Recorded!\n")