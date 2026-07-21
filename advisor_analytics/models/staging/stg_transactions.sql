SELECT
    transaction_id,
    account_id,
    txn_date,
    txn_type,
    amount,
    is_amount_missing
FROM (
    SELECT
        CAST(transaction_id AS INTEGER) AS transaction_id,
        CAST(account_id AS INTEGER)     AS account_id,
        CAST(txn_date AS DATE)          AS txn_date,
        LOWER(TRIM(txn_type))           AS txn_type,
        CASE WHEN amount IS NULL THEN 0.0 ELSE amount END AS amount,
        CASE WHEN amount IS NULL THEN 1 ELSE 0 END AS is_amount_missing,
        ROW_NUMBER() OVER (PARTITION BY transaction_id ORDER BY transaction_id) AS rn
    FROM {{ source('seed_data', 'transactions') }}
)
WHERE rn = 1