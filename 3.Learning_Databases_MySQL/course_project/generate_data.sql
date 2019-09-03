INSERT INTO calendar 
SELECT a.date datetime
FROM (
SELECT curdate() - INTERVAL (a.a + (10 * b.a) + (100 * c.a) + (1000 * d.a) ) DAY AS Date
FROM (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS a
CROSS JOIN (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS b
CROSS JOIN (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS c
CROSS JOIN (SELECT 0 AS a UNION ALL SELECT 1 UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9) AS d
) a
WHERE a.date BETWEEN '2010-01-01' AND '2022-12-31'
ORDER BY a.date;

INSERT INTO users (idusers, login, pass) VALUES
(1, 'alex', 	'234'	),
(2, 'michael',	'9j9'	),
(3, 'john',		'sfg23'	),
(4, 'max',		'1'		),
(5, 'eva',		'sdf3'	);


INSERT INTO users_data (id_user, NAME, SECOND_NAME, EMAIL, BIRTHDAY, CREATE_DATA) VALUES
(1,'Alexandr',	'Gleason',	'gleason@post.com',	'1986-07-09','2003-07-09 10:08:05'),
(2,'Michael',	'Jackson',	'jackson@post.com',	'1990-03-31','2005-01-01 12:00:00'),
(3,'John',		'Dickens',	'dickens@post.com',	'1980-01-15','2002-02-12 11:11:11'),
(4,'Maximilian','Spencer',	'spenser@post.com',	'1986-07-09','2003-07-09 10:08:05'),
(5,'Eva',		'Davis',	'davis@post.com',	'1986-07-09','2003-07-09 10:08:05');


INSERT INTO class_of_room (id_class_of_room, class_of_room) VALUES
(1, 'apartaments'	),
(2, 'luxury'		),
(3, 'half-luxury'	),
(4, 'econom'		),
(5, 'hostel'		);


INSERT INTO type_allocation (id_type_allocation, number_of_adults, number_of_children, number_of_animals) VALUES
(1,1,0,0),
(2,2,0,0),
(3,1,1,0),
(4,2,1,0),
(5,2,2,0),
(6,3,2,0),
(7,2,0,1),
(8,4,0,0),
(9,6,0,0),
(10,4,2,1),
(11,4,4,1),
(12,10,0,0);


INSERT INTO hotels (idhotels, name, stars) VALUES
(1,'Lynx',4),
(2,'SunLight',5),
(3,'SeaDream',3),
(4,'Mountain dreams',5),
(5,'Avalanche',5),
(6,'Funny John',2),
(7,'Ugly Turkey',2),
(8,'BoomBoroom',4),
(9,'First stay',2),
(10,'Orevoir',4);


INSERT INTO hotel_location (id_hotel, latitude, longitude, country, region, city, street, house_number, building, apartment) VALUES
(1,55.75583,37.61767, 'Russia', 'Moskovskaya oblast', 'Zelenograd', 'Lenina', 66, '1', 50),
(2,80.65485,20.59898, 'Russia', 'Nizhegorodskaya oblast', 'Kirovka', 'Marksa', 22, '', 12),
(3,32.56677,12.89854, 'Russia', 'Krasnodarskiy krai', 'Sochi', 'Kraskova', 112, '1', 21),
(4,55.75222,12.89854, 'Russia', 'Moscow', 'Moscow', 'Ulgina', 23, '1', 11),
(5,55.02870,82.90689, 'Russia', 'Novosibirskaya oblast', 'Novosibirsk', 'Sharpova', 8, '1', 1),
(6,37.61750,55.75204, 'Russia', 'Moscow', 'Moscow', 'Mamaikina', 22, '1', 45);


INSERT INTO hotel_services (id_hotel, hotel_language, free_wi_fi, parking, pool, allow_pets, family_apartments, restaurant, bar, equipment_rental, elevator, smoking_room, airport_shuttle, check_in_time, check_out_time) VALUES
(1,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00'),
(2,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00'),
(3,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00'),
(4,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00'),
(5,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00'),
(6,'russian, english',1,1,0,0,1,1,1,0,1,1,1,'12:00:00', '14:00:00');
