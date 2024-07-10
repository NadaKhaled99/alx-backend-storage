-- Create function SafeDiv that divides (and returns) the first by the second number
-- or returns 0 if second number is equal to 0
-- Function SafeDiv takes 2 arguments: a, INT, b, INT
-- Return a / b or 0 if b == 0

delimiter //

drop function if exists SafeDiv;
create function SafeDiv(a INT, b INT)
returns float DETERMINISTIC
begin
	return (if (b = 0, 0, a / b));
end //

delimiter;
