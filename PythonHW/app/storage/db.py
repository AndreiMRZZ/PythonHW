import sqlite3
from datetime import datetime

from app.models.record import RequestRecord

DB_NAME = "database.db"


def db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def db_init():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation TEXT NOT NULL,
            input1 REAL,
            input2 REAL,
            result REAL NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

#si aici pot crea un obiect, sa nu mai am atatia parametrii
#timestamp ul adaugat la obiectul la care se face tranz, pot pune ca param timestamp
def save_requests(record: RequestRecord):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO requests (operation, input1, input2, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
        ''',
        (record.operation, record.input1, record.input2, record.result, record.timestamp)
    )
    conn.commit()
    conn.close()
def get_all_requests() -> list:
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT *FROM requests ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]
