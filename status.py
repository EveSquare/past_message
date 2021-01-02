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

def delete_db(token:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    c.execute(f'DELETE from stocks WHERE token = "{token}"')

    conn.commit()
    print("DELEAT")
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

# return :list
def where_date_db(date:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT date, token, created_datetime, user_id FROM stocks where date = "{date}"'):
        where_list.append(i)

    conn.close()

    return where_list

def where_date_db2(date:str):
    conn = sqlite3.connect(path)
    c = conn.cursor()

    where_list = []

    for i in c.execute(f'SELECT date, token, created_datetime, user_id FROM stocks where date < "{date}"'):
        where_list.append(i)

    conn.close()

    return where_list

if __name__ == "__main__":

    #  # Create table
    # c.execute('''CREATE TABLE stocks
    #              (date text,
    #                message text, 
    #                token text,
    #                created_datetime text,
    #                user_id text,
    #                status Integer)''')
    message = "一年dadadadadada前"
    id = "Ud04d8ad9c4a2070d410d4b913422da5fd"

    push_db("2020-12-22","","",id,1)


    # for i in where_date_db2((dt.datetime.now() + dt.timedelta(days=10)).strftime("%Y-%m-%d")):
    #     delete_db(i[3])
    # date_dbs = where_date_db(now())

    # if date_dbs != []:
    #     for row in date_dbs:
    #         date = row[0].split('-')
    #         else:
    #             token = row[1]
    #             created_date = row[2]
    #             user_id = row[3]
    #             print("send Message")
    
    date_dbs2 = where_date_db2(dt.datetime.now() - dt.timedelta(days=10))

    for row in date_dbs2:
        delete_db(row[1])

    all_data()