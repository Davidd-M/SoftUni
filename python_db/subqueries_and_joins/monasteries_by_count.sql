UPDATE countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';

INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	(
	'Hanga Abbey' ,
	(SELECT
		country_code
	FROM
		countries
	WHERE 
	country_name = 'Tanzania')
	);

INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	(
	'Myin-Tin-Daik',
	(SELECT
		country_code
	FROM
		countries
	WHERE 
	country_name = 'Myanmar')
	);

SELECT
	c.continent_name,
	cs.country_name,
	COUNT(m.monastery_name) AS monasteries_count
FROM
	continents AS c
JOIN 
	countries AS cs
ON
	cs.continent_code = c.continent_code
LEFT JOIN
	monasteries AS m
ON
	m.country_code = cs.country_code
WHERE
	cs.three_rivers IS NOT TRUE
GROUP BY
	cs.country_name,
	c.continent_name
ORDER BY
	monasteries_count DESC,
	cs.country_name