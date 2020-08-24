import geopandas as gpd

geojson_file='/home/rodrigo/Documents/_Thesis_Resources/_Data/cl_countrywide-addresses-country.geojson'
csv_file='/home/rodrigo/Documents/_Thesis_Resources/_Data/cl_countrywide-addresses-country.csv'

geodf=gpd.read_file(geojson_file)
geodf.to_csv(csv_file,sep=';')
