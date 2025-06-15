CREATE DATABASE Book_store;
USE Book_store;


CREATE TABLE Authors
(
  author_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(20) NOT NULL UNIQUE,
  last_name VARCHAR(30) NOT NULL
);

CREATE TABLE Books
(
book_id INT PRIMARY KEY AUTO_INCREMENT, 
title VARCHAR (100) NOT NULL,
author_id INT,
genre VARCHAR (50),
price DECIMAL (4,2),
FOREIGN KEY (author_id) REFERENCES AUTHORS(author_id)
);

CREATE TABLE Stock
(
stock_id INT PRIMARY KEY AUTO_INCREMENT,
book_id INT,
quantity iNT CHECK (quantity >=0),
min_threshold INT NOT NULL DEFAULT 2,
FOREIGN KEY (book_id) REFERENCES books (book_id)
);

INSERT INTO authors (first_name, last_name)
VALUES 
('Harper', 'Lee'),
('Jane', 'Austen'),
('J.K', 'Rowling'),
('Chloe', 'Walsh'),
('Elsie', 'Silver'),
('Kate', 'Eberdeen'), 
('Susan', 'Lewis'),
('Paige', 'Toon');

INSERT INTO books (title, author_id, genre, price)
VALUES
('To kill a mockingbird', 1, 'Fiction', 6.99),
('Pride and Prejudice', 2, 'Romance', 5.82),
('Harry Pottor', 3, 'Fantasy', 11.90),
('Binding 13', 4, 'Romance', 3.50),
('Flawless', 5, 'Thriller', 4.20),
('Miss you', 6, 'Biography', 12.28),
('One minute later', 7, 'Thriller', 5.30),
('Five years ago', 8, 'Romantic fantasy', 7.28),
('Random', 8, 'Thriller', 4.30);

INSERT INTO stock (book_id, quantity, min_threshold)
VALUES
(1,7,3),
(2,1,2),
(3,9,2),
(4,8,3),
(5,1,2),
(6,3,1),
(7,4,3),
(8,3,3);



















