-- A table called user with attributes 
-- id integer, not null, auto incr and primary key
-- email string with 255 character, not null, and unique
-- name string 255 character

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
