SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	companion_full_name ILIKE '%AND%'
		AND
	email NOT LIKE '%@gmail';