from dataclasses import dataclass
from datetime import datetime
from .connectors.local.file_reader import FileReader
from .connectors.web.website_reader import WebsiteReader

@dataclass(frozen=True)
class ConvertedPricePLN:
    currency: str
    rate: float
    price_in_pln: float
    date: str


class PriceCurrencyConverterToPLN:
    def convert_to_pln(self, source: str, currency: str, price: float) -> ConvertedPricePLN:
        if source == "example_currency_rates.json":
            fr = FileReader()
            data = fr.read_file(source)
            rate = fr.get_rate(data, currency)
        elif source == "http://api.nbp.pl/api/":
            wr = WebsiteReader()
            data = wr.read_data(source, currency)
            rate = wr.get_rate(data)
        else:
            raise Exception("Not supported data source")
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        return ConvertedPricePLN(currency, rate, rate*price, date)
    



