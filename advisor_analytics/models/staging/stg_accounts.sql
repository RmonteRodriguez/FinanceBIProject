SELECT
    CAST(account_id AS INTEGER) AS account_id,
    CAST(client_id AS INTEGER) AS client_id,
    TRIM(account_type) AS account_type,
    CAST(open_date AS DATE) AS open_date,
    LOWER(TRIM(status)) AS status,
    CAST(balance AS NUMERIC) AS balance
FROM {{ source('seed_data', 'accounts') }}
