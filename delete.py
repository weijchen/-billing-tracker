# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
Ver: 1.2 (finish delete modules)
Link:
Todo: 
''' 
# --------------------------------------------------- libs
import re
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
class Delete(object):
    """docstring for Delete"""
    def __init__(self, arg):
        super(Delete, self).__init__()
        self.arg = arg
    def run(conn, id, curMonth, nextMonth, table):
        cur = conn.cursor()
        sqlstr = "SELECT * FROM {1} WHERE (id == {0})".format(id, table)
        cur.execute(sqlstr)
        var = cur.fetchall()
        if len(var) == 0:
            print("No item {}!".format(id))
        else:
            sqlstr = "DELETE FROM {1} WHERE id = {0}".format(id, table)
            cur.execute(sqlstr)
            print("Item {} is delete!".format(id))
        conn.commit()
    def month_init():
        date_after_month = datetime.datetime.now() + relativedelta(months=1)
        date_ = datetime.datetime.now()
        dam = date_after_month
        return date_, dam
    def show_income(conn, check, curMonth, nextMonth, table):
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
                print("===== {1} list (Month: {0}) =====".format(curMonth, table.capitalize()))
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
                print("===== {1} list (Month: {0}) =====".format(curMonth, table.capitalize()))
                print("--------------------------------------------------------------------------------------")
                print("ID | Date | Time | Amount | Account | Main Category | Sub Category | Details | Invoice")
                print("--------------------------------------------------------------------------------------")
                for idx in range(len(var)):
                    for i in range(len(var[idx])):
                        print(var[idx][i], end=' | ')
                    print("")