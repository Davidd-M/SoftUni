SELECT
	id,
	CONCAT_WS(' ',
	"number",
	street
	),
	city_id
FROM
	addresses
WHERE
	id >= 20
