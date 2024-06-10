DELETE FROM 
	board_games
WHERE publisher_id IN (
	SELECT id FROM publishers WHERE address_id IN(
		SELECT id FROM addresses WHERE LEFT(town, 1) = 'L'
	)
);

DELETE FROM 
	publishers 
WHERE address_id IN(
	SELECT id FROM addresses WHERE LEFT(town, 1) = 'L'
);


DELETE FROM 
	addresses
WHERE
	LEFT(town, 1) = 'L';