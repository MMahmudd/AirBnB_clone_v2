-- Create_the hbnb_test_db database if_it doese not_exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create_the hbnb_test user if_it doese not_exist and set_the_password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant_all_privileges_on hbnb_test_db to_the hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant_SELECT_privilege_on performance_schema to_the hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
