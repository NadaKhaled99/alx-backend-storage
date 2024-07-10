-- Create stored procedure ComputeAverageScoreForUser
-- computes and stores average score for a student


delimiter $$

drop procedure if exists ComputeAverageScoreForUser;
create procedure ComputeAverageScoreForUser (in user_id int)
begin
	update users
	set
	average_score = (select avg(score) from corrections where corrections.user_id = user_id)
	where id = user_id;

end $$

delimiter;
