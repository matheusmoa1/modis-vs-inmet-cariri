import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

cariri = gpd.read_file('cariri_paraibano.geojson')
cariri = cariri.to_crs(epsg=4326)

def filtrar_estacoes(caminho_csv, fonte, col_lat='VL_LATITUDE', col_lon='VL_LONGITUDE'):
    df = pd.read_csv(caminho_csv, sep=';', on_bad_lines='skip')
    df[col_lat] = df[col_lat].astype(str).str.replace(',', '.').astype(float)
    df[col_lon] = df[col_lon].astype(str).str.replace(',', '.').astype(float)

    geometry = [Point(xy) for xy in zip(df[col_lon], df[col_lat])]
    gdf = gpd.GeoDataFrame(df, geometry=geometry, crs='EPSG:4326')

    estacoes_filtradas = gdf[gdf.within(cariri.unary_union)].copy()
    estacoes_filtradas['Fonte'] = fonte
    return estacoes_filtradas

inmet_auto = filtrar_estacoes('inmet_automaticas.csv', 'INMET Automática')
inmet_conv = filtrar_estacoes('inmet_convencionais.csv', 'INMET Convencional')
todas_estacoes_cariri = pd.concat([inmet_auto, inmet_conv], ignore_index=True)
todas_estacoes_cariri.to_csv('inmet_estacoes_cariri.csv', index=False)
