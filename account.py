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
import pandas as pd
from income import *
from expense import *
from show import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Acc(object):
    """docstring for Acc"""
    def __init__(self, arg):
        super(Acc, self).__init__()
        self.arg = arg
    def adjust(check, conn, cat, num):
        cur = conn.cursor()
        sqlstr_get = "SELECT amount FROM account WHERE id = '{0}';".format(check)
        cur.execute(sqlstr_get)
        try:
            var = cur.fetchone()
            if cat == 'income':
                adj = var[0] + num
                cur = conn.cursor()
                sqlstr_update = "UPDATE account SET amount = {0} WHERE id = '{1}';".format(adj, check)
                cur.execute(sqlstr_update)
                conn.commit()
            elif cat == 'expense':
                adj = var[0] - num
                cur = conn.cursor()
                sqlstr_update = "UPDATE account SET amount = {0} WHERE id = '{1}';".format(adj, check)
                cur.execute(sqlstr_update)
                conn.commit()
            else:
                print("Error input!")
                return 0
        except:
            return False
    def enter(conn):
        accs = []
        id_ = Acc.get_account_length(conn)+1
        date_, time_ = str(datetime.datetime.now()).split(" ")[0], str(datetime.datetime.now()).split(" ")[1]
        title = input("Enter account name: ")
        while (Acc.account_check(str(title), conn) == True):
            print("Title existed!")
            title = input("Enter account name (Q to leave): ")
            if title == 'Q' or title == 'q':
                return 0
        else:
            initial = int(input("Init value: ") or 0)
            amount = initial
            details = str(input("Details: ") or "None")
            accs.append((id_, date_, time_, title, initial, amount, details))
            sqlstr_acc_ent = ("INSERT OR IGNORE INTO account (id, date, time, title, initial, amount, details) VALUES (?,?,?,?,?,?,?)")
            conn.executemany(sqlstr_acc_ent, accs)
            conn.commit()
            print("Recorded!\n")
    def account_check(check, conn):
        '''check the existence of particular account'''
        if type(check) == int:
            '''income() by int to choose account'''
            cur = conn.cursor()
            sqlstr = "SELECT title FROM account WHERE id = '{0}';".format(check)
            cur.execute(sqlstr)
            try:
                var = cur.fetchone()
                return var[0]
            except:
                return False
        if type(check) == str:
            '''account() by string'''
            cur = conn.cursor()
            sqlstr = "SELECT title FROM account WHERE title = '{0}';".format(check)
            cur.execute(sqlstr)
            try:
                var = cur.fetchone()
                return (len(var) >= 1)
            except:
                return False
    def get_account_length(conn):
        cur = conn.cursor()
        sqlstr = "SELECT Count(*) FROM account;"
        cur.execute(sqlstr)
        var = cur.fetchone()
        return var[0]