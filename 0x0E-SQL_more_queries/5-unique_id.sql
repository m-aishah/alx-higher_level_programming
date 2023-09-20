-- Creates the table unique_id on the MYSQL server with columns id and name.
-- id is a unique id.
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT,
	`name` VARCHAR(256),
	UNIQUE (`id`)
);
