SELECT
	cars.id AS car_id,
	cars.make,
	cars.mileage,
	COUNT(c.id) AS count_of_courses,
	ROUND(AVG(c.bill), 2) AS average_bill
FROM
	cars
LEFT JOIN
	courses AS c
ON
	c.car_id = cars.id
GROUP BY
	cars.id,
	cars.make,
	cars.mileage
HAVING
	COUNT(cars.id) <> 2
ORDER BY
	count_of_courses DESC,
	car_id;