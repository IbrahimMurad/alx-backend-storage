-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
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
END//
DELIMITER ;