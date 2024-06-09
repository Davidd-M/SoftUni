UPDATE 
	coaches
SET 
	salary = salary * coach_level	
WHERE
	(SELECT
		COUNT(coach_id)
	FROM 
		coaches
	JOIN
		players_coaches
	ON
		coaches.id = players_coaches.coach_id
	WHERE
		LEFT(first_name, 1) = 'C'
	) > 0;
