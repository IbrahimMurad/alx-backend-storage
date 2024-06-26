-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input:
--		user_id, a users.id value (you can assume user_id is linked to an existing users)

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id FLOAT)
BEGIN
	UPDATE users
	SET average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id)
	WHERE users.id = user_id;
END //

DELIMITER ;
