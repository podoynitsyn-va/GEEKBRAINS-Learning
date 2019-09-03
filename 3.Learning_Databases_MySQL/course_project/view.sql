DROP VIEW IF EXISTS hotels_table_view;
CREATE VIEW hotels_table_view AS 
SELECT 
	hotels.NAME AS name,
	hotels.STARS AS stars,
	hotel_location.COUNTRY AS country,
	hotel_location.CITY AS city,
	hotel_location.REGION AS region,
	hotel_location.STREET AS street,
	hotel_location.HOUSE_NUMBER AS house_number,
	hotel_location.BUILDING AS building,
	hotel_location.APARTMENT AS apartment,
	hotel_services.HOTEL_LANGUAGE AS hotel_language,
	hotel_services.AIRPORT_SHUTTLE AS airport_shuttle,
	hotel_services.FAMILY_APARTMENTS AS family_apartment,
	hotel_services.PARKING AS parking,
	hotel_services.RESTAURANT AS restaurant
FROM HOTELS
	JOIN HOTEL_LOCATION 
		ON hotel_location.id_hotel = hotels.idhotels
	LEFT JOIN HOTEL_SERVICES 
		ON hotel_services.id_hotel = hotels.idhotels
ORDER BY hotels.NAME;

DROP VIEW IF EXISTS rooms_view;
CREATE VIEW rooms_view AS 
SELECT
	hotels.name AS hotel_name,
	rooms.NUMBER_OF_ROOMS AS number_of_rooms,
	class_of_room.CLASS_OF_ROOM AS class_of_room,
	CONCAT(type_allocation.NUMBER_OF_ADULTS,' взрослых,', type_allocation.NUMBER_OF_CHILDREN, ' детей,', type_allocation.NUMBER_OF_ANIMALS,' животных') AS allocation,
	rooms.AIR_CONDITIONING AS air_conditioning,
	rooms.TELEVISION AS television,
	rooms.heating AS heating,
	rooms.restroom AS restroom,
	rooms.shower AS shower
FROM ROOMS
	JOIN HOTELS 
		ON rooms.id_hotel = hotels.idhotels
	JOIN CLASS_OF_ROOM
		ON rooms.ID_ROOM_CLASS = class_of_room.ID_CLASS_OF_ROOM
	JOIN TYPE_ALLOCATION
		ON rooms.ID_ALLOCATION_TYPE = type_allocation.ID_TYPE_ALLOCATION
ORDER BY hotels.NAME, rooms.ID_ROOM;
	