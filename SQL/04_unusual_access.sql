SELECT 
	user_id,
	department,
	system_accessed,
	COUNT(*) AS times_accessed
FROM fake_logins
GROUP BY user_id, system_accessed
ORDER BY user_id, times_accessed;