
CREATE OR REPLACE FUNCTION fn_stadium_team_name(
	stadium_name VARCHAR(30)
) RETURNS TABLE (team_name VARCHAR)
AS
$$
BEGIN
	RETURN QUERY 
	SELECT 
		DISTINCT name
	FROM
		teams
	WHERE
		stadium_id = 
		(SELECT
			id
		FROM
			stadiums AS s
		WHERE
			s.name = stadium_name)
	ORDER BY 
		name;
END;
$$
LANGUAGE plpgsql;