-- creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
		DECLARE done INT DEFAULT 0;
		DECLARE user_id INT;
		DECLARE total_score DECIMAL(5,2);
		DECLARE total_weight DECIMAL(5,2);
		DECLARE average_score DECIMAL(5,2);
		DECLARE average_weighted_score DECIMAL(5,2);
		DECLARE cur CURSOR FOR SELECT user_id FROM users;
		DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

		OPEN cur;
		read_loop: LOOP
				FETCH cur INTO user_id;
				IF done THEN
						LEAVE read_loop;
				END IF;

				SET total_score = 0;
				SET total_weight = 0;
				SET average_score = 0;
				SET average_weighted_score = 0;

				SELECT SUM(score) INTO total_score FROM scores WHERE user_id = user_id;
				SELECT SUM(weight) INTO total_weight FROM scores WHERE user_id = user_id;

				IF total_weight > 0 THEN
						SET average_score = total_score / total_weight;
				END IF;

				INSERT INTO average_weighted_score (user_id, average_weighted_score) VALUES (user_id, average_score);
		END LOOP;
		CLOSE cur;
END$$
DELIMITER ;
