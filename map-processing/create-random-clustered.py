import processing

distances = [
    100,
    1000,
    2500,
    5000,
    10000,
    15000
]

expos = [
    1,
    100,
    1000,
    2500
]

maxs = [
    2,
    4
]

for distanceIndex in range(len(distances)):
    for exposIndex in range(len(expos)):
        for maxsIndex in range(len(maxs)):
            distance = distances[distanceIndex]
            expo = expos[exposIndex]
            max = maxs[maxsIndex]
            imageFile = '/Users/daveism/capstone/tiffs/random-clustered/random_clustered-d-' + str(distance) + '-e-' + str(expo) + '-max-' + str(max) + '.tif'
            shpFile = '/Users/daveism/capstone/tiffs/random-clustered/random_clustered-d-' + str(distance) + '-e-' + str(expo)  + '-max-' + str(max) + '.shp'
            params = {
                '-u': True,
                'GRASS_RASTER_FORMAT_META': 'PROFILE=GeoTIFF,TFW=YES,type=Byte,COMPRESS=LZW',
                'GRASS_RASTER_FORMAT_OPT': '',
                'GRASS_REGION_CELLSIZE_PARAMETER': 240,
                'GRASS_REGION_PARAMETER': '-9787149.877532974,-9655629.877532974,3882750.326433916,3986670.326433916 [EPSG:4326]',
                'distance': distance,
                'exponent': expo,
                'flat': 1,
                'high': max,
                'seed': None,
                'output': imageFile
            }
            # create tiles
            res = processing.run('grass7:r.random.surface', params)
            
            alg_params = {
                'CRS': QgsCoordinateReferenceSystem('EPSG:3857'),
                'INPUT': imageFile
            }               
            res = processing.run('gdal:assignprojection', alg_params)

            alg_params = {
                'BAND': 1,
                'EIGHT_CONNECTEDNESS': True,
                'EXTRA': '',
                'FIELD': 'DN',
                'INPUT': imageFile,
                'OUTPUT': shpFile
            }
            res = processing.run('gdal:polygonize', alg_params)