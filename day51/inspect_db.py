import sqlite3

try:
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables Found:")
    for t in tables:
        print(f"- {t[0]}")
        
    for table in tables:
        table_name = table[0]
        print(f"\n--- Schema for {table_name} ---")
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"{col[1]} ({col[2]})")
            
    conn.close()
except Exception as e:
    print(f"Error: {e}")
