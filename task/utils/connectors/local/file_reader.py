# TODO connector for reading local source (example_currency_rates.json) with currency rates
import json

class FileReader:
    def read_file(self, source: str) -> dict:
        with open(source, "r") as file:
            return json.load(file)

    def get_rate(self, data: dict, currency: str) -> float:
        try:
            rate = data[currency.upper()][0]["rate"]
            # indeks 0, bo na podstawie zawartości pliku zakładam, że najświeższa data będzie miała indeks 0
        except KeyError:
            raise KeyError(f"Missing currency {currency} in this data source")
        return rate
