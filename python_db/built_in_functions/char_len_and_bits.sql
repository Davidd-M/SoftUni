SELECT
	CONCAT(mountains.mountain_range, ' ', peaks.peak_name)
		AS 
	mountain_information,
	CHAR_LENGTH(
		CONCAT(mountains.mountain_range, ' ', peaks.peak_name)
	)
		AS 
	character_length,
	BIT_LENGTH(
		CONCAT(mountains.mountain_range, ' ', peaks.peak_name)
	)
		AS 
	bits_of_a_string
FROM
	mountains, peaks
WHERE
	mountains.id = peaks.mountain_id;