import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(dbname="typeapp", user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), host="127.0.0.1")

cursor = conn.cursor()


with open('/Users/daniilnovoselcev/Downloads/chastot_shuffle.txt', 'r', encoding='utf-8') as file:
    line = file.readline()
    execute_line = "INSERT INTO frequency_words (word) VALUES (%s)"
    while line:
        cursor.execute(execute_line, (line.strip(),))
        conn.commit()
        line = file.readline()

cursor.close()
conn.close()
