import json

from extract.extractor import Extractor
from transform.transformer import Transformer
from load.loader import Loader

with open("config/config.json") as file:
    config = json.load(file)

extractor = Extractor(config["api_url"])

transformer = Transformer()

loader = Loader()

data = extractor.fetch_data()

df = transformer.transform(data)

loader.load_data(df)

print("ETL Pipeline Completed Sucessfully")
