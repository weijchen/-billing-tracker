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
from expense import *
from account import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Show(object):
    """docstring for Show"""
    def __init__(self, arg):
        super(Show, self).__init__()
        self.arg = arg
    def account(conn):
        cur = conn.cursor()
        sqlstr = "SELECT title, amount, details FROM account;"
        cur.execute(sqlstr)
        var = cur.fetchall()
        if len(var) == 0:
            print("No account created!")
            input("Press Enter to continue ...")
        else:
            print("===== Account list =====")
            print("No.\tTilte\tAmount\tDetails")
            for idx in range(len(var)):
                print('{0}\t{1}\t{2}\t{3} '.format(idx+1, var[idx][0], var[idx][1], var[idx][2]))
            print("")
    def show_monthly(conn, check, curMonth, nextMonth, table):
        curMonth = str(curMonth).split(" ")[0][0:7]
        nextMonth = str(nextMonth).split(" ")[0][0:7]
        if check == 1:
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM {2} WHERE (date >= '{0}' and date< '{1}') ORDER BY date ASC, time ASC;".format(curMonth, nextMonth, table))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
        elif check == 2:
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM {2} WHERE (date >= '{0}' and date< '{1}') ORDER BY date ASC, time ASC;".format(curMonth, nextMonth, table))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
    def income(conn, check):
        if check == 1:
            date_ = str(datetime.datetime.now()).split(" ")[0]
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM income WHERE date = '{0}' ORDER BY date ASC, time ASC;".format(date_))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Income list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        elif check == 2:
            year = str(input("Which year: "))
            month = str(input("Which month: "))
            day = str(input("Which day: "))
            date_ = year+'-'+month+'-'+day
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM income WHERE date = '{0}' ORDER BY date ASC, time ASC;".format(date_))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Income list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        elif check == 3:
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM income ORDER BY date ASC, time ASC;")
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Income list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        else:
            print("Input error")
            input("Press Enter to continue ...")
            return 0
    def expense(conn, check):
        if check == 1:
            date_ = str(datetime.datetime.now()).split(" ")[0]
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM expense WHERE date = '{0}' ORDER BY date ASC, time ASC;".format(date_))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Expense list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        elif check == 2:
            year = str(input("Which year: "))
            month = str(input("Which month: "))
            day = str(input("Which day: "))
            date_ = year+'-'+month+'-'+day
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM expense WHERE date = '{0}' ORDER BY date ASC, time ASC;".format(date_))
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Expense list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        elif check == 3:
            cur = conn.cursor()
            sqlstr = ("SELECT * FROM expense ORDER BY date ASC, time ASC;")
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                print("No account created!")
            else:
                print("===== Expense list =====")
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")
            input("Press Enter to continue ...")
            print("")
        else:
            print("Input error")
            input("Press Enter to continue ...")
            return 0
    def month_init():
        date_after_month = datetime.datetime.now() + relativedelta(months=1)
        date_ = datetime.datetime.now()
        dam = date_after_month
        return date_, dam
    