import sqlite3


conn = sqlite3.connect("orders.db")
cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS whitelist(
        id integer UNIQUE NOT NULL,
        vk TEXT UNIQUE NOT NULL,
        discord TEXT,
        nickname TEXT NOT NULL);
""")
cur.execute("""
        CREATE TABLE IF NOT EXISTS blacklist_vk(
        vk TEXT UNIQUE NOT NULL);""")
cur.execute("""CREATE TABLE IF NOT EXISTS blacklist_dis (discord TEXT UNIQUE NOT NULL);""")

def it_was_test():
    for i in range(get_id()+1):
        cur.execute(""" DELETE from whitelist where id = ? ;""",(i,))
        cur.execute(""" UPDATE ID SET id =1  where id = ? ;""",(i,))
    
    cur.execute('select * from blacklist_vk') 
    for i in cur.fetchall():
        cur.execute(""" DELETE from vk_blacklist where id = ? ;""",(i,))
    
    cur.execute('select * from blacklist_dis') 
    for i in cur.fetchall():
        cur.execute(""" DELETE from dis_blacklist where discord = * ;""")
    
    conn.commit()

def id():
    cur.execute(""" select * from ID""")
    _id = cur.fetchone()[0]
    _id_new = _id+1
    cur.execute("""UPDATE ID SET id = ?  where id = ?;""", (_id_new,_id))
    conn.commit()
    return _id
def get_id():
    cur.execute(""" select * from ID""")
    _id = cur.fetchone()[0]
    return _id


def all_tables():
    cur.execute('SELECT name from sqlite_master where type= "table"')
    print(cur.fetchall())

#    cur.execute("""DROP TABLE ?;""",(table,))
#    conn.commit() 
