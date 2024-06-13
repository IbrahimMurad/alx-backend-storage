-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE user_id INT;
	DECLARE user_ids CURSOR FOR SELECT id FROM users;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
	
	OPEN user_ids;
	user_loop: LOOP
		FETCH user_ids INTO user_id;
		IF done THEN
			LEAVE user_loop;
		END IF;
		CALL ComputeAverageWeightedScoreForUser(user_id);
	END LOOP;
	
	CLOSE user_ids;
END //
DELIMITER ;
