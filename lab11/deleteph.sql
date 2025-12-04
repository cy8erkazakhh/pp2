CREATE PROCEDURE delete_phone(phoni TEXT)
LANGUAGE plpgsql
AS $$
BEGIN
IF phoni ~ '^\d{11}$' THEN
    IF EXISTS (
        SELECT 1 FROM phonebook 
        WHERE phone = phoni
    ) THEN
        DELETE FROM phonebook WHERE phone = phoni;
    ELSE
        RAISE NOTICE 'number phone (%) does not exist', phoni;
    END IF;
ELSE
    RAISE NOTICE 'enter correct phone number';
END IF;
END;
$$;