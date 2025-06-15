USE Book_store;

SELECT title, genre FROM books WHERE genre = 'Romance'
ORDER BY title ASC;

SELECT title, price FROM books WHERE price > 6.00
ORDER BY price DESC;

SELECT b.title, a.first_name, a.last_name
FROM books b
JOIN authors a ON b.author_id = a.author_id;

SELECT b.title, b.genre, b.price
FROM books b
JOIN authors a on b.author_id = a.author_id
ORDER BY b.price DESC;

SELECT title, genre, price FROM books
ORDER BY title ASC;

SELECT 
COUNT(*) total_books,
AVG(price) AS average_price
FROM books;

DELETE FROM books
WHERE title = 'Random';


DELIMITER //
CREATE PROCEDURE CheckLowStock()
BEGIN
SELECT b.title, s.quantity 
FROM books b
JOIN stock s ON b.book_id = s.book_id
WHERE s.quantity < s.min_threshold;
END//
DELIMITER ;

-- This database helps manag a bookstores inventory. New books can be added, old books can be removed and the stock for all the books can be monitored. If the stock count went lower than the threshold mentioned, the staff will be notified. The data joins author details with book titles, genre and price.alte.




