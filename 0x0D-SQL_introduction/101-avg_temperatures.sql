-- Syntax used import dump table

SELECT city,AVG(value) as avg_temp FROM tempratures GROUP BY city ORDER BY avg_temp DESC;



