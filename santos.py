import geopandas as gpd
import matplotlib.pyplot as plt

# Carregando o shapefile
caminho_shapefile = r'C:\Users\UNIFESP\Desktop\heric_arquivos\geo\santos_shapefiles\ABAIRRAMENTO_LC1187-2022-SIR.shp'
gdf = gpd.read_file(caminho_shapefile)

# Visualizando o shapefile
gdf.plot()
plt.title("Mapa da Cidade de Santos")
plt.show()


# Usando uma coluna do shapefile para aplicar cores diferentes
gdf.plot(column='NOME', cmap='Set3', legend=True)
plt.title("Mapa dos Bairros de Santos")
plt.show()