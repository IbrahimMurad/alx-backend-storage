-- create a trigger that will reduce the quantity of an item in the items table
-- when a new order is placed
DELIMITER $$
CREATE TRIGGER reduce_amount
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
		UPDATE items
		SET quantity = quantity - NEW.number
		WHERE name = NEW.item_name;
END;
DELIMITER ;