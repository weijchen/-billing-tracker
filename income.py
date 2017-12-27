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
from expense import *
from show import *
from account import *
from delete import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Inc(object):
    """docstring for Inc"""
    def __init__(self, arg):
        super(Inc, self).__init__()
        self.arg = arg
    def delete(conn):
        Inc.show()
        check = int(input("Choose function: "))
        if check == 1:
            cMonth, nMonth = Delete.month_init()
            end = True
            while end == True:
                Delete.show_income(conn, check, cMonth, nMonth, 'income')
                print("--------------------------------------------------------------------------------------")
                print("1. Prev")
                print("2. Back")
                print("3. Delete")
                print("4. Quit")
                choose = int(input("Choose function: "))
                if choose == 1:
                    nMonth = cMonth
                    cMonth -= relativedelta(months=1)
                elif choose == 2:
                    cMonth = nMonth
                    nMonth += relativedelta(months=1)
                elif choose == 3:
                    id_ = int(input("Delete item(id): "))
                    Delete.run(conn, id_, cMonth, nMonth, 'income')
                    end = False
                elif choose == 4:
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
            Delete.show_income(conn, check, cMonth, nMonth, 'income')
            print("--------------------------------------------------------------------------------------")
            print("1. Delete")
            print("2. Quit")
            choose = int(input("Choose function: "))
            if choose == 1:
                id_ = int(input("Delete item(id): "))
                Delete.run(conn, id_, cMonth, nMonth, 'income')
                end = False
            elif choose == 2:
                end = False
            else:
                print("Input error")
    def show():
        print("-------------------")
        print("   Delete -> Income  ")
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
            acc = input("To account (NO., Q to leave): ")
            if acc == 'Q' or acc == 'q':
                return 0
        else:
            account = Acc.account_check(int(acc), conn)
            check = input("Today (Y/N): ")
            date_, time_ = Inc.get_time(check)
            id_ = Inc.get_id(account, date_, conn)
            amount = int(input("Amount: "))
            print("========================================")
            main = Inc.get_main()
            sub = Inc.get_sub(main)
            details = str(input("Details: ") or "None")
            invoice = str(input("Invoice: ") or "None")
            sqlstr_inc_ent = ("INSERT OR IGNORE INTO income (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
            deal.append((id_, date_, time_[0:8], amount, account, main, sub, details, invoice))
            conn.executemany(sqlstr_inc_ent, deal)
            conn.commit()
            Acc.adjust(acc, conn, 'income', amount)
            print("Recorded!\n")
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
    def get_id(account, date, conn):
        cur = conn.cursor()
        sqlstr = "SELECT Count(*) FROM income"
        cur.execute(sqlstr)
        var = cur.fetchone()
        return var[0]+1
    def get_main():
        cat = ['Salary', 'Other income']

        # Display cat
        for idx in range(len(cat)):
            print('{0}. {1} '.format(idx+1, cat[idx]))
        print("----------------------------------------")
        choose = int(input("Which category? "))
        print("========================================")
        print("")
        while choose < 0 and choose > len(cat):
            choose = int(input("Which category? "))
        else:
            return cat[choose-1]
    def get_sub(main):
        dic = {
            'Salary': {
                '1': 'Income',
                '2': 'Interest income',
                '3': 'Part-time',
                '4': 'Bonus income'
            },
            'Other income':{
                '1': 'Gifts income',
                '2': 'Special income',
                '3': 'Investment income',
                '4': 'Adjustment income'
            }
        }
        for key, val in enumerate(dic[main]):
            print('{0}. {1} '.format(key+1, dic[main][val]))
        print("----------------------------------------")
        choose = str(input("Which item? "))
        print("========================================")
        print("")
        while int(choose) < 0 and int(choose)-1 == len(dic[main]):
            choose = str(input("Which item? "))
        return dic[main][choose]