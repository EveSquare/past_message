import sqlite3
import secrets as se
import datetime as dt

path = "status.db"


created_datetime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# return None
# date format 2020-12-12
# time format 14:24:03
def push_db(date:str, content:str, created_datetime:str, user_id:str, status:int):
    conn = sqlite3.connect(path)

    c = conn.cursor()
    # Insert a row of data
    c.execute(f"INSERT INTO stocks VALUES ('{date}','{content}', '{se.token_hex()}', '{created_datetime}', '{user_id}', {status})")
 
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
def where_db(select:str, column:str, where:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT {select} FROM stocks where {column} = "{where}"'):
        where_list.append(i)

    conn.close()

    return where_list

def all_data():
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT * FROM stocks'):
        where_list.append(i)

    conn.close()

    print(where_list)

def update_db(user_id:str, status:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    c.execute(f'UPDATE stocks SET {status} WHERE user_id = "{user_id}"')

    conn.commit()

    conn.close()

def user_status(user_id:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT status FROM stocks where user_id = "{user_id}"'):
        conn.close()
        return i[0]

def delete_db(user_id:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute(f'DELETE from stocks WHERE user_id = "{user_id}"')

    conn.commit()

    conn.close()

def user_all_data(user_id:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT * FROM stocks WHERE user_id = "{user_id}"'):
        where_list.append(i)

    conn.close()

    return where_list

# format 2020-12-31
def now():
    return dt.datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":

    #  # Create table
    # c.execute('''CREATE TABLE stocks
    #              (date text,
    #                message text, 
    #                token text,
    #                created_datetime text,
    #                user_id text,
    #                status Integer)''')
    message = "一年前"
    id = "Ud04d8ad9c4a2070d410d4b913422da5f"

    #push_db("","","",id,1)

    # all_data()
    print(user_all_data(id)[0])
    