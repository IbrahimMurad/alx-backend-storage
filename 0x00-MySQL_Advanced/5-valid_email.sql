-- creates a trigger that resets the attribute valid_email only when the email has been changed.

DELIMITER $$
CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email != NEW.email
		UPDATE users
		RESET users.valid_email
	END IF
END;
DELIMITER ;