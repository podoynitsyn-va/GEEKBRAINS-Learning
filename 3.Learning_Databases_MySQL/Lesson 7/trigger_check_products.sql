DROP TRIGGER IF EXISTS check_products_name;
DELIMITER //
CREATE TRIGGER check_products_name BEFORE INSERT ON products
FOR EACH ROW
BEGIN	
	IF NEW.name IS NULL AND NEW.description IS NULL THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'WRONG Values in row product';
	END IF;
END//
DELIMITER ;