CREATE PROCEDURE insertlist(names TEXT[], phones TEXT[]) 
LANGUAGE plpgsql
AS $$
DECLARE
i INTEGER;
invalid RECORD;
BEGIN
FOR i IN 1..array_length(names, 1) LOOP
    IF phones[i] ~ '^\d{11}$' THEN
        INSERT INTO phonebook (name, phone) VALUES (names[i], phones[i]);
    ELSE 
        RAISE NOTICE 'incorrect phone number % - %', name[i], phone[i];
    END IF;
END LOOP;
END;
$$;