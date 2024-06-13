SELECT
	CONCAT_WS(' ', first_name, last_name) AS full_name,
	email,
	MAX(bg.rating) AS rating
FROM
	creators AS c
JOIN
	creators_board_games AS cbg
ON
	cbg.creator_id = c.id
JOIN
	board_games AS bg
ON
	bg.id = cbg.board_game_id
WHERE
	RIGHT(email, 4) = '.com'
GROUP BY
	full_name,
	email
ORDER BY
	full_name;