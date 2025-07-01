import sqlite3

# Connect to SQLite DB (it will create one if it doesn't exist)
conn = sqlite3.connect("test.db")
cursor = conn.cursor()

# Create a sample table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    department TEXT
)
""")

# Insert sample data
cursor.executemany("""
INSERT INTO students (name, age, department) VALUES (?, ?, ?)
""", [
    ("Alice", 21, "Computer Science"),
    ("Bob", 22, "Electrical"),
    ("Charlie", 20, "Mechanical")
])

conn.commit()
conn.close()
print("Database setup complete.")
