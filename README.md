# 👋 My CFGDegree Assignments Repository
My name is **Kaveyah** and this repository contains my assignments for the <sup>CFGDegree</sup> Foundation Module.

## Reasons for taking this course
- To get an understanding of programming
- To learn something new
- To learn Python

### Documents included in this repository
1. Requirments.txt - a file that contains a list of packages or libraries needed to work on a project that can all be installed with the file
2. gitignore. - this file tells git which files and folders it shouldn't track

> "knowledge is power." – Sir Francis Bacon


Assignment 4

# Pet Adoption API

This is a beginner-friendly API that allows users to view available pets, apply to adopt one, or cancel an application.

---

## Features

- View all available pets 
- Apply to adopt a pet
- Cancel an adoption

### SETUP
1. Clone the repo
https://github.com/Kaveyah/CFG-Assignments

2. Install
flask
mysql-connector-python
requests

3. Create SQL database

CREATE DATABASE pet_adoption;

USE pet_adoption;

CREATE TABLE pets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(50),
    adopted BOOLEAN DEFAULT FALSE
);

CREATE TABLE applications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    applicant_name VARCHAR(100),
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT INTO pets (name, species, adopted) VALUES
('Milo', 'Dog', FALSE),
('Luna', 'Cat', FALSE),
('Charlie', 'Rabbit', FALSE),
('Bella', 'Dog', FALSE),
('Max', 'Parrot', FALSE);


INSERT INTO applications (pet_id, applicant_name) VALUES
(1, 'Alice'),
(2, 'Ben'),
(3, 'Cara'),
(5, 'David');

