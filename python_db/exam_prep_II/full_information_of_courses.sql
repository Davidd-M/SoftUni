SELECT
	addresses.name AS address,
	CASE
		WHEN EXTRACT(HOUR FROM courses.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	courses.bill,
	clients.full_name,
	cars.make,
	cars.model,
	categories.name
FROM
	addresses
JOIN
	courses
ON
	addresses.id = courses.from_address_id
JOIN
	clients
ON
	clients.id = courses.client_id
JOIN
	cars
ON
	courses.car_id = cars.id
JOIN
	categories
ON
	categories.id = cars.category_id