CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
	first_name_of_creator VARCHAR(30)
) RETURNS INT
AS
$$
BEGIN
	RETURN (SELECT
		COUNT(c.id)
	FROM
		creators AS c
	JOIN
		creators_board_games AS cbg
	ON
		cbg.creator_id = c.id
	WHERE
		c.first_name = first_name_of_creator);
END;
$$
LANGUAGE plpgsql;
