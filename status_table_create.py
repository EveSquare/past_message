import sqlite3

path = 'status.db'


if __name__ == "__main__":
    conn = sqlite3.connect(path)


    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text,
                   message text, 
                   token text,
                   created_datetime text,
                   user_id text,
                   status Integer)''')
    print("success")