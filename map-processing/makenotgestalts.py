targets = [
    '01',
    '02',
    '03',
    '04',
    '05',
    '06',
    '07',
    '08',
    '09',
    '10',
    '11',
    '12',
    '13',
    '14',
    '15',
    '16',
    '17',
    '18',
    '19',
    '20',
    '21',
    '22',
    '23',
    '24',
    '25',
    '26',
    '27',
    '28',
    '29',
    '30',
    '31',
    '32',
    '33',
    '34',
    '35',
    '36',
    '37',
    '38',
    '39',
    '40',
    '41',
    '42',
    '43',
    '44',
    '45',
    '46',
    '47',
    '48',
    '49',
    '50'
]

layer1 = iface.mapCanvas().layers()[0]
print(layer1)

basepath = '/Users/daveism/capstone/shapefiles/targets/'
for target in range(len(targets)):
    path = basepath + 'tornado-notgestalt-v2-' + targets[target] + '.shp'
    _writer = QgsVectorFileWriter.writeAsVectorFormat(layer1,path,"utf-8",layer1.crs(),"ESRI Shapefile")

    