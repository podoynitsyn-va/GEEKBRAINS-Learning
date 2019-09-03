/*Практическое задание Тема №3:*/

/*	1. Пусть в таблице users поля created_at и updated_at оказались незаполненными. 
Заполните их текущими датой и временем.*/
UPDATE users SET created_at = NOW(), updated_at=NOW();

/*	2. Таблица users была неудачно спроектирована. 
 * Записи created_at и updated_at были заданы типом VARCHAR 
 * и в них долгое время помещались значения в формате "20.10.2017 8:10". 
 * Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения. */
UPDATE users 
	SET created_at = STR_TO_DATE(created_at,'%d.%m.%Y %h:%i'), 
	updated_at = STR_TO_DATE(updated_at,'%d.%m.%Y %h:%i');
/*значения в колонках преобразуются, но колонки всё равно остаются типа VARCHAR
 для полного совершенства необходимо привести их к типу DATETIME:*/

ALTER TABLE users MODIFY created_at  DATETIME;
ALTER TABLE users MODIFY updated_at  DATETIME;

/*	3. В таблице складских запасов storehouses_products 
 в поле value могут встречаться самые разные цифры: 
 0, если товар закончился 
 и выше нуля, если на складе имеются запасы. 
 Необходимо отсортировать записи таким образом, 
 чтобы они выводились в порядке увеличения значения value. 
 Однако, нулевые запасы должны выводиться в конце, после всех записей.*/

/*отфильтруем нулевые значения и присвоим им более поздний ранг, нежели ненулевым,
 затем фильтруем непосредственно по значению*/
SELECT 
	Storehouse_id, 
	product_id, 
	value 
FROM storehouses_products 
ORDER BY 
	CASE WHEN value = 0 THEN 1 ELSE 0 END,
	value;

/*	4. (по желанию) Из таблицы users необходимо извлечь пользователей, 
 родившихся в августе и мае. Месяцы заданы в виде списка английских названий ('may', 'august')*/

SELECT 
	*, 
	MONTHNAME(birthday_at) AS month_name 
FROM users 
WHERE MONTHNAME(birthday_at) IN ('May', 'August');

/*	5. (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса.
 SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
 Отсортируйте записи в порядке, заданном в списке IN*/

SELECT 
	* 
FROM catalogs 
WHERE id IN (5, 1, 2) 
ORDER BY FIELD(id, 5, 1, 2);





