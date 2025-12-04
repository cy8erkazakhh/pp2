CREATE PROCEDURE new_user(namik TEXT, phne TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
IF phne ~ '\d{11}' THEN
	IF EXISTS (
		SELECT 1 FROM phonebook 
		WHERE name = namik
		) THEN
			UPDATE phonebook 
			SET phone = phne 
			WHERE name = namik;
	ELSE 
		INSERT INTO phonebook(name, phone) 
		VALUES (namik, phne);
	END IF;
ELSE 
	RAISE NOTICE 'phone number have to be integer with length 11.';
END IF;
END;
$$;