# ETL Test Plan – User Data Pipeline

## Objective
Ensure that user data is correctly extracted, transformed, and loaded from source DB to DWH.

## Scope
- Source: `source_db.users`
- Target: `dwh.dim_users`
- Fields: `user_id`, `name`, `email`, `signup_date`, `is_active`

## Test Scenarios
1. Source data validation
2. Duplicate detection
3. Row count comparison
4. Transformation checks
5. Email formatting
6. Null checks

## Tools
- MySQL Workbench / DBeaver
- Pytest (optional)
- Airflow/Databricks (future)
