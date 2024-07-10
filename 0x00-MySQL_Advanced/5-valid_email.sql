-- Create a trigger that resets the attribute valid_email
-- only when the email has been changed

delimiter $$

create trigger new_email before update on users
for each row
begin
        if OLD.email != NEW.email then
            set NEW.valid_email = 0;
        end if;
end$$

delimiter;
