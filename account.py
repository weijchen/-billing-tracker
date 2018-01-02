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
from show import *
from income import *
from expense import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Acc(object):
    """docstring for Acc"""
    def __init__(self, arg):
        super(Acc, self).__init__()
        self.arg = arg
    def delete(conn, id):
        cur = conn.cursor()
        sqlstr = "SELECT * FROM account WHERE id == '{0}'".format(id)
        cur.execute(sqlstr)
        var = cur.fetchall()
        name = var[0][3]
        if len(var) == 0:
            print("No account {}!".format(id))
        else:
            sqlstr = "DELETE FROM account WHERE id = {0}".format(id)
            cur.execute(sqlstr)
            print("Account {} is delete!".format(name))
        conn.commit()
    def account(conn):
        cur = conn.cursor()
        sqlstr = "SELECT id, title, amount, details FROM account;"
        cur.execute(sqlstr)
        var = cur.fetchall()
        if len(var) == 0:
            print("No account created!")
            input("Press Enter to continue ...")
        else:
            print("===== Account list =====")
            print("ID.\tTilte\tAmount\tDetails")
            for idx in range(len(var)):
                print('{0}\t{1}\t{2}\t{3} '.format(var[idx][0], var[idx][1], var[idx][2], var[idx][3]))
            print("")
    def change(conn):
        Acc.account(conn)
        end = True
        while end == True:
            print("--------------------------------------------------------------------------------------")
            print("1. Delete")
            print("2. Modify")
            print("3. Quit")
            choose = int(input("Choose function: "))
            if choose == 1:
                id_ = int(input("Delete item(id): "))
                Acc.delete(conn, id_)
                end = False
            elif choose == 2:
                pass
            elif choose == 3:
                end = False
            else:
                print("Input error")
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