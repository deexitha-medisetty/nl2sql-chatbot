import sqlite3

conn = sqlite3.connect("test.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
''')

cursor.execute('''
INSERT INTO students (name, age, major)
VALUES
    ('Alice', 21, 'CS'),
    ('Bob', 22, 'Math'),
    ('Charlie', 23, 'Physics')
''')

conn.commit()
conn.close()

print("✅ test.db initialized with sample data.")

