SELECT
  start_station_id,
	start_station_name,
	end_station_id,
	end_station_name,
	Count(tripduration) as tripcount
FROM citibike
GROUP BY
	start_station_id,
	start_station_name,
	end_station_id,
	end_station_name
ORDER BY
	tripcount DESC,
	start_station_id,
	end_station_id
LIMIT 10
