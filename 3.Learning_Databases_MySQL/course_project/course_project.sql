DROP DATABASE IF EXISTS reservation;

CREATE DATABASE  IF NOT EXISTS reservation DEFAULT CHARSET utf8;
USE reservation;

--
-- Table structure for table users
--

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  idusers SERIAL PRIMARY KEY,
  login varchar(255) NOT NULL,
  pass varchar(255) NOT NULL,
  UNIQUE KEY login_UNIQUE (login),
  UNIQUE KEY idusers_UNIQUE (idusers)
) ENGINE=InnoDB;


--
-- Table structure for table users_data
--

DROP TABLE IF EXISTS users_data;
CREATE TABLE users_data (
  id_user SERIAL PRIMARY KEY,
  name varchar(100) NOT NULL,
  second_name varchar(100) NOT NULL,
  email varchar(100) DEFAULT NULL,
  birthday datetime DEFAULT NULL,
  create_data datetime DEFAULT NULL,
  UNIQUE KEY email_UNIQUE (email),
  INDEX nameuser_index (name,second_name),
  FOREIGN KEY (id_user) REFERENCES users (idusers) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;

--
-- Table structure for table calendar
--

DROP TABLE IF EXISTS calendar;
CREATE TABLE calendar (
  date datetime NOT NULL
) ENGINE=InnoDB COMMENT='hotel days table';

--
-- Table structure for table class_of_room
--

DROP TABLE IF EXISTS class_of_room;
CREATE TABLE class_of_room (
  id_class_of_room SERIAL PRIMARY KEY,
  class_of_room varchar(255) NOT NULL COMMENT '(Luxury, Economy etc.)'
) ENGINE=InnoDB;

--
-- Table structure for table type_allocation
--

DROP TABLE IF EXISTS type_allocation;
CREATE TABLE type_allocation (
  id_type_allocation SERIAL PRIMARY KEY,
  number_of_adults int(11) NOT NULL DEFAULT '0',
  number_of_children int(11) NOT NULL DEFAULT '0',
  number_of_animals int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB;

--
-- Table structure for table hotels
--

DROP TABLE IF EXISTS hotels;
CREATE TABLE hotels (
  idhotels SERIAL PRIMARY KEY,
  name varchar(45) NOT NULL,
  stars tinyint(5) DEFAULT NULL,
  INDEX hotel_index (name)
) ENGINE=InnoDB ;

--
-- Table structure for table hotel_location
--

DROP TABLE IF EXISTS hotel_location;
CREATE TABLE hotel_location (
  id_hotel SERIAL PRIMARY KEY,
  latitude decimal(8,5) NOT NULL,
  longitude decimal(8,5) NOT NULL,
  country varchar(45) NOT NULL,
  region varchar(100) DEFAULT NULL,
  city varchar(45) NOT NULL,
  street varchar(255) NOT NULL,
  house_number int(11) NOT NULL,
  building varchar(5) DEFAULT NULL,
  apartment int(11) NOT NULL,
  INDEX country_index (country),
  INDEX region_index (region),
  INDEX city_index (city),
  INDEX street_index (street),
  FOREIGN KEY (id_hotel) REFERENCES hotels (idhotels)
) ENGINE=InnoDB;

--
-- Table structure for table hotel_services
--

DROP TABLE IF EXISTS hotel_services;
CREATE TABLE hotel_services (
  id_hotel SERIAL PRIMARY KEY,
  hotel_language varchar(500) NOT NULL,
  free_wi_fi tinyint(1) NOT NULL,
  parking tinyint(1) NOT NULL,
  pool tinyint(1) NOT NULL,
  allow_pets tinyint(1) NOT NULL,
  family_apartments tinyint(1) NOT NULL,
  restaurant tinyint(1) NOT NULL,
  bar tinyint(1) NOT NULL,
  equipment_rental tinyint(1) NOT NULL,
  elevator tinyint(1) NOT NULL,
  smoking_room tinyint(1) NOT NULL,
  airport_shuttle tinyint(1) NOT NULL,
  check_in_time DATETIME NOT NULL DEFAULT NOW() COMMENT 'time of arrival at the hotel',
  check_out_time DATETIME NOT NULL DEFAULT NOW() COMMENT 'time of departure from the hotel',
  FOREIGN KEY (id_hotel) REFERENCES hotels (idhotels)
) ENGINE=InnoDB;

--
-- Table structure for table rooms
--

DROP TABLE IF EXISTS rooms;
CREATE TABLE rooms (
  id_room SERIAL PRIMARY KEY,
  id_hotel BIGINT UNSIGNED NOT NULL,
  number_of_rooms int(11) NOT NULL,
  id_room_class BIGINT UNSIGNED NOT NULL,
  id_allocation_type BIGINT UNSIGNED NOT NULL,
  beautiful_view tinyint(1) NOT NULL,
  restroom tinyint(1) NOT NULL,
  shower tinyint(1) NOT NULL,
  television tinyint(1) NOT NULL,
  phone tinyint(1) NOT NULL,
  air_conditioning tinyint(1) NOT NULL,
  heating tinyint(1) NOT NULL,
  clothes_hanger tinyint(1) NOT NULL,
  towels tinyint(1) NOT NULL,
  INDEX key_hotel_room_idx (id_hotel),
  INDEX key_class_room_idx (id_room_class),
  INDEX key_allocate_room_idx (id_allocation_type),
  FOREIGN KEY (id_allocation_type) REFERENCES type_allocation (id_type_allocation),
  FOREIGN KEY (id_room_class) REFERENCES class_of_room (id_class_of_room),
  FOREIGN KEY (id_hotel) REFERENCES hotels (idhotels)
) ENGINE=InnoDB;

--
-- Table structure for table rooms_rate
--

DROP TABLE IF EXISTS rooms_rate;
CREATE TABLE rooms_rate (
  id_rooms SERIAL PRIMARY KEY,
  price_datetime datetime NOT NULL,
  price_adult decimal(15,2) NOT NULL,
  price_children decimal(15,2) NOT NULL,
  price_pet decimal(15,2) NOT NULL,
  FOREIGN KEY (id_rooms) REFERENCES rooms (id_room)
) ENGINE=InnoDB;

--
-- Table structure for table reservations
--

DROP TABLE IF EXISTS reservations;
CREATE TABLE reservations (
  id_reservations SERIAL PRIMARY KEY,
  id_user BIGINT UNSIGNED NOT NULL,
  id_room BIGINT UNSIGNED NOT NULL,
  reserve_from datetime NOT NULL,
  reserve_to datetime NOT NULL,
  reserve_status enum('booked','reservation','cancel') NOT NULL,
  payment_status enum('not_paid','partial_payment','paid') NOT NULL,
  cost_of_living decimal(15,2) NOT NULL,
  INDEX key_reserve_user_idx (id_user),
  INDEX key_reserve_room_idx (id_room),
  FOREIGN KEY (id_room) REFERENCES rooms (id_room),
  FOREIGN KEY (id_user) REFERENCES users (idusers)
) ENGINE=InnoDB;

--
-- Table structure for table payment_for_reservation
--

DROP TABLE IF EXISTS payment_for_reservation;
CREATE TABLE payment_for_reservation (
  id_reserve_paid BIGINT UNSIGNED NOT NULL,
  id_reservation BIGINT UNSIGNED NOT NULL,
  payment_date datetime NOT NULL,
  payment_amount datetime NOT NULL,
  PRIMARY KEY (id_reserve_paid, id_reservation),
  INDEX key_pay_reservation_idx (id_reservation),
  FOREIGN KEY (id_reservation) REFERENCES reservations (id_reservations)
) ENGINE=InnoDB;





