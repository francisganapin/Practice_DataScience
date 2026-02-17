CREATE TABLE customers(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	full_name TEXT NOT NULL,
	email TEXT UNIQUE,
	phone TEXT,
	join_date TEXT
);


INSERT INTO customers (full_name, email, phone, join_date) VALUES
('John Santos', 'john@example.com', '09171234567', '2024-01-10'),
('Maria Dela Cruz', 'maria@example.com', '09981235566', '2024-02-05'),
('Daniel Reyes', 'daniel@example.com', '09192223344', '2024-03-01'),
('Anna Lopez', 'anna@example.com', '09175553311', '2024-04-22'),
('Leo Castillo', 'leo@example.com', '09223334455', '2024-05-14');


CREATE TABLE products (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name TEXT NOT NULL,
	category TEXT,
	price REAL NOT NULL,
	stock INTEGER NOT NULL
);

INSERT INTO products (name, category, price, stock) VALUES
('Creatine', 'Supplements', 850, 10),
('Mass Gainer', 'Supplements', 1200, 5),
('Vitamin C', 'Vitamins', 350, 40),
('Fish Oil', 'Vitamins', 500, 15),
('Knee Wraps', 'Accessories', 299, 25),
('Gym Gloves', 'Accessories', 499, 18),
('Pre-Workout', 'Supplements', 1100, 12),
('Shaker Bottle', 'Accessories', 150, 30),
('BCAA', 'Supplements', 900, 8);

CREATE TABLE orders(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	customer_id INTEGER,
	order_date TEXT,
	totals REAL,
	FOREIGN KEY(customer_id) REFERENCES customers(id)
);

INSERT INTO orders (customer_id, order_date, totals) VALUES
(1, '2024-06-01', 2350),
(2, '2024-06-05', 1500),
(1, '2024-06-08', 1200),
(3, '2024-06-10', 499),
(4, '2024-06-15', 2400),
(5, '2024-06-20', 900);


CREATE TABLE order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 1500),
(1, 4, 1, 350),
(1, 6, 1, 500),
(2, 1, 1, 1500),
(3, 3, 1, 1200),
(4, 7, 1, 499),
(5, 1, 1, 1500),
(5, 8, 1, 900),
(6, 10, 1, 900);


--GET ALL SORTED BY PRICE (HIGHEST TO LOWEST)

SELECT * FROM products ORDER BY price DESC;

--get all customers who joined after march 2024
SELECT * FROM customers WHERE DATE(join_date) > "2024-03-31";

-- select all product  with stock less than
SELECT * from products WHERE stock < 10;

-- GET THE TOP 3 MOST EXPENSIVE products
SELECT * from products ORDER BY price DESC LIMIT  3;


-- find customers whoes name  contains "a"
SELECT * FROM customers WHERE full_name LIKE "%A%";

-- count how many orders each custmer has
SELECT
	customers.full_name AS customer_name,
	COUNT(*) AS order_count
from orders
join customers on orders.customer_id = customers.id
group by customers.id;

--Calculate total sales per category
SELECT 
	products.category,
	SUM (order_items.price * order_items.quantity) as total_sales
FROM order_items
JOIN products on order_items.product_id = products.id
GROUP BY products.category;

--list of product was never purchase
SELECT products.*
FROM products
left JOIN order_items on products.id  = order_items.product_id
WHERE order_items.product_id IS NULL;


-- find the best-selling product(highest quantity total)
SELECT products.name as name,
SUM(order_items.quantity) AS total_quantity,
	  SUM(order_items.price * order_items.quantity) as sales
from products
JOIN order_items on products.id = order_items.product_id
GROUP BY products.name
ORDER BY sales DESC LIMIT 3;


--product sort them by price
SELECT * FROM products
ORDER BY price DESC;


--GET CUSTOMER WHO JOINED after March 2024
SELECT *
FROM customers
WHERE join_date > '2024-03-31';

-- show all proudcts with stock less than 10
SELECT * FROM products WHERE stock < 10;

--show customer whose name contains "a".
SELECT * FROM customers 
WHERE full_name like "%a%";

--Show all
SELECT orders.id,
		customers.full_name,
		orders.order_date,
		orders.total
FROM orders
JOIN customers
	ON orders.customer_id = customers.id
	
	
SELECT customers.full_name,
	COUNT(orders.id) as total_orders
FROM customers
LEFT JOIN orders
	on customers.id = orders.customer_id
GROUP BY customers.id;

-- total sales per category.
SELECT products.category,
	sum(order_items.price * order_items.quantity) as total_sales
from order_items
join products
	ON order_items.product_id = products.id
GROUP BY products.category;


--find customer does not purchase any item
SELECT customers.full_name,
from customers
left join orders
	on orders.customer_id  = customers.id
WHERE orders.customer_id IS NULL;

INSERT INTO customers (full_name, email, phone, join_date) VALUES
('Alice Santos', 'alice@example.com', '09171234567', '2023-01-15'),
('Brian Cruz', 'brian@example.com', '09181234567', '2023-02-20'),
('Carla Reyes', 'carla@example.com', '09192223333', '2023-03-05'),
('David Tan', 'david@example.com', '09201234567', '2023-04-10'),
('Ella Lim', 'ella@example.com', '09211234567', '2023-05-25');

SELECT customers.full_name
FROM customers
LEFT JOIN orders ON orders.customer_id = customers.id
WHERE orders.customer_id IS NULL;

-- show each customer latest order date
SELECT customers.full_name,
		orders.order_date
FROM customers
JOIN orders ON orders.customer_id = customers.id
ORDER BY orders.order_date DESC;

--Find wich category earns the most money overall.
SELECT products.category as category
	   SUM(order_items.price * order_items.quantity) AS overall_sales
FROM products
JOIN order_items on products.id = product_id
GROUP BY products.category;

------ find which category earns the most  money overall
SELECT 
  products.category AS category,
  SUM(order_items.price * order_items.quantity) AS overall_sales
FROM products
JOIN order_items ON products.id = order_items.product_id
GROUP BY products.category
ORDER BY overall_sales DESC;