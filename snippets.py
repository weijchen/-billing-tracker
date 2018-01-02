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
from show import *
from account import *
from delete import *
from modify import *
# --------------------------------------------------- init settings
# --------------------------------------------------- Functions
class Tools(object):
    """docstring for Tools"""
    def __init__(self, arg):
        super(Tools, self).__init__()
        self.arg = arg
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
        return out_1, out_2[0:8]
    def get_id(account, table, conn):
        id_ = 1
        found = True
        while found:
            cur = conn.cursor()
            sqlstr = "SELECT * FROM {} WHERE id == {}".format(table, id_)
            cur.execute(sqlstr)
            var = cur.fetchall()
            if len(var) == 0:
                return id_
            else:
                id_ += 1
        
class Category_inc(object):
    """docstring for Category"""
    def __init__(self, arg):
        super(Category, self).__init__()
        self.arg = arg
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
class Category_exp(object):
    """docstring for Category_exp"""
    def __init__(self, arg):
        super(Category_exp, self).__init__()
        self.arg = arg
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
        