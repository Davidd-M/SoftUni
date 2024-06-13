SELECT
	creators.id,
	CONCAT_WS(' ', first_name, last_name) AS creator_name,
	email
FROM
	creators
LEFT JOIN
	creators_board_games
ON
	creators_board_games.creator_id = creators.id
LEFT JOIN
	board_games
ON
	board_games.id = creators_board_games.board_game_id
WHERE
	board_games.id IS NULL
ORDER BY
	creator_name;