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
		UPDATE users
		SET average_score = (
			SELECT (sum_weighted_score / sum_weight) AS average_weighted_score
			FROM (
				SELECT SUM(projects.weight * corrections.score) AS sum_weighted_score,
				SUM(projects.weight) AS sum_weight
				FROM corrections JOIN projects ON corrections.project_id=projects.id
				WHERE corrections.user_id = user_id
			) AS temp
		)
		WHERE users.id = user_id;
	END LOOP;

	CLOSE user_ids;
END //
DELIMITER ;
