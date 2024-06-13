-- creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER valid_email
BEFORE UPDATE ON user
FOR EACH ROW
BEGIN
		IF NEW.email != OLD.email THEN
				RESET NEW.valid_email = 0;
		END IF;
END$$
DELIMITER ;