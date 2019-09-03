DROP FUNCTION IF EXISTS FIBONACCI;
DELIMITER //
CREATE FUNCTION FIBONACCI(num INT)
RETURNS INT NOT DETERMINISTIC
BEGIN
	DECLARE fib_1, fib_2, fib, step INT;
	SET fib_1 = 1;
	SET fib_2 = 1;
	SET step = 0;
	WHILE step < num-2 DO
		SET fib = fib_1 + fib_2;
		SET fib_1 = fib_2;
		SET fib_2 = fib;
		SET step = step + 1;
	END WHILE;
	RETURN fib;	
END//
DELIMITER ;