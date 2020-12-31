import sqlite3
import datetime as dt
import schedule
import time

path = "pastmessage.db"

# return :list
def where_db(column:str, where:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT date, time, token FROM stocks where {column} = "{where}" ORDER BY time'):
        where_list.append(i)

    conn.close()

    return where_list

# format 2020-12-31
def now():
    return dt.datetime.now().strftime("%Y-%m-%d")

def now_time():
    return dt.datetime.now().strftime("%H:%M:%S")

def watch_db():
    db_time = where_db("date",now())
    
    for i in range(len(where_db("date",now()))):
        if db_time[i][0] == now():#日付一致
            data = db_time[i][1].split(":")
            nows = now_time().split(":")
            if data[0] == nows[0] and data[1] == nows[1]:# 時・分一致
                print(db_time[i])

if __name__ == "__main__":
    schedule.every(1).minutes.do(watch_db)

    while True:
        schedule.run_pending()
        time.sleep(1)