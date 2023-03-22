-- a script that creates the database hbtn_0d_usa and the table cities
-- creates database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- creates table
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL FOREIGN KEY REFERENCES state(id),
	name VARCHAR(256) NOT NULL);
