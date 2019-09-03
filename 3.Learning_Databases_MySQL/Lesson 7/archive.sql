DROP TABLE IF EXISTS logs;
CREATE TABLE logs(
	id SERIAL PRIMARY KEY,
	tablename VARCHAR(255),
	namevalue VARCHAR(255),
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE Archive CHARACTER SET utf8;

DELIMITER //
CREATE TRIGGER insert_table AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs (
		tablename,
		namevalue,
		created_at) 
	VALUES(
		'products',
		NEW.name,
		NOW()
		);
END//

CREATE TRIGGER insert_table AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs (
		tablename,
		namevalue,
		created_at) 
	VALUES(
		'users',
		NEW.name,
		NOW()
		);
END//

CREATE TRIGGER insert_table AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs (
		tablename,
		namevalue,
		created_at) 
	VALUES(
		'catalogs',
		NEW.name,
		NOW()
		);
END//
DELIMITER ;

