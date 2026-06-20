import requests
import os
import json


from utils.logger import logger


class Extractor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        logger.info("Extraction started..")

        response = requests.get(self.api_url)
        response.raise_for_status()
        data = response.json()

        os.makedirs("raw_data", exist_ok=True)

        with open("raw_data/orders.json", "w") as file:
            json.dump(data, file, indent=4)

        logger.info("Raw data saved.")

        return data
