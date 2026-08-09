SELECT 
	user_id,
	COUNT(*) AS failed_attempts
FROM fake_logins
WHERE success = 'false'
GROUP BY user_id
HAVING COUNT(*) >= 5
ORDER BY failed_attempts DESC ;