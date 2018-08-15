{'title': 'Understanding Priorities',
 'model': {'items': [{'operation': 'add-data',
    'params': {'data': {'type': 'feature-layer',
      'url': 'https://servicesdev.arcgis.com/gKIM0DxFtj9ijTZo/arcgis/rest/services/Snowfall_data/FeatureServer/0'}},
    'outDataset': 'Traffic_incidents_faf3441'},
   {'operation': 'add-data',
    'params': {'data': {'type': 'feature-layer',
      'url': 'https://servicesdev.arcgis.com/gKIM0DxFtj9ijTZo/arcgis/rest/services/Snowfall_data/FeatureServer/1'}},
    'outDataset': 'Schools_Locations_af6f275'},
   {'operation': 'add-data',
    'params': {'data': {'type': 'feature-layer',
      'url': 'https://servicesdev.arcgis.com/gKIM0DxFtj9ijTZo/arcgis/rest/services/Snowfall_data/FeatureServer/3'}},
    'outDataset': 'T2017_Citizens_Complaints_9469f93'},
   {'operation': 'add-data',
    'params': {'data': {'type': 'feature-layer',
      'url': 'https://servicesdev.arcgis.com/gKIM0DxFtj9ijTZo/arcgis/rest/services/Snowfall_data/FeatureServer/4'}},
    'outDataset': 'Maintenance_Districts_38d8b56'},
   {'operation': 'add-data',
    'params': {'data': {'type': 'feature-layer',
      'url': 'https://servicesdev.arcgis.com/gKIM0DxFtj9ijTZo/arcgis/rest/services/Roads_Priorities/FeatureServer/0'}},
    'outDataset': 'Route_Planning_2fee8bb'},
   {'operation': 'calc-field',
    'params': {'dataset': 'Route_Planning_2fee8bb',
     'calcs': [{'expression': 'shape__Length/1.609344',
       'outField': 'mileage'}]},
    'outDataset': 'Route_Planning_9e29d42'},
   {'operation': 'aggregateByPoly',
    'params': {'pointDataset': 'T2016_Citizens_Complaints_5f18b08',
     'polygonDataset': 'Maintenance_Districts_38d8b56',
     'summaryFields': [{'field': 'objectid',
       'type': 'count',
       'outField': 'objectid_count'}]},
    'outDataset': 'Maintenance_Districts_36ba8cd'},
   {'operation': 'style-layer',
    'params': {'dataset': 'Maintenance_Districts_36ba8cd',
     'type': 'size',
     'field': 'objectid_count',
     'classify': {'method': 'natural-breaks', 'classes': 5},
     'symbol': {'outline': {}, 'color': '#73b2ff'}},
    'outDataset': 'Maintenance_Districts_ecb9660'},
   {'operation': 'aggregateByPoly',
    'params': {'pointDataset': 'Traffic_incidents_faf3441',
     'polygonDataset': 'Maintenance_Districts_38d8b56',
     'summaryFields': [{'field': 'objectid',
       'type': 'count',
       'outField': 'objectid_count'}]},
    'outDataset': 'Maintenance_Districts_0cc5fcd'},
   {'operation': 'aggregateByPoly',
    'params': {'pointDataset': 'Route_Planning_9e29d42',
     'polygonDataset': 'Maintenance_Districts_38d8b56',
     'summaryFields': [{'field': 'objectid',
       'type': 'count',
       'outField': 'objectid_count'},
      {'field': 'mileage', 'type': 'sum', 'outField': 'mileage_sum'}]},    'outDataset': 'Maintenance_Districts_606a52f'},
   {'operation': 'style-layer',
    'params': {'dataset': 'Maintenance_Districts_606a52f',
     'type': 'size',
     'field': 'objectid_count',
     'classify': {'method': 'natural-breaks', 'classes': 5}},
    'outDataset': 'Maintenance_Districts_bf6ee06'},
   {'operation': 'aggregateByPoly',
    'params': {'pointDataset': 'Schools_Locations_af6f275',
     'polygonDataset': 'Maintenance_Districts_38d8b56',
     'summaryFields': [{'field': 'objectid',
       'type': 'count',
       'outField': 'objectid_count'}]},
    'outDataset': 'Maintenance_Districts_070eb07'},
   {'operation': 'style-layer',
    'params': {'dataset': 'Maintenance_Districts_070eb07',
     'type': 'size',
     'field': 'objectid_count',
     'classify': {'method': 'natural-breaks', 'classes': 5},
     'symbol': {'outline': {}, 'color': '#55ff00'}},
    'outDataset': 'Maintenance_Districts_13fcb8f'},
   {'operation': 'join',
    'params': {'dataset': 'DC608CA2-92C8-E711-80C2-0003FF2A4807_e046e88',
     'fields': None,
     'joins': [{'fields': [{'left': 'districts',
         'right': 'name',
         'op': 'EQUALS'}],
       'dataset': 'Maintenance_Districts_38d8b56',
       'type': 'INNER',
       'joins': []}]},
    'outDataset': 'D847B8DD-73C6-E711-80C2-0003FF2A4807_0f0c356'},
   {'operation': 'aggregate',
    'params': {'dataset': 'Maintenance_Districts_36ba8cd',
     'statistics': [{'type': 'sum',
       'field': 'objectid_count',
       'outField': 'objectid_count_sum'}],
     'groupBy': ['name']},
    'outDataset': 'Maintenance_Districts_846065e'},
   {'operation': 'aggregate',
    'params': {'dataset': 'Maintenance_Districts_0cc5fcd',
     'statistics': [{'type': 'sum',
       'field': 'objectid_count',
       'outField': 'objectid_count_sum'}],
     'groupBy': ['name']},
    'outDataset': 'Maintenance_Districts_8d8c693'},
   {'operation': 'aggregate',
    'params': {'dataset': 'Maintenance_Districts_606a52f',
     'statistics': [{'type': 'sum',
       'field': 'mileage_sum',
       'outField': 'mileage_sum_sum'}],
     'groupBy': ['name']},
    'outDataset': 'Maintenance_Districts_bcce821'},
   {'operation': 'aggregate',
    'params': {'dataset': 'Maintenance_Districts_070eb07',
     'statistics': [{'type': 'sum',
       'field': 'objectid_count',
       'outField': 'objectid_count_sum'}],
     'groupBy': ['name']},
    'outDataset': 'Maintenance_Districts_ef6104b'},
   {'operation': 'aggregateByPoly',
    'params': {'pointDataset': 'Traffic_incidents_faf3441',
     'polygonDataset': 'Maintenance_Districts_38d8b56',
     'summaryFields': [{'field': 'objectid',
       'type': 'count',
       'outField': 'objectid_count'}]},
    'outDataset': 'Maintenance_Districts_5c2f7f5'},
   {'operation': 'style-layer',
    'params': {'dataset': 'Maintenance_Districts_5c2f7f5',
     'type': 'size',
     'field': 'objectid_count',
     'classify': {'method': 'natural-breaks', 'classes': 5},
     'symbol': {'outline': {'color': 'rgba(255, 255, 255, 1)', 'width': 1},
      'color': 0}},
    'outDataset': 'Maintenance_Districts_9fab892'}]},
 'cards': [{'title': 'Public Works Snow Operations Map',
   'type': 'map',
   'content': {'layers': [{'datasetId': 'Maintenance_Districts_38d8b56'},
     {'datasetId': 'Maintenance_Districts_bf6ee06', 'hidden': False},
     {'datasetId': 'Route_Planning_9e29d42', 'hidden': True},
     {'datasetId': 'T2016_Citizens_Complaints_5f18b08',
      'hidden': True,
      'transparency': 30,
      'drawingOptions': {'type': 'heatmap'}},
     {'datasetId': 'Traffic_incidents_faf3441', 'hidden': True},
     {'datasetId': 'Schools_Locations_af6f275', 'hidden': True}]}},
  {'title': 'Complaints by Districts',
   'type': 'map',
   'content': {'layers': [{'datasetId': 'Maintenance_Districts_ecb9660',
      'hidden': False}]}},
  {'title': 'Schools by Districts',
   'type': 'map',
   'content': {'layers': [{'datasetId': 'Maintenance_Districts_13fcb8f',
      'hidden': False}]}},
  {'title': 'Complaints Tree Map by districts',
   'type': 'chart',
   'content': {'type': 'treemap',
    'layers': [{'datasetId': 'Maintenance_Districts_ecb9660',
      'mappings': {'x': 'shape', 'y': 'objectid_count'},
      'color': 0,
      'colors': {'31': 12,
       '69': 15,
       '91': 17,
       '112': 18,
       '213': 13,
       '422': 16,
       '758': 21,
       '1136': 19,
       '1143': 20,
       '1512': 14,
       '1561': 11,
       'Snowmap 4A': 0,
       'Snowmap 1A': 1,
       'Snowmap 2A': 2,
       'Snowmap 3A': 3,
       'Snowmap 5A': 4,
       'Snowmap 1B': 5,
       'Snowmap 2B': 6,
       'Snowmap 3B': 7,
       'Snowmap 5B': 8,
       'Snowmap 4B': 9,
       'Snowmap 4C': 10}}]},
   'description': 'This tree map contains a diagram representing hierarchicaldata of citizens complaints by district in the city.'},
  {'title': 'Schools Tree Map by districts',
   'type': 'chart',
   'content': {'type': 'treemap',
    'layers': [{'datasetId': 'Maintenance_Districts_13fcb8f',
      'mappings': {'x': 'shape', 'y': 'objectid_count'},
      'color': 2,
      'colors': {'Snowmap 4A': 0,
       'Snowmap 1A': 1,
       'Snowmap 2A': 2,
       'Snowmap 3A': 3,
       'Snowmap 5A': 4,
       'Snowmap 1B': 5,
       'Snowmap 2B': 6,
       'Snowmap 3B': 7,
       'Snowmap 5B': 8,
       'Snowmap 4B': 9,
       'Snowmap 4C': 10}}]},
   'description': 'This tree map contains a diagram representing hierarchicaldata of schools by district in the city.'},
  {'title': 'Complaints ∑ by Districts',
   'type': 'chart',
   'content': {'type': 'line',
    'layers': [{'datasetId': 'Maintenance_Districts_846065e',
      'chartLines': {'mean': True},
      'color': 3}],
    'sorting': 'alph'}},
  {'title': 'Collisions ∑ by Districts',
   'type': 'chart',
   'content': {'type': 'line',
    'layers': [{'datasetId': 'Maintenance_Districts_8d8c693',
      'chartLines': {'mean': True},
      'color': 4}],
    'sorting': 'alph'}},
  {'title': 'Routes Mileage ∑ by Districts',
   'type': 'chart',
   'content': {'type': 'line',
    'layers': [{'datasetId': 'Maintenance_Districts_bcce821',
      'chartLines': {'mean': True},
      'color': 0}],
    'sorting': 'alph'}},
  {'title': 'Schools ∑ by Districts',
   'type': 'chart',
   'content': {'type': 'line',
    'layers': [{'datasetId': 'Maintenance_Districts_ef6104b',
      'chartLines': {'mean': True},
      'color': 0}],
    'sorting': 'alph'}},
  {'title': 'Collisions by District',
   'type': 'map',
   'content': {'layers': [{'datasetId': 'Maintenance_Districts_9fab892'}]}},
  {'title': 'Collisions Tree Map by districts',
   'type': 'chart',
   'content': {'type': 'treemap',
    'layers': [{'datasetId': 'Maintenance_Districts_5c2f7f5',
      'mappings': {'x': 'shape'},
      'color': 1,
      'colors': {'Snowmap 4A': 0,
       'Snowmap 1A': 1,
       'Snowmap 2A': 2,
       'Snowmap 3A': 3,
       'Snowmap 5A': 4,
       'Snowmap 1B': 5,
       'Snowmap 2B': 6,
       'Snowmap 3B': 7,
       'Snowmap 5B': 8,
       'Snowmap 4B': 9,
       'Snowmap 4C': 10}}]}}],
 'layout': [{'x': 0, 'y': 0, 'w': 5, 'h': 9, 'z': 20},
  {'x': 5, 'y': 0, 'w': 4, 'h': 4},
  {'x': 13, 'y': 0, 'w': 4, 'h': 4},
  {'x': 5, 'y': 4, 'w': 4, 'h': 5, 'z': 18},
  {'x': 13, 'y': 4, 'w': 4, 'h': 5, 'z': 24},
  {'x': 5, 'y': 9, 'w': 4, 'h': 4, 'z': 21},
  {'x': 9, 'y': 9, 'w': 4, 'h': 4},
  {'x': 0, 'y': 9, 'w': 5, 'h': 4, 'z': 22},
  {'x': 13, 'y': 9, 'w': 4, 'h': 4},
  {'x': 9, 'y': 0, 'w': 4, 'h': 4},
  {'x': 9, 'y': 4, 'w': 4, 'h': 5, 'z': 23}],
 'contents': [{'dataset': 'Traffic_incidents_faf3441'},
  {'dataset': 'Schools_Locations_af6f275'},
  {'dataset': 'T2016_Citizens_Complaints_5f18b08'},
  {'dataset': 'T2017_Citizens_Complaints_9469f93'},
  {'dataset': 'Maintenance_Districts_38d8b56'},
  {'dataset': 'Route_Planning_9e29d42'},
  {'dataset': 'D847B8DD-73C6-E711-80C2-0003FF2A4807_0f0c356', 'result': True},
  {'dataset': 'DC608CA2-92C8-E711-80C2-0003FF2A4807_e046e88'},
  {'dataset': 'Maintenance_Districts_36ba8cd', 'result': True},
  {'dataset': 'Maintenance_Districts_0cc5fcd', 'result': True},
  {'dataset': 'Maintenance_Districts_606a52f', 'result': True},
  {'dataset': 'Maintenance_Districts_070eb07', 'result': True},
  {'dataset': 'Maintenance_Districts_5c2f7f5', 'result': True}],
 'basemap': '3bf493a35b1c493292c1c62551c5c230'}