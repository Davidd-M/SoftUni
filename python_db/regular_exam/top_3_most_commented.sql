SELECT
	p.id,
	p.capture_date,
	p.description,
	COUNT(*) AS comments_count
FROM
	photos AS p
JOIN
	comments AS c
ON
	c.photo_id = p.id
WHERE
	p.description IS NOT NULL
GROUP BY
	p.id,
	p.capture_date,
	p.description
ORDER BY
	comments_count DESC,
	p.id
LIMIT 3;