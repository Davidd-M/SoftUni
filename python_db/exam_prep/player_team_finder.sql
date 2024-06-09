CREATE OR REPLACE PROCEDURE sp_players_team_name(
	IN player_name VARCHAR(50),
    OUT team_name VARCHAR(4)
) 
AS
$$
BEGIN
	SELECT INTO team_name
		DISTINCT t.name
	FROM
		players AS p
	LEFT JOIN
		teams AS t
	ON
		p.team_id = t.id
	WHERE
		CONCAT(first_name, ' ', last_name) = player_name;

    IF team_name IS NULL THEN
        team_name := 'The player currently has no team';
    END IF;
END;
$$
LANGUAGE plpgsql;

CALL sp_players_team_name('Walther Olenchenko', '');