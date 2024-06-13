-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	UPDATE users
	SET average_score = (
		SELECT (sum_weighted_score / sum_weight) AS average_weighted_score
		FROM (
			SELECT SUM(projects.weight * corrections.score) AS sum_weighted_score,
			SUM(projects.weight) AS sum_weight
			FROM corrections JOIN projects ON corrections.project_id=projects.id
			WHERE corrections.user_id = users.id
		) AS temp
	);
END//
DELIMITER ;
