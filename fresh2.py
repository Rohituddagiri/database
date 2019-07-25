import sqlite3
import time
import datetime



def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data(datestamp TEXT, keyword TEXT UNIQUE, value REAL)')

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    k = input("Enter key to be added:")
    v = int(input("Enter value to be added:"))
    c.execute("SELECT keyword FROM data")
    entry = c.fetchall()
    c.execute("INSERT INTO data (datestamp, keyword, value) VALUES (?, ?, ?)",(date,k,v))
    conn.commit()
    c.execute("SELECT * FROM data")
    [print(row) for row in c.fetchall()]
   
def read_db():
    c.execute("SELECT * FROM data")
    [print(row) for row in c.fetchall()]
    k = input("Enter key to read:")
    print(50*'#')
    c.execute("SELECT * FROM data WHERE keyword=?",(k, ))
    [print(row) for row in c.fetchall()]
    conn.commit()
    
def delete_item(key):
    c.execute('SELECT * FROM data')
    [print(row) for row in c.fetchall()]
    c.execute("DELETE FROM data WHERE keyword=?",(key, ))
    conn.commit()
    print(50*'#')
    c.execute('SELECT * FROM data')
    [print(row) for row in c.fetchall()]


conn = sqlite3.connect('file.db')
c = conn.cursor()
create_table()
while input("Do you want to continue?")=="y":
    i = input("Enter C(create) or R(read) or D(delete) action to be performed:")
    if i == 'C':    
        dynamic_data_entry()
        print("You have entered data successfully!")

    if i == 'R':
        read_db()
    if i == 'D':
        ke = input("Enter key to delete:")
        delete_item(ke)
        
c.close()
conn.close()
    
