import sqlite3
import secrets as se
import datetime as dt

path = "pastmessage.db"

# return None
# date format 2020-12-12
# time format 14:24:03
def push_db(date:str, time:str, content:str, img:str):
    conn = sqlite3.connect(path)

    c = conn.cursor()
    # Insert a row of data
    c.execute(f"INSERT INTO stocks VALUES ('{date}','{time}','{content}', '{img}', '{se.token_hex()}')")
 
    conn.commit()

    conn.close()

# return :list
def fetch_db(select= "*", order= "*"):

    conn = sqlite3.connect(path)
    c = conn.cursor()

    order_list = []

    if order == "*":
        for i in c.execute(f'SELECT {select} FROM stocks'):
            order_list.append(i)
    else:
        for i in c.execute(f'SELECT {select} FROM stocks ORDER BY {order}'):
            order_list.append(i)

    conn.close()

    return order_list

# return :list
def where_db(column:str, where:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT * FROM stocks where {column} = "{where}"'):
        where_list.append(i)

    conn.close()

    return where_list


if __name__ == "__main__":
    # push_db("2020-12-30","14:02:03","こんにちは",None)
    # db_data = fetch_db()
    # print(db_data[0][1])
    now = dt.datetime.now().strftime("%Y-%m-%d")
    print(where_db("date",now))
