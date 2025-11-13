
INSERT INTO books (id, title, author, year_published, category_id, stock) VALUES
(11, 'Quantum Realms', 'Alice Newton', 2015, 1, 5),
(12, 'Digital Shadows', 'Brian Lee', 2018, 2, 3),
(13, 'The Code of Life', 'Cynthia Ramos', 2020, 3, 7),
(14, 'Echoes of the Future', 'Daniel Cruz', 2017, 1, 4),
(15, 'Neural Pathways', 'Elena Torres', 2019, 2, 6),
(16, 'Virtual Horizons', 'Felix Tan', 2021, 4, 2),
(17, 'Cybernetic Dreams', 'Grace Lim', 2016, 2, 8),
(18, 'The Last Algorithm', 'Henry Yu', 2022, 3, 5),
(19, 'Data Storm', 'Isabel Chen', 2014, 1, 9),
(20, 'Machine Heart', 'Jason Ong', 2023, 4, 1),
(21, 'Encrypted Truths', 'Karen Mendoza', 2020, 2, 3);



--Display all pending Borrow request.
SELECT * FROM borrow_request WHERE status='Pending';

SELECT 
	books.title as book_title,
	categories.name as category_name,
FROM
	books
JOIN 
	categories on books.category_id = categories.id;
	
	

-- Display the category name for each book
SELECT 
  books.title AS book_title,
  categories.category_name AS category_name
FROM 
  books
JOIN 
  categories ON books.category_id = categories.id;
 
 
--Find all book books in the Science Category.
SELECT 
	books.title AS book_title,
	categories.category_name AS category_name
FROM
	books 
JOIN
	categories ON books.category_id = categories.id
WHERE 
	categories.category_name = "Science";

--show books with pendign request
SELECT 
  books.title AS book_title
FROM 
  books
JOIN 
  borrow_request ON borrow_request.book_id = books.id
WHERE 
  borrow_request.status = 'Pending';
  
  
---- List student names
-- Who requested books
-- That belong to the "Technology" category

SELECT 
  students.first_name AS first_name,
  students.last_name AS last_name,
  books.title AS book_title
FROM 
  students
JOIN 
  borrow_request ON borrow_request.student_id = students.id
JOIN 
  books ON borrow_request.book_id = books.id
JOIN 
  categories ON books.category_id = categories.id
WHERE 
  categories.category_name = 'Technology';
  
  
 --SHOW BOOKS THAT WAS NEVER BEEN BORROWED
SELECT
  books.title AS title
FROM
  books
LEFT JOIN
  borrow_request ON borrow_request.book_id = books.id
WHERE
  borrow_request.book_id IS NULL;

  
