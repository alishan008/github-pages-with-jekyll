WITH ranked_dates AS (
  SELECT
    f.key,
    f.b_date,
    s.s_date,
    s.price,
    LEAD(s.s_date) OVER (PARTITION BY f.key ORDER BY s.s_date) AS next_s_date
  FROM
    first_table f
  LEFT JOIN
    second_table s ON f.key = s.key
)

SELECT
  key,
  b_date,
  s_date,
  price
FROM (
  SELECT
    key,
    b_date,
    s_date,
    price,
    ROW_NUMBER() OVER (PARTITION BY key, b_date ORDER BY 
                       CASE WHEN b_date = s_date THEN 0 ELSE 1 END, s_date) AS row_num
  FROM
    ranked_dates
  WHERE
    b_date = s_date OR (b_date < s_date AND (next_s_date = b_date OR next_s_date IS NULL))
) result
WHERE
  row_num = 1
