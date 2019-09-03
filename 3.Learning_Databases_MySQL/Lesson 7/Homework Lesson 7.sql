/**********************************************************************/
                 /*Практическое задание тема №8*/
/**********************************************************************/

/* 1. Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток.
 * С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
 * с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
 * с 18:00 до 00:00 — "Добрый вечер", 
 * с 00:00 до 6:00 — "Доброй ночи".*/

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


/*2. В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
 *Допустимо присутствие обоих полей или одно из них. 
 *Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
 *Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. 
 *При попытке присвоить полям NULL-значение необходимо отменить операцию.*/
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


/*3. (по желанию) Напишите хранимую функцию для вычисления произвольного числа Фибоначчи. 
 *Числами Фибоначчи называется последовательность в которой число равно сумме двух предыдущих чисел. 
 *Вызов функции FIBONACCI(10) должен возвращать число 55.*/

/*сначала попробовал сделать через рекурсию: */
DROP FUNCTION IF EXISTS FIBONACCI;
DELIMITER //
CREATE FUNCTION FIBONACCI(num INT)
RETURNS INT NOT DETERMINISTIC
BEGIN
  DECLARE fib_1, fib_2, fib INT;
  IF num <=0 THEN
    SET fib = 0;
  ELSEIF num = 1 OR num = 2 THEN
    SET fib = 1;
  ELSE
    SET fib_1 = FIBONACCI(num-1);
    SET fib_2 = FIBONACCI(num-2);
    SET fib = (fib_1 + fib_2);    
  END IF;
  RETURN fib;
END//
DELIMITER ;
/*но MySQL выдал вот что:
 * "error 1424 recursive stored functions and triggers are not allowed"
 *Так что он тут подумал за пользователя сам )))), рекурсию использовать нельзя.
 *Пришлось через цикл:                                               */
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


/**********************************************************************/
					/*Практическое задание тема №9*/
/**********************************************************************/

/*1. Создайте таблицу logs типа Archive. 
 * Пусть при каждом создании записи в таблицах users, catalogs и products 
 * в таблицу logs помещается время и дата создания записи, название таблицы, 
 * идентификатор первичного ключа и содержимое поля name.*/

/*не нашел, как можно один триггер распространить сразу на несколько таблиц,
 * поэтому пришлось плодить 3 одинаковых триггера, 
 * отличающихся лишь наименованиями используемых таблиц.
 * Дайте пожалуйста комментарий по заданию, есть ли такой способ, 
 * чтобы одному триггеру поставить в соответствие сразу 2 таблицы?
 */

DROP TABLE IF EXISTS logs;
CREATE TABLE logs(
	id SERIAL PRIMARY KEY,
	tablename VARCHAR(50),
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

/*2. (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.*/

/*основная идея задания, по моему мнению - организовать множественную загрузку данных в строки таблицы 
 * (сразу одновременно большое количество строк) вместо перебора вставки отдельной строки в цикле.
 * попробовал сгенерировать 100000 строк на одной итерации из 10: */
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
/*но MYSQL сгенерировал ошибку, не смог определить, почему не выполняется процедура:
 * SQL Error [1064] [42000]: You have an error in your SQL syntax;
 *  check the manual that corresponds to your MySQL server version for the right syntax to use near 
 * 'SELECT @new_row := @new_row + 1 as new_row FROM
	    (SELECT 0 union all SELECT' at line 8
	    
 * хотя сам блок, отмеченный комментариями "Начало генерации" и "Конец генерации" отдельным скриптом
 * отрабатывает корректно, генерируется сто тысяч строк с одной колонкой new_row.
 * Можете подсказать, в чём моя ошибка? */



/**********************************************************************/
					/*Практическое задание тема №10*/
/**********************************************************************/

/*1. В базе данных Redis подберите коллекцию для подсчета посещений с определенных IP-адресов.*/
/*немного не понял смысл задания, что имелось в виду под "подберите коллекцию". Попробовал сделать задание, как понял: */
SADD need_ip '192.168.6.1'
SADD need_ip '192.168.6.2'

SET need_ip 0
-- произошёл вход--
INCR need_ip
 -- произошёл вход--
INCR need_ip
-- получение данных
GET need_ip

/*2. При помощи базы данных Redis решите задачу поиска имени пользователя по электронному адресу и наоборот,
 *поиск электронного адреса пользователя по его имени.*/
SET 'pva@mail.ru' 'Petya' 
SET 'vva@mail.ru' 'Vasya' 
SET 'kva@mail.ru' 'Kolya' 
SET 'ava@mail.ru' 'ARISTARH!!!11' 

SET 'Petya' 'pva@mail.ru' 
SET 'Vasya' 'vva@mail.ru' 
SET 'Kolya' 'kva@mail.ru'
SET 'ARISTARH!!!11' 'ava@mail.ru' 

-- получение имени по email--
GET 'ava@mail.ru'

-- получение email по имени--
GET 'ARISTARH!!!11'

/*3. Организуйте хранение категорий и товарных позиций учебной базы данных shop в СУБД MongoDB.*/
db.shop.insert({id:1,
				name:'Intel Core i3-8100',
				description:'Процессор для настольных персональных компьютеров, основанных на платформе Intel.',
				price:7890.00,
				catalog:{catalog_id:1, name:'Процессоры'}
				})
db.shop.insert({id:2,
				name:'Intel Core i5-7400',
				description:'Процессор для настольных персональных компьютеров, основанных на платформе Intel.',
				price:12700.00,
				catalog:{catalog_id:1, name:'Процессоры'}
				})
db.shop.insert({id:3,
				name:'AMD FX-8320E',
				description:'Процессор для настольных персональных компьютеров, основанных на платформе AMD.',
				price:4780.00,
				catalog:{catalog_id:1, name:'Процессоры'}
				})
db.shop.insert({id:4,
				name:'AMD FX-8320',
				description:'Процессор для настольных персональных компьютеров, основанных на платформе AMD.',
				price:7120.00,
				catalog:{catalog_id:1, name:'Процессоры'}
				})
db.shop.insert({id:5,
				name:'ASUS ROG MAXIMUS X HERO',
				description:'Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX',
				price:19310.00,
				catalog:{catalog_id:2, name:'Материнские платы'}
				})
db.shop.insert({id:6,
				name:'Gigabyte H310M S2H',
				description:'Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX',
				price:4790.00,
				catalog:{catalog_id:2, name:'Материнские платы'}
				})
db.shop.insert({id:7,
				name:'MSI B250M GAMING PRO',
				description:'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX',
				price:5060.00,
				catalog:{catalog_id:2, name:'Материнские платы'}
				})



