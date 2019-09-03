SADD need_ip '192.168.6.1'
SADD need_ip '192.168.6.2'

SET need_ip 0

-- произошёл вход--

 INCR need_ip

 -- произошёл вход--

 INCR need_ip

-- получение данных
GET need_ip




SET 'pva@mail.ru' 'Petya' 
SET 'vva@mail.ru' 'Vasya' 
SET 'kva@mail.ru' 'Kolya' 
SET 'ava@mail.ru' 'ARISTARH!!!11' 

SET 'Petya' 'pva@mail.ru' 
SET 'Vasya' 'vva@mail.ru' 
SET 'Kolya' 'kva@mail.ru'
SET 'ARISTARH!!!11' 'ava@mail.ru' 

--получение имени по email
GET 'ava@mail.ru'

--получение email по имени
GET 'ARISTARH!!!11'



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

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название',
  desription TEXT COMMENT 'Описание',
  price DECIMAL (11,2) COMMENT 'Цена',
  catalog_id INT UNSIGNED,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  KEY index_of_catalog_id (catalog_id)
) COMMENT = 'Товарные позиции';

INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  ('Intel Core i3-8100', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 7890.00, 1),
  ('Intel Core i5-7400', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 12700.00, 1),
  ('AMD FX-8320E', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.', 4780.00, 1),
  ('AMD FX-8320', 'Процессор для настольных персональных компьютеров, основанных на платформе AMD.', 7120.00, 1),
  ('ASUS ROG MAXIMUS X HERO', 'Материнская плата ASUS ROG MAXIMUS X HERO, Z370, Socket 1151-V2, DDR4, ATX', 19310.00, 2),
  ('Gigabyte H310M S2H', 'Материнская плата Gigabyte H310M S2H, H310, Socket 1151-V2, DDR4, mATX', 4790.00, 2),
  ('MSI B250M GAMING PRO', 'Материнская плата MSI B250M GAMING PRO, B250, Socket 1151, DDR4, mATX', 5060.00, 2);

DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название раздела',
  UNIQUE unique_name(name(10))
) COMMENT = 'Разделы интернет-магазина' ENGINE=InnoDB;

INSERT INTO catalogs VALUES
  (NULL, 'Процессоры'),
  (NULL, 'Материнские платы'),
  (NULL, 'Видеокарты'),
  (NULL, 'Жесткие диски'),
  (NULL, 'Оперативная память');
