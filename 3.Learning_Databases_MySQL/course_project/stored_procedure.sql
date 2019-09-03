DROP PROCEDURE IF EXISTS get_free_rooms;
DELIMITER //
CREATE PROCEDURE get_free_rooms(p_hotel TEXT, p_date DATE) 
BEGIN
	SELECT
		hotels.IDHOTELS,
		rooms.ID_ROOM
	FROM ROOMS
		JOIN HOTELS ON rooms.id_hotel = hotels.idhotels
		JOIN RESERVATIONS 
			ON reservations.ID_ROOM = rooms.ID_ROOM
				AND reservations.RESERVE_FROM >= p_date
				AND reservations.RESERVE_TO <= p_date
	WHERE hotels.NAME LIKE '%p_hotel'
	UNION ALL
	SELECT
		hotels.IDHOTELS,
		rooms.ID_ROOM
	FROM ROOMS
		JOIN HOTELS ON rooms.id_hotel = hotels.idhotels
		JOIN RESERVATIONS 
			ON reservations.ID_ROOM = rooms.ID_ROOM
	WHERE reservations.ID_RESERVATIONS IS NULL
			AND hotels.NAME LIKE '%p_hotel';
END//
DELIMITER ;