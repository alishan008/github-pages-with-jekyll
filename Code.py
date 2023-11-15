WITH ranked_dates AS (
  SELECT
    f.key,
    f.b_date,
    s.s_date,
    s.price,
    FIRST_VALUE(s.s_date) OVER (PARTITION BY f.key, f.b_date 
                               ORDER BY CASE WHEN s.s_date >= f.b_date THEN s.s_date END) AS next_s_date
  FROM
    first_table f
  LEFT JOIN
    second_table s ON f.key = s.key
)

SELECT
  key,
  b_date,
  COALESCE(next_s_date, s_date) AS s_date,
  price
FROM
  ranked_dates
