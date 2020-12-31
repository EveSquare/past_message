import sqlite3

path = 'pastmessage.db'


if __name__ == "__main__":
    conn = sqlite3.connect(path)


    c = conn.cursor()

    # Create table
    c.execute('''CREATE TABLE stocks
                 (date text,
                   time text,
                   message text, 
                   img_path text,
                   token text)''')
    print("success")