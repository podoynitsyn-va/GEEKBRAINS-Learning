DROP PROCEDURE IF EXISTS million_rows;
DELIMITER //
CREATE PROCEDURE million_rows()
BEGIN
	DECLARE v INT;
	SET v = 0;
	WHILE v < 10 DO
    INSERT INTO users(ID) VALUES
    	/*генерируем 100000 строк*/
    	(SELECT @new_row := @new_row + 1 as new_row FROM
	    (SELECT 0 union all SELECT 1 union all SELECT 2 union all SELECT 3 union all SELECT 4 union all SELECT 5 union all SELECT 6 union all SELECT 7 union all SELECT 8 union all SELECT 9) AS t1,
		(SELECT 0 union all SELECT 1 union all SELECT 2 union all SELECT 3 union all SELECT 4 union all SELECT 5 union all SELECT 6 union all SELECT 7 union all SELECT 8 union all SELECT 9) AS t2, 
		(SELECT 0 union all SELECT 1 union all SELECT 2 union all SELECT 3 union all SELECT 4 union all SELECT 5 union all SELECT 6 union all SELECT 7 union all SELECT 8 union all SELECT 9) AS t3, 
		(SELECT 0 union all SELECT 1 union all SELECT 2 union all SELECT 3 union all SELECT 4 union all SELECT 5 union all SELECT 6 union all SELECT 7 union all SELECT 8 union all SELECT 9) AS t4, 
		(SELECT 0 union all SELECT 1 union all SELECT 2 union all SELECT 3 union all SELECT 4 union all SELECT 5 union all SELECT 6 union all SELECT 7 union all SELECT 8 union all SELECT 9) AS t5, 
		(SELECT @new_row:=0) t6);
		/*конец генерации*/
    SET v = v + 1;
  	END WHILE;
END//
DELIMITER ;

CALL million_rows();
SELECT * FROM users;