CREATE TABLE branches(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	branch_name TEXT,
	city TEXT,
	opening_date TEXT
);

CREATE TABLE employees (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	first_name TEXT,
	last_name TEXT,
	position TEXT,
	hire_date TEXT,
	branch_id INTEGER
);

CREATE TABLE menu_items(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	item_name TEXT,
	category TEXT,
	price REAL
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_date TEXT,
    branch_id INTEGER,
    employee_id INTEGER
);

CREATE TABLE order_items(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	order_id INTEGER,
	menu_item_id INTEGER,
	quanity INTEGER

);
INSERT INTO branches (branch_name, city, opening_date) VALUES
('Jollibee SM North', 'Quezon City', '2015-06-10'),
('Jollibee Glorietta', 'Makati', '2018-03-22'),
('Jollibee Alabang Town Center', 'Muntinlupa', '2020-11-05');


INSERT INTO employees (first_name, last_name, position, hire_date, branch_id) VALUES
('Anna', 'Reyes', 'Cashier', '2021-01-15', 1),
('Mark', 'Santos', 'Cook', '2022-07-10', 1),
('Liza', 'Tan', 'Manager', '2020-05-20', 2),
('John', 'Lopez', 'Cashier', '2023-02-01', 2),
('Carlos', 'Lim', 'Cook', '2023-08-12', 3);

INSERT INTO menu_items (item_name, category, price) VALUES
('Chickenjoy', 'Chicken', 89.00),
('Jolly Spaghetti', 'Pasta', 65.00),
('Burger Steak', 'Rice Meal', 75.00),
('Yumburger', 'Burger', 45.00),
('Peach Mango Pie', 'Dessert', 35.00);


INSERT INTO orders (order_date, branch_id, employee_id) VALUES
('2024-11-01', 1, 1),
('2024-11-01', 1, 2),
('2024-11-02', 2, 3),
('2024-11-03', 2, 4),
('2024-11-04', 3, 5);


INSERT INTO order_items (order_id, menu_item_id, quanity) VALUES
(1, 1, 2),  -- Chickenjoy x2
(1, 5, 1),  -- Peach Mango Pie x1
(2, 2, 3),  -- Jolly Spaghetti x3
(3, 3, 1),  -- Burger Steak x1
(3, 4, 2),  -- Yumburger x2
(4, 1, 1),  -- Chickenjoy x1
(5, 2, 1),  -- Jolly Spaghetti x1
(5, 5, 2);  -- Peach Mango Pie x2

SELECT * FROM branches;
SELECT * FROM employees;
SELECT * FROM menu_items;
SELECT * FROM order_items;
SELECT * FROM orders;


-- List all employees working in makati
SELECT * 
FROM employees
JOIN  branches ON branches.id = employees.branch_id
WHERE branches.city LIKE "%Makati%";

-- Show Orders By cashier
SELECT * 
from orders
JOIN  employees on employees.id = orders.employee_id
WHERE employees.position = "Cashier";


--GET THE total quantity sold per menu item
SELECT SUM(order_items.quanity * menu_items.price) as Sales ,menu_items.item_name
FROM order_items
JOIN menu_items on menu_items.id = order_items.menu_item_id
GROUP BY item_name;

-- List all orders that include chicken JOY
SELECT menu_items.item_name,order_items.order_id
FROM menu_items
JOIN order_items on order_items.menu_item_id = menu_items.id
WHERE menu_items.item_name LIKE "%Chickenjoy%";


--show the full name of employees and the items they sold
SELECT employees.first_name,employees.last_name,menu_items.item_name
FROM employees
JOIN orders on orders.employee_id = employees.id
JOIN order_items on order_items.order_id = orders.id
JOIN menu_items on menu_items.id = order_items.menu_item_id;


-- which brand sold the most Peach Mango Pies
SELECT branch_name,quanity,item_name
FROM branches
JOIN orders on orders.branch_id = branches.id
JOIN order_items on order_items.order_id = orders.id
JOIN menu_items on menu_items.id = order_items.menu_item_id
WHERE menu_items.item_name LIKE "%Peach Mango Pie%"
ORDER BY order_items.quanity DESC; 

