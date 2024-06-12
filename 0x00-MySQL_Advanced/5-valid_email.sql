-- creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
		IF NEW.email != OLD.email AND NEW.valid_email = OLD.valid_email THEN
				SET users.valid_email = 0;
		END IF;
END;
DELIMITER ;
