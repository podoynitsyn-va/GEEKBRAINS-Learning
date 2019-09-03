DROP FUNCTION IF EXISTS hello;
DELIMITER //
CREATE FUNCTION hello()
RETURNS TEXT NOT DETERMINISTIC
BEGIN
	DECLARE hour_now INT;
	SET hour_now = HOUR(NOW());
	IF hour_now >=0 AND hour_now < 6 THEN
		RETURN 'Доброй ночи';
	ELSEIF hour_now >=6 AND hour_now < 12 THEN
		RETURN 'Доброе утро';
	ELSEIF hour_now >=12 AND hour_now < 18 THEN
		RETURN 'Добрый день';
	ELSE RETURN 'Добрый вечер';
	END IF;
END//
DELIMITER ;