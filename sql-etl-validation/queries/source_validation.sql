-- check if source table has data
select count(*) as row_count from source_db.users;

-- check for duplicate records based on user_id
select user_id, count(*) 
from source_db.users 
group by user_id 
having count(*) > 1;

-- check for nulls in critical columns
select * from source_db.users where user_id is null or email is null;
