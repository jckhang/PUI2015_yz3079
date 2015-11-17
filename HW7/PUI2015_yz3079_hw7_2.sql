SELECT
	start_station_id,
	start_station_name,
	CDB_TransformToWebmercator(CDB_LatLng(
		start_station_latitude,
 		start_station_longitude
 		)
 	) as the_geom_webmercator,
	Count(tripduration) as tripcount
FROM citibike
WHERE
ST_dWithin(CDB_LatLng(
          end_station_latitude,
          end_station_longitude
          )::geography
           , CDB_LatLng(40.7307602, -73.9974086)::geography
           , 1000)
AND
	extract(DOW FROM starttime) IN (0,6)
GROUP BY
	start_station_id,
	start_station_name,
	start_station_longitude,
	start_station_latitude
ORDER BY
	tripcount DESC
