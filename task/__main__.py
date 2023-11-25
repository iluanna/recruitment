import sys
from dataclasses import asdict
from utils.currency_converter import PriceCurrencyConverterToPLN
from utils.connectors.database.json import JsonFileDatabaseConnector
from utils.connectors.database.sql import SqlDatabaseConnector
from utils.config import MODE
from utils.logger import setup_logger

logger = setup_logger(__name__)

price = int(sys.argv[1])
currency = str(sys.argv[2])
source = str(sys.argv[3])
# possible sources:
# - http://api.nbp.pl/api/
# - example_currency_rates.json


"""
price = 20
currency = "eur"
source = "http://api.nbp.pl/api/"
"""

conv = PriceCurrencyConverterToPLN()

try:
    obj = conv.convert_to_pln(source, currency, price)
    d = asdict(obj)
    if MODE.lower() == "dev":
        j = JsonFileDatabaseConnector()
        j.save(d)
    elif MODE.lower() == "prod":
        sql = SqlDatabaseConnector()
        sql.save(d)
    logger.info(f"Job done! Actual rate: {obj.rate}")
except Exception as err:
    logger.error(err)
