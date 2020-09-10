import sqlite3

database = 'code/books.db'
def connect():
    """Connects to sqlite3 database, if not there creates it."""
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, \
        title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    """Inserts items into database."""
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', 
        (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    """Displays items in database."""
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title='', author='', year='', isbn=''):
    """Search for an item in database."""
    conn =sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(
        'SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?', 
        (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    """Removes items from database."""
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute('DELETE FROM book WHERE id=?', (id,))
    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    """Updates item information in data base."""
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute(
        'UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', 
        (title, author, year, isbn, id))
    conn.commit()
    conn.close()

connect()
#insert('The Sun', 'John Smith', 1915, 54327957923)
#delete(3)
#update(3, 'The Moon', 'John Smooth', 1234, 432564765)
#print(view())
#print(search(author = 'John Smith'))