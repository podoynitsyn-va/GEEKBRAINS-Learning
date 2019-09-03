/*Тема “Сложные запросы”*/

/* 1. Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.*/

SELECT DISTINCT
	users.name 
FROM orders 
	LEFT JOIN users 
		ON orders.user_id = users.id;
		
/* 2. Выведите список товаров products и разделов catalogs, который соответствует товару*/	
SELECT
	products.name,
	catalogs.name 
FROM products
	LEFT JOIN catalogs 
		ON products.catalog_id = catalogs.id;

/* 3. Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
 Поля from, to и label содержат английские названия городов, поле name — русское. 
 Выведите список рейсов flights с русскими названиями городов */
DROP TABLE IF EXISTS flights;
CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  flight_from VARCHAR(255),
  flight_to VARCHAR(255));
  
INSERT INTO flights (flight_from, flight_to) VALUES
  ('moscow', 'omsk'),
  ('novgorod', 'kazan'),
  ('irkutsk', 'moscow'),
  ('omsk', 'irkutsk'),
  ('moscow', 'kazan');
  
DROP TABLE IF EXISTS cities;
CREATE TABLE cities (
  label VARCHAR(255),
  name VARCHAR(255));
  
 INSERT INTO cities (label, name) VALUES
 	('moscow', 'Москва'),
 	('irkutsk', 'Иркутск'),
 	('novgorod', 'Новгород'),
 	('kazan', 'Казань'),
 	('omsk', 'Омск');
 
 SELECT
 	flights.id,
 	cities_from.name AS 'Пункт отправления',
 	cities_to.name AS 'Пункт назначения'
 FROM
 	flights
 		LEFT JOIN cities as cities_from
 			ON flights.flight_from = cities_from.label
 		LEFT JOIN cities as cities_to
 			ON flights.flight_to = cities_to.label
 ORDER BY flights.id
 
 
/*Тема “Транзакции, переменные, представления”*/
 
/* 1. В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
  Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции */
START TRANSACTION;
INSERT INTO sample.users  (SELECT * FROM shop.users WHERE shop.users.id=1);
COMMIT;

/* 2. Создайте представление, которое выводит название name товарной позиции 
 из таблицы products и соответствующее название каталога name из таблицы catalogs.*/
CREATE OR REPLACE VIEW products_catalogs AS
	SELECT 
		products.name AS product_name, 
		catalogs.name AS Catalogs_name
	FROM products 
		LEFT JOIN catalogs 
			ON products.catalog_id = catalogs.id;

 
	