from database.db_connection import engine
from utils.logger import logger


class Loader:
    def load_data(self, df):

        logger.info("Loading Stareted.")

        df.to_sql("orders", engine, if_exists="append", index=False)

        logger.info("Loading completed.")
