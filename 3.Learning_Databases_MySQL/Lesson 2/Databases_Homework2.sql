/*Практическое задание тема №2
 1. Пусть в таблице catalogs базы данных shop в строке name могут находиться пустые строки и поля,
 принимающие значение NULL. Напишите запрос, который заменяет все такие поля на строку ‘empty’.
 Помните, что на уроке мы установили уникальность на поле name?
 Возможно ли оставить это условие? Почему?
 */
DROP TABLE IF EXISTS catalogs;
CREATE TABLE catalogs (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Название раздела'
  /*UNIQUE unique_name(name(10))*/
) COMMENT = 'Разделы интернет-магазина';

INSERT IGNORE INTO catalogs VALUES
  (DEFAULT, 'processors'),
  (DEFAULT, 'motherboards'),
  (DEFAULT, 'videocards'),
  (DEFAULT, ''),
  (DEFAULT, NULL);
 
 UPDATE catalogs set name = 'empty' WHERE name = '' OR name is NULL;

 SELECT * from catalogs;
 
/*результат:

id|name        |
--|------------|
 1|processors  |
 2|motherboards|
 3|videocards  |
 4|empty       |
 5|empty       |
 */

DROP TABLE IF EXISTS catalogs;

/*
если у нас может быть более одной строки с пустым наименованием,
то от поля unique_name придется избавиться,
поскольку уникальность по первым 10 символам имени уже не будет соблюдена
 */

/*
 2. Спроектируйте базу данных, которая позволяла бы организовать хранение медиа-файлов, 
 загружаемых пользователем (фото, аудио, видео). 
 Сами файлы будут храниться в файловой системе, 
 а база данных будет хранить только пути к файлам, 
 названия, описания, ключевых слов и принадлежности пользователю.
 */

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) COMMENT 'Имя пользователя',
	login VARCHAR(50) COMMENT 'Логин',
	pass VARCHAR(50) COMMENT 'Пароль',
	
	INDEX (name),
	INDEX (login)
) 	COMMENT = 'Список пользователей хранилища';

DROP TABLE IF EXISTS content_type;
CREATE TABLE content_type (
	id SERIAL PRIMARY KEY,
	content VARCHAR(255) COMMENT 'Тип файла'
) COMMENT 'Разновидности медиафайлов';

DROP TABLE IF EXISTS storage;
CREATE TABLE storage (
	id SERIAL PRIMARY KEY,
	storage VARCHAR(50) COMMENT 'Вид хранилища'
) COMMENT 'Виды хранилищ файлов';

DROP TABLE IF EXISTS mediafiles;
CREATE TABLE mediafiles (
	id SERIAL PRIMARY KEY,
	id_user BIGINT UNSIGNED COMMENT 'Идентификатор пользователя',
	id_content_type BIGINT UNSIGNED COMMENT 'Идентификатор типа файлов',
	name VARCHAR(255) COMMENT 'Наименование файла',
	keywords VARCHAR(255) COMMENT 'Список ключевых слов',
	
	FOREIGN KEY (id_user) REFERENCES users(id),
	FOREIGN KEY (id_content_type) REFERENCES content_type(id)
) COMMENT 'Данные о медиафайлах';

DROP TABLE IF EXISTS file_actions;
CREATE TABLE file_actions (
	id SERIAL PRIMARY KEY,
	id_file BIGINT UNSIGNED COMMENT 'Идентификатор медиафайла',
	id_storage BIGINT UNSIGNED COMMENT 'Идентификатор хранилища',
	directory VARCHAR(255) COMMENT 'Путь файла в хранилище',
	create_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время создания файла',
	modify_at DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT 'Время модификации файла',
	
	FOREIGN KEY (id_file) REFERENCES mediafiles(id),
	FOREIGN KEY (id_storage) REFERENCES storage(id)
) COMMENT 'Действия с файлами';



