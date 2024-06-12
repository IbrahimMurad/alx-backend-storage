-- lists all bands with 'Glam rock' as their main style, ranked by their longevity
-- select the band name and the number of years they were active (split - formed) as lifespan
-- if the band is still active, use 2022 as the split year
SELECT band_name, (COALESCE(split, 2022) - formed) AS lifespan
	FROM metal_bands
	WHERE style LIKE '%Glam rock%'
	ORDER BY lifespan DESC;