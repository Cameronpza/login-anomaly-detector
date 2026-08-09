SELECT 
	user_id,
	department,
	auth_type
FROM fake_logins
WHERE auth_type = 'basic';