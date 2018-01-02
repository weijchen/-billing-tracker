# -*- coding: utf-8 -*-
'''
Author: Jimmy Chen
PN: Billing Tracker, Created Dec. 2017
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
    def reverse(conn, cat, title, amount):
        cur = conn.cursor()
        sqlstr = "SELECT amount FROM account WHERE title == '{0}'".format(title)
        cur.execute(sqlstr)
        try:
            var = cur.fetchone()
            if cat == 'income':
                adj = var[0] - amount
                sqlstr_update = "UPDATE account SET amount = {0} WHERE title == '{1}';".format(adj, title)
                cur.execute(sqlstr_update)
                conn.commit()
            elif cat == 'expense':
                adj = var[0] + amount
                sqlstr_update = "UPDATE account SET amount = {0} WHERE title == '{1}';".format(adj, title)
                cur.execute(sqlstr_update)
                conn.commit()
            else:
                print("Error input!")
                return 0
        except:
            return False
    def run(conn, id, curMonth, nextMonth, table):
        cur = conn.cursor()
        sqlstr = "SELECT * FROM {1} WHERE id == {0}".format(id, table)
        cur.execute(sqlstr)
        var = cur.fetchall()
        title_, amount_ = var[0][4], var[0][3]
        Delete.reverse(conn, table, title_, amount_)
        if len(var) == 0:
            print("No item {}!".format(id))
        else:
            sqlstr = "DELETE FROM {1} WHERE id = {0}".format(id, table)
            cur.execute(sqlstr)
            print("Item {} is delete!".format(id))
        conn.commit()