import sqlite3
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
# --- SQL SETUP ---
conn = sqlite3.connect('social_media.db')
cursor = conn.cursor()
# Create Tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        join_date DATE,
        country TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usage_logs (
        log_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        date DATE,
        platform TEXT,
        minutes_spent INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
''')
# Insert Mock Data
users = [
    (1, 'alice_99', '2023-01-15', 'USA'),
    (2, 'bob_tech', '2023-02-10', 'UK'),
    (3, 'charlie_vlogs', '2023-03-01', 'USA'),
    (4, 'diana_arts', '2023-03-05', 'Canada'),
    (5, 'eve_gamer', '2023-04-20', 'UK')
]
cursor.executemany('INSERT OR IGNORE INTO users VALUES (?,?,?,?)', users)
logs = []
platforms = ['Instagram', 'TikTok', 'Twitter']
for uid in range(1, 6):
    for i in range(10): # 10 days of data
        day = (datetime(2023, 1, 1) + timedelta(days=i)).strftime('%Y-%m-%d')
        platform = random.choice(platforms)
        minutes = random.randint(5, 180)
        logs.append((None, uid, day, platform, minutes))
        
cursor.executemany('INSERT OR IGNORE INTO usage_logs VALUES (?,?,?,?,?)', logs)
conn.commit()
print("SQL Database 'social_media.db' created.")
conn.close()
# --- NUMPY SETUP ---
# Simulating a 5 users x 7 days matrix of hours spent
# Rows = Users, Cols = Days of Week (Mon-Sun)
usage_matrix = np.random.randint(0, 10, size=(5, 7)) 
print("\nNumPy Usage Matrix (5 users x 7 days):")
print(usage_matrix)