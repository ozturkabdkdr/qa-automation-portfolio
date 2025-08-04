-- confirm target table row count matches source
select count(*) as row_count from dwh.dim_users;

-- check for business rule: email format
select * from dwh.dim_users where email not like '%@%.%';

-- check transformation logic: is_active should be boolean
select distinct is_active from dwh.dim_users;
