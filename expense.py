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
    def enter(conn):
        deal = []
        Show.account(conn)

        acc = input("To account (ID.): ")
        while (Acc.account_check(int(acc), conn) == False):
            print("Title not exist!")
            acc = input("To account (ID., Q to leave): ")
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
            print("========================================")
            sub = sp.Category_exp.get_sub(main)
            details = str(input("Details: ") or "None")
            invoice = str(input("Invoice: ") or "None")
            sqlstr_inc_ent = ("INSERT OR IGNORE INTO expense (id, date, time, amount, account, main, sub, details, invoice) VALUES (?,?,?,?,?,?,?,?,?)")
            deal.append((id_, date_, time_[0:8], amount, account, main, sub, details, invoice))
            conn.executemany(sqlstr_inc_ent, deal)
            conn.commit()
            Acc.adjust(acc, conn, 'expense', amount)
            print("Recorded!\n")