import json
from sqlalchemy import create_engine


with open("config/config.json") as file:
    config = json.load(file)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{config['db_user']}:"
    f"{config['db_password']}@"
    f"{config['db_host']}:"
    f"{config['db_port']}/"
    f"{config['db_name']}"
)

engine = create_engine(DATABASE_URL)
