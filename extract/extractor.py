import requests
import os
import json


from utils.logger import logger


class Extractor:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        logger.info("Extraction started")
