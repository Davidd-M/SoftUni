SELECT
	clients.full_name,
	COUNT(car_id) AS count_of_cars,
	SUM(bill)
FROM 
	clients
JOIN
	courses
ON
	clients.id = courses.client_id
WHERE
	SUBSTRING(clients.full_name, 2, 1) = 'a'
GROUP BY
	clients.id
HAVING
	COUNT(car_id) > 1
ORDER BY
	clients.full_name;
