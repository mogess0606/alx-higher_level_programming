-- Syntax used to create cities table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT UNIQUE PRIMARY KEY AUTO_INCREMENT, state_id INT  FOREIGN KEY REFERENCES states(id), name varchar(256) NOT NULL);

