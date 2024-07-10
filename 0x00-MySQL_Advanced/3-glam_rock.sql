-- List bands with Glam rock as thir main style ranked by longevity

select band_name, coalesce(split, 2022) - formed as lifespan from metal_bands
where style like '%Glam rock%' order by lifespan desc;
