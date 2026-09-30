-- PASSVAULT database setup
-- The stored password column contains a Base64-encoded value for this
-- classroom project. Base64 is encoding, not encryption.

CREATE DATABASE IF NOT EXISTS passvault_db;

USE passvault_db;

CREATE TABLE IF NOT EXISTS credentials (
	id INT AUTO_INCREMENT PRIMARY KEY,
	account_name VARCHAR(100) NOT NULL,
	username_email VARCHAR(120) NOT NULL,
	encrypted_password VARCHAR(255) NOT NULL,
	category VARCHAR(50) NOT NULL DEFAULT 'Other',
	strength_tier VARCHAR(20) NOT NULL,
	created_date DATE NOT NULL
);
