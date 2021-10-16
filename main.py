import sqlite3
from user import User
from bases import conn,cur
import sys
import os

if str(sys.argv[1]) == 'shell':
    os.system('python3')

os.system('clear')
cur.close()