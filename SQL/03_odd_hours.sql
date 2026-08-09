SELECT
	user_id,
	department, 
	timestamp, 
	auth_type
FROM fake_logins
WHERE CAST(strftime('%H', timestamp) AS INTEGER) < 6
   OR CAST(strftime('%H', timestamp) AS INTEGER) > 21
ORDER BY timestamp;