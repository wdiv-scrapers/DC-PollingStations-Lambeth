from dc_base_scrapers.arcgis_scraper import ArcGisScraper


stations_url = "http://gis.lambeth.gov.uk/arcgis/rest/services/ElectoralServices/MapServer/0/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPoint&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
districts_url = "http://gis.lambeth.gov.uk/arcgis/rest/services/ElectoralServices/MapServer/1/query?where=1%3D1&text=&objectIds=&time=&geometry=&geometryType=esriGeometryPolygon&inSR=&spatialRel=esriSpatialRelIntersects&relationParam=&outFields=*&returnGeometry=true&maxAllowableOffset=&geometryPrecision=&outSR=4326&returnIdsOnly=false&returnCountOnly=false&orderByFields=OBJECTID&groupByFieldsForStatistics=&outStatistics=&returnZ=false&returnM=false&gdbVersion=&returnDistinctValues=false&f=pjson"
council_id = 'E09000022'


stations_scraper = ArcGisScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID_1')
stations_scraper.scrape()
districts_scraper = ArcGisScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID_1')
districts_scraper.scrape()
