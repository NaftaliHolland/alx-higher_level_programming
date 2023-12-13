-- Converts hbtn_0c_0 database to utf8

USE `hbtn_0c_0`;

ALTER DATABASE `hbtn_0c_0`
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE `first_table`
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

ALTER TABLE `hbtn_0c_0`
MODIFY `name` TEXT
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
