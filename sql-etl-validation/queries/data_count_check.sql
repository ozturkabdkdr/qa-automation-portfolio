-- source vs target row count check
select 
  (select count(*) from source_db.users) as source_count,
  (select count(*) from dwh.dim_users) as target_count;
