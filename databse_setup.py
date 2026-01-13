import sqlite3

# Create database and table to store user interactions
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS interactions (email TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)")
conn.commit()
conn.close()

print("Database setup complete.")
