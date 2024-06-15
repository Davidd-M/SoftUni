UPDATE addresses
SET country = 'Blocked'
WHERE LEFT(country, 1) = 'B';

UPDATE addresses
SET country = 'Test'
WHERE LEFT(country, 1) = 'T';

UPDATE addresses
SET country = 'In Progress'
WHERE LEFT(country, 1) = 'P';