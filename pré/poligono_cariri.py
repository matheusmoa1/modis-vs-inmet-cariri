import geopandas as gpd

gdf = gpd.read_file('cariri_paraibano.geojson')

gdf_unido = gdf.dissolve()

gdf_unido.to_file('cariri_paraibano_unido.geojson', driver='GeoJSON')