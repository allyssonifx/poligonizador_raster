import rasterio
from rasterio.features import shapes
mask = None
lista_estados = ['CE','DF','ES','GO','MA','MT','MS','MG','PA','PB','PE','PI','PR','RR','RO','RJ','RN','RS','SC','SP','SE','TO']
caminho = r'CAMINHO AQUI'
for es in lista_estados:
    with rasterio.Env():
        with rasterio.open(caminho+'\\mapbiomas_'+es+'.tif') as src:
            image = src.read(1) # first band
            results = (
            {'properties': {'raster_val': v}, 'geometry': s}
            for i, (s, v) 
            in enumerate(
                shapes(image, mask=mask, transform=src.transform)))
            
    print('leu raster')
    geoms = list(results)
    from shapely.geometry import shape
    geometrias = []
    for c in range(0,len(geoms)):
        if int(geoms[c]['properties']['raster_val']) == 39:
            print(int(geoms[c]['properties']['raster_val']))
            geometrias.append(shape(geoms[c]['geometry']))

    print('leu 39')

    import geopandas as gpd
    df = gpd.GeoDataFrame({'geometry':geometrias})
    df.set_geometry('geometry',inplace=True,crs='epsg:4326')
    df.to_file('mapbiomas_'+es+'.shp')