-- SQL script that creates trigger that decreases quant after adding a new item

CREATE TRIGGER order_decrease
BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
