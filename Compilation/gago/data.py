import sqlite3
import os

db_file = 'law_firm_system.db'

# Connect to database (creates it if it doesn't exist)
conn = sqlite3.connect(db_file)
c = conn.cursor()

# Create Tables
c.execute('''
CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    phone TEXT
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Lawyers (
    lawyer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    specialization TEXT,
    hourly_rate REAL
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Cases (
    case_id INTEGER PRIMARY KEY,
    title TEXT,
    type TEXT,
    status TEXT,
    client_id INTEGER,
    lead_lawyer_id INTEGER,
    start_date DATE,
    FOREIGN KEY(client_id) REFERENCES Clients(client_id),
    FOREIGN KEY(lead_lawyer_id) REFERENCES Lawyers(lawyer_id)
)
''')

c.execute('''
CREATE TABLE IF NOT EXISTS TimeEntries (
    entry_id INTEGER PRIMARY KEY,
    case_id INTEGER,
    lawyer_id INTEGER,
    hours_worked REAL,
    date_worked DATE,
    description TEXT,
    FOREIGN KEY(case_id) REFERENCES Cases(case_id),
    FOREIGN KEY(lawyer_id) REFERENCES Lawyers(lawyer_id)
)
''')

# Clear existing data to avoid duplicates if run multiple times
c.execute("DELETE FROM TimeEntries")
c.execute("DELETE FROM Cases")
c.execute("DELETE FROM Lawyers")
c.execute("DELETE FROM Clients")

# Insert Sample Data
# Clients
clients = [
    (1, 'John', 'Doe', 'john@example.com', '555-0101'),
    (2, 'Jane', 'Smith', 'jane@company.com', '555-0102'),
    (3, 'Robert', 'Downey', 'iron@stark.com', '555-9000'),
    (4, 'Sarah', 'Connor', 'sarah@resistance.org', '555-2029')
]
c.executemany("INSERT INTO Clients VALUES (?,?,?,?,?)", clients)

# Lawyers
lawyers = [
    (1, 'Harvey', 'Specter', 'Corporate', 500.00),
    (2, 'Mike', 'Ross', 'Fraud', 250.00),
    (3, 'Jessica', 'Pearson', 'Management', 600.00),
    (4, 'Louis', 'Litt', 'Financial', 400.00)
]
c.executemany("INSERT INTO Lawyers VALUES (?,?,?,?,?)", lawyers)

# Cases
cases = [
    (101, 'Merger Acquisition A', 'Corporate', 'Open', 2, 1, '2023-01-15'),
    (102, 'Patent Defense B', 'IP', 'Closed', 3, 2, '2023-02-10'),
    (103, 'Estate Planning C', 'Family', 'Open', 1, 4, '2023-03-01'),
    (104, 'Tax Audit D', 'Financial', 'Pending', 2, 4, '2023-03-05'),
    (105, 'SkyNet Liability', 'Criminal', 'Open', 4, 1, '2023-04-01')
]
c.executemany("INSERT INTO Cases VALUES (?,?,?,?,?,?,?)", cases)

# Time Entries
entries = [
    (1, 101, 1, 5.5, '2023-01-16', 'Client meeting and strategy'),
    (2, 101, 2, 8.0, '2023-01-17', 'Document review'),
    (3, 103, 4, 2.0, '2023-03-02', 'Initial consultation'),
    (4, 105, 1, 10.0, '2023-04-02', 'Court appearance'),
    (5, 102, 2, 3.5, '2023-02-11', 'Filling motions')
]
c.executemany("INSERT INTO TimeEntries VALUES (?,?,?,?,?,?)", entries)

conn.commit()
print("Database 'law_firm_system.db' created loaded with sample data.")
conn.close()