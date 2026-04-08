DROP TABLE IF EXISTS properties;

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

INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P001', '123 Maple Ave, Springfield, IL', 250000, 3, 2, 1800, 'House', 1995, 'Garage, Backyard, Central AC', 'Sarah Jones', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P002', '456 Oak St, Springfield, IL', 180000, 2, 1, 950, 'Condo', 2005, 'Gym, Pool, Elevator', 'Mike Brown', 'Sold');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P003', '789 Pine Ln, Springfield, IL', 450000, 4, 3, 2800, 'House', 2018, 'Garage, Pool, Smart Home, Fireplace', 'Sarah Jones', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P004', '101 Elm St, Springfield, IL', 120000, 1, 1, 700, 'Apartment', 1980, 'Shared Laundry', 'Emily Davis', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P005', '202 Birch Blvd, Springfield, IL', 320000, 3, 2.5, 2100, 'Townhouse', 2010, 'Garage, Patio, Hardwood Floors', 'Mike Brown', 'Pending');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P006', '303 Cedar Dr, Springfield, IL', 550000, 5, 4, 3500, 'House', 2022, 'Garage, Pool, Home Theater, Wine Cellar, Solar Panels', 'Sarah Jones', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P007', '404 Walnut Ct, Springfield, IL', 195000, 2, 2, 1100, 'Condo', 2000, 'Gym, Parking Spot', 'Emily Davis', 'Sold');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P008', '505 Ash Way, Springfield, IL', 275000, 3, 2, 1600, 'House', 1960, 'Backyard, Basement', 'David Wilson', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P009', '606 Cherry St, Springfield, IL', 150000, 2, 1, 900, 'Apartment', 1990, 'Balcony', 'David Wilson', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P010', '707 Spruce Ave, Springfield, IL', 380000, 4, 2.5, 2400, 'House', 2015, 'Garage, Fenced Yard, Granite Countertops', 'Mike Brown', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P011', '808 Willow Rd, Springfield, IL', 210000, 2, 2, 1300, 'Townhouse', 2008, 'Garage, Community Pool', 'Sarah Jones', 'Pending');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P012', '909 Poplar Pl, Springfield, IL', 600000, 6, 5, 4200, 'House', 2020, 'Garage, Pool, Guest House, Lake View', 'Emily Davis', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P013', '111 Magnolia Cir, Springfield, IL', 175000, 2, 1.5, 1000, 'Condo', 1998, 'Parking Spot, Gym', 'David Wilson', 'Sold');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P014', '222 Cypress Dr, Springfield, IL', 290000, 3, 2, 1750, 'House', 1975, 'Backyard, Fireplace, Renovated Kitchen', 'Mike Brown', 'Available');
INSERT INTO properties (property_id, address, price, bedrooms, bathrooms, square_feet, type, year_built, amenities, agent, status)
VALUES ('P015', '333 Redwood Ln, Springfield, IL', 135000, 1, 1, 800, 'Apartment', 2012, 'Rooftop Access, Concierge', 'Sarah Jones', 'Available');