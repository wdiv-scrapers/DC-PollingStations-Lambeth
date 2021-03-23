from dc_base_scrapers.geojson_scraper import GeoJsonScraper
from dc_base_scrapers.hashonly_scraper import HashOnlyScraper

search_url = "https://opendata.arcgis.com/api/v3/datasets?q=polling&filter[owner]=opendata@lambeth.gov.uk&fields[datasets]=name,url"
stations_url = "https://opendata.arcgis.com/datasets/ae36e573b7a94632b1b2e585c30eda3d_0.geojson"
districts_url = "https://opendata.arcgis.com/datasets/82d23d4644634038ba18a2121e0e3129_0.geojson"
council_id = 'LBH'

search_scraper = HashOnlyScraper(search_url, council_id, 'datasets', 'json')
search_scraper.scrape(exclude_keys=['meta'])
stations_scraper = GeoJsonScraper(stations_url, council_id, 'utf-8', 'stations', key='OBJECTID')
stations_scraper.scrape()
districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts', key='OBJECTID')
districts_scraper.scrape()
