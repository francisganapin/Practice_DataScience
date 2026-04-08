import sqlite3

try:
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM financial_transactions;")
    count = cursor.fetchone()[0]
    print(f"Total rows: {count}")
    
    cursor.execute("SELECT * FROM financial_transactions LIMIT 3;")
    rows = cursor.fetchall()
    print("Sample data:")
    for row in rows:
        print(row)
            
    conn.close()
except Exception as e:
    print(f"Error: {e}")
