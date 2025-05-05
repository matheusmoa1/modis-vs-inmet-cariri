import json

# Carregar o GeoJSON com todos os municípios da Paraíba
with open('geojs-25-mun.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Lista de municípios do Cariri Paraibano
cariri_municipios = [
    "Monteiro", "Sumé", "Serra Branca", "Taperoá", "Coxixola", "Zabelê",
    "São João do Tigre", "São Sebastião do Umbuzeiro", "Camalaú", "Congo",
    "Caraúbas", "Ouro Velho", "Prata", "Gurjão", "Livramento",
    "São José dos Cordeiros", "Parari", "Cabaceiras", "Boa Vista", "Pocinhos",
    "Areial", "Gado Bravo", "Barra de Santana", "Queimadas", "Boqueirão",
    "Riacho de Santo Antônio", "Alcantil", "Santa Cecília", "Caturité"
]

# Filtrar apenas os municípios do Cariri
cariri_features = [
    feature for feature in data['features']
    if feature['properties']['name'].strip() in cariri_municipios
]

# Salvar o novo GeoJSON com os municípios do Cariri Paraibano
cariri_geojson = {'type': 'FeatureCollection', 'features': cariri_features}

with open('cariri_paraibano.geojson', 'w', encoding='utf-8') as f:
    json.dump(cariri_geojson, f, ensure_ascii=False, indent=4)

print("GeoJSON do Cariri Paraibano gerado com sucesso!")
