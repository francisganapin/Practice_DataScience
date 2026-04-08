import sqlite3
import random
import datetime
from decimal import Decimal
# --- Configuration ---
DB_NAME = 'finance.db'
NUM_USERS = 50
NUM_DAYS = 100
START_DATE = datetime.date(2023, 1, 1)
# Sample Data
SECTORS = ['Technology', 'Finance', 'Healthcare', 'Energy', 'Consumer Discretionary']
TICKERS = {
    'Technology': ['AAPL', 'MSFT', 'NVDA', 'ORCL', 'IBM'],
    'Finance': ['JPM', 'BAC', 'GS', 'MS', 'V'],
    'Healthcare': ['JNJ', 'PFE', 'UNH', 'ABBV', 'MRK'],
    'Energy': ['XOM', 'CVX', 'COP', 'SLB', 'EOG'],
    'Consumer Discretionary': ['AMZN', 'TSLA', 'HD', 'MCD', 'NKE']
}
USER_NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Henry', 'Ivy', 'Jack']
def create_connection():
    return sqlite3.connect(DB_NAME)
def setup_schema(conn):
    cur = conn.cursor()
    
    # 1. Companies Table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS companies (
        ticker TEXT PRIMARY KEY,
        company_name TEXT,
        sector TEXT,
        industry TEXT,
        market_cap_billions REAL
    )
    ''')
    # 2. Daily Stock Prices Table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS daily_prices (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ticker TEXT,
        date DATE,
        open_price REAL,
        high_price REAL,
        low_price REAL,
        close_price REAL,
        volume INTEGER,
        FOREIGN KEY (ticker) REFERENCES companies(ticker)
    )
    ''')
    # 3. Users Table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        join_date DATE,
        country TEXT
    )
    ''')
    # 4. Transactions Table (Buys/Sells)
    cur.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        ticker TEXT,
        tx_type TEXT CHECK(tx_type IN ('BUY', 'SELL')),
        quantity INTEGER,
        price_per_share REAL,
        tx_date TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (ticker) REFERENCES companies(ticker)
    )
    ''')
    conn.commit()
def generate_data(conn):
    cur = conn.cursor()
    print("Generating data...")
    # --- Populate Companies ---
    companies_data = []
    all_tickers = []
    for sector, tickers in TICKERS.items():
        for t in tickers:
            market_cap = random.uniform(50.0, 2500.0)
            companies_data.append((t, f"{t} Corp", sector, "General " + sector, market_cap))
            all_tickers.append(t)
    
    cur.executemany('INSERT OR IGNORE INTO companies VALUES (?,?,?,?,?)', companies_data)
    # --- Populate Daily Prices ---
    prices_data = []
    base_prices = {t: random.uniform(50, 500) for t in all_tickers}
    
    for day_offset in range(NUM_DAYS):
        current_date = START_DATE + datetime.timedelta(days=day_offset)
        # Skip weekends
        if current_date.weekday() >= 5:
            continue
            
        for t in all_tickers:
            prev_close = base_prices[t]
            change_pct = random.uniform(-0.05, 0.05)
            open_p = prev_close * (1 + random.uniform(-0.01, 0.01))
            close_p = prev_close * (1 + change_pct)
            high_p = max(open_p, close_p) * (1 + random.uniform(0, 0.02))
            low_p = min(open_p, close_p) * (1 - random.uniform(0, 0.02))
            volume = int(random.uniform(100000, 5000000))
            
            prices_data.append((t, current_date, round(open_p, 2), round(high_p, 2), round(low_p, 2), round(close_p, 2), volume))
            base_prices[t] = close_p # Update for next day
    cur.executemany('''INSERT INTO daily_prices (ticker, date, open_price, high_price, low_price, close_price, volume) 
                       VALUES (?,?,?,?,?,?,?)''', prices_data)
    # --- Populate Users ---
    users_data = []
    for i in range(NUM_USERS):
        name = random.choice(USER_NAMES) + f"{i}"
        users_data.append((name, f"{name.lower()}@example.com", START_DATE, 'USA'))
    
    cur.executemany('INSERT INTO users (username, email, join_date, country) VALUES (?,?,?,?)', users_data)
    # --- Populate Transactions ---
    # Fetch user IDs
    cur.execute("SELECT user_id FROM users")
    user_ids = [row[0] for row in cur.fetchall()]
    
    tx_data = []
    for _ in range(500): # 500 random transactions
        uid = random.choice(user_ids)
        ticker = random.choice(all_tickers)
        tx_type = random.choice(['BUY', 'BUY', 'BUY', 'SELL']) # More buys than sells usually
        qty = random.randint(1, 100)
        price = base_prices[ticker] # rough approximation
        date = START_DATE + datetime.timedelta(days=random.randint(0, NUM_DAYS))
        
        tx_data.append((uid, ticker, tx_type, qty, round(price, 2), date))
    cur.executemany('''INSERT INTO transactions (user_id, ticker, tx_type, quantity, price_per_share, tx_date) 
                       VALUES (?,?,?,?,?,?)''', tx_data)
    
    conn.commit()
    print("Database populated successfully!")
if __name__ == '__main__':
    conn = create_connection()
    setup_schema(conn)
    generate_data(conn)
    conn.close()