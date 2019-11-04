from flask import Flask
from flask import request
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'
conn = sqlite3.connect(DATABASE)
conn.execute('CREATE TABLE IF NOT EXISTS store (data TEXT)')
conn.close()


@app.route('/')
def home():
    return ''


@app.route('/save', methods=['GET'])
def save_query():
    data = request.args.get('q')
    try:
        with sqlite3.connect(DATABASE) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO store (data) VALUES (?)', (data,))
            conn.commit()
            print("Data Saved")
    except Exception:
        conn.rollback()
        print("Error Occured!")
    finally:
        conn.close()
        return ''
