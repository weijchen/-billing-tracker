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
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Exp(object):
    """docstring for Exp"""
    def __init__(self, arg):
        super(Exp, self).__init__()
        self.arg = arg
    def delete(conn):
        Exp.show()
        check = int(input("Choose function: "))
        if check == 1:
            cMonth, nMonth = Delete.month_init()
            end = True
            while end == True:
                Delete.show_income(conn, check, cMonth, nMonth, 'expense')
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
                    Delete.run(conn, id_, cMonth, nMonth, 'expense')
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
            Delete.show_income(conn, check, cMonth, nMonth, 'expense')
            print("--------------------------------------------------------------------------------------")
            print("1. Delete")
            print("2. Quit")
            choose = int(input("Choose function: "))
            if choose == 1:
                id_ = int(input("Delete item(id): "))
                Delete.run(conn, id_, cMonth, nMonth, 'expense')
                end = False
            elif choose == 2:
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
            date_, time_ = Exp.get_time(check)
            id_ = Exp.get_id(account, date_, conn)
            amount = int(input("Amount: "))
            print("========================================")
            main = Exp.get_main()
            sub = Exp.get_sub(main)
            details = str(input("Details: ") or "None")
            invoice = str(input("Invoice: ") or "None")
            sqlstr_inc_ent = ("INSERT OR IGNORE INTO expense (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
            deal.append((id_, date_, time_[0:8], amount, account, main, sub, details, invoice))
            conn.executemany(sqlstr_inc_ent, deal)
            conn.commit()
            Acc.adjust(acc, conn, 'expense', amount)
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
        sqlstr = "SELECT Count(*) FROM expense"
        cur.execute(sqlstr)
        var = cur.fetchone()
        return var[0]+1
    def get_main():
        cat = ['Food, Drink', 'Home', 'Traffic', 'Communication', 'Entertainment', 'Education', 'Social', 'Healthcare', 'Finance', 'Other']

        # Display cat
        for idx in range(len(cat)):
            print('{0}. {1} '.format(idx+1, cat[idx]))
            # if idx == 4:
                # print('\n')
        print("----------------------------------------")
        choose = int(input("Which category? "))
        print("========================================")
        print("")
        while int(choose) < 0 and int(choose) > len(cat):
            choose = input("Which category? ")
        else:
            return cat[int(choose)-1]
    def get_sub(main):
        dic = {
            'Food, Drink': {
                '1': 'Breakfast',
                '2': 'Lunch',
                '3': 'Dinner'
            },
            'Home': {
                '1': 'Daily',
                '2': 'Utilities',
                '3': 'Rent'
            },
            'Traffic': {
                '1': 'Public transportation',
                '2': 'Taxi',
                '3': 'Petrol',
                '4': 'Train & Plane',
                '5': 'Motorcycle'
            },
            'Communication': {
                '1': 'Telephone bills',
                '2': 'Mobile fee',
                '3': 'Internet fee',
                '4': 'CableTV fee'
            },
            'Entertainment': {
                '1': 'Sport',
                '2': 'Friend dine',
                '3': 'Casual fun',
                '4': 'Pet',
                '5': 'Travel',
                '6': 'Luxury',
                '7': 'Clothes',
                '8': 'Shoes, Hat'
            },
            'Education': {
                '1': 'Newspaper',
                '2': 'Education',
                '3': 'E-Learning'
            },
            'Social': {
                '1': 'Gifts',
                '2': 'Family fee',
                '3': 'Donations'
            },
            'Healthcare': {
                '1': 'Medical expenses',
                '2': 'Health fee',
                '3': 'Insurance',
                '4': 'Health food',
                '5': 'Beauty wellness'
            },
            'Finance': {
                '1': 'Bank fee',
                '2': 'Installment',
                '3': 'Investment loss',
                '4': 'Tax',
                '5': 'Regulatory fines'
            },
            'Other': {
                '1': 'Other expense',
                '2': 'Lost',
                '3': 'Doubtful loss'

            }
        }
        for key, val in enumerate(dic[main]):
            print('{0}. {1} '.format(key+1, dic[main][val]))
        print("----------------------------------------")
        choose = int(input("Which item? "))
        print("========================================")
        print("")
        while int(choose) < 0 and int(choose)-1 == len(dic[main]):
            choose = input("Which category? ")
        
        return dic[main][str(choose)]