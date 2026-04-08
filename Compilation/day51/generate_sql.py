import json

with open('real_estate.json', 'r') as f:
    data = json.load(f)

sql_statements = []
sql_statements.append("DROP TABLE IF EXISTS properties;")
sql_statements.append("""
CREATE TABLE properties (
    property_id TEXT PRIMARY KEY,
    address TEXT,
    price INTEGER,
    bedrooms INTEGER,
    bathrooms REAL,
    square_feet INTEGER,
    type TEXT,
    year_built INTEGER,
    amenities TEXT, -- Storing array as comma-separated string for SQLite
    agent TEXT,
    status TEXT
);
""")

for prop in data:
    amenities = ", ".join(prop['amenities'])
    # Escape single quotes in strings
    address = prop['address'].replace("'", "''")
    agent = prop['agent'].replace("'", "''")
    prop_type = prop['type'].replace("'", "''")
    status = prop['status'].replace("'", "''")
    
    sql = f"""INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('{prop['property_id']}', '{address}', {prop['price']}, {prop['bedrooms']}, {prop['bathrooms']}, {prop['square_feet']}, '{prop_type}', {prop['year_built']}, '{amenities}', '{agent}', '{status}');"""
    sql_statements.append(sql)

with open('setup_real_estate.sql', 'w') as f:
    f.write("\n".join(sql_statements))

print("setup_real_estate.sql created successfully.")
