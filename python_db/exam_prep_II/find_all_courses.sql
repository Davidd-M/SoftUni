CREATE OR REPLACE FUNCTION fn_courses_by_client(
	phone_num VARCHAR(20)
) RETURNS INT
AS
$$
BEGIN
	RETURN (
		SELECT
			COUNT(*)
		FROM
			courses
		WHERE
			client_id = (SELECT id FROM clients WHERE phone_number = phone_num)
	);
END;
$$
LANGUAGE plpgsql;