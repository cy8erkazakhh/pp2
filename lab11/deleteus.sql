CREATE PROCEDURE delete_user(namik TEXT) 
LANGUAGE plpgsql
AS $$
BEGIN
IF EXISTS (
        SELECT name FROM phonebook WHERE name = namik
) THEN 
    DELETE FROM phonebook WHERE name = namik;
ELSE 
    RAISE NOTICE 'user with name %s does not exist', namik;
END IF;
END;
$$;