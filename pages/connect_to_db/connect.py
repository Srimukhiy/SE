import sqlite3

def connection():
    conn = sqlite3.connect('pages/data.db')
    c = conn.cursor();
    return c,conn;