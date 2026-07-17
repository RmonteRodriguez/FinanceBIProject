SELECT
    CAST(client_id AS INTEGER) AS client_id,
    (SUBSTR(client_name,1,1) || LOWER(SUBSTR(client_name,2))) AS client_name,
    CAST(advisor_id AS INTEGER) AS advisor_id,
    UPPER(TRIM(state)) AS state,
    CAST(signup_date AS DATE) AS signup_date,
    NULLIF(TRIM(email), '') AS email
FROM {{ source('seed_data', 'clients') }}