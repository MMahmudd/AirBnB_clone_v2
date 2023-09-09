-- Create_the hbnb_dev_db database if_it doese not_exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create_the hbnb_dev user if_it doese not_exist and_set the_password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant_all_privileges on hbnb_dev_db to_the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant_SELECT privilege_on performance_schema to_the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
