SELECT
  f.key,
  f.b_date,
  MIN(s.s_date) AS s_date,
  FIRST_VALUE(s.price) OVER (PARTITION BY f.key, f.b_date ORDER BY ABS(DATEDIFF(day, f.b_date, s.s_date)), s.s_date) AS price
FROM
  first_table f
LEFT JOIN LATERAL (
  SELECT
    s_date,
    price
  FROM
    second_table s
  WHERE
    f.key = s.key
    AND (f.b_date = s.s_date OR s.s_date > f.b_date)
  ORDER BY
    CASE WHEN f.b_date = s.s_date THEN 0 ELSE 1 END, s.s_date
  LIMIT 1
) s ON TRUE
GROUP BY
  f.key,
  f.b_date
