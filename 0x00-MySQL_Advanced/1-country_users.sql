-- Active: 1702391851621@@127.0.0.1@3306@holberton
-- create table users
-- with attributes id, email, name and country (US - CO - TN)

CREATE TABLE IF NOT EXISTS users (
		id INT AUTO_INCREMENT PRIMARY KEY,
		email VARCHAR(255) NOT NULL UNIQUE,
		name VARCHAR(255),
		country ENUM('US', 'CO', 'TN') DEFAULT 'US'
);
