SELECT
    CAST(advisor_id AS INTEGER) AS advisor_id,
    TRIM(advisor_name) AS advisor_name,
    UPPER(TRIM(region)) AS region,
    CAST(hire_date AS DATE) AS hire_date
FROM {{ source('seed_data', 'advisors') }}