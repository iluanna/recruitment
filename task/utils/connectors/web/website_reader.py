# TODO connector for reading local source (example_currency_rates.json) with currency rates
import requests

class WebsiteReader:
    def read_data(self, source: str, currency: str) -> dict:
        url = f"{source}exchangerates/rates/A/{currency}/"
        resp = requests.get(url)
        if resp.status_code != 200:
            raise Exception("Couldn't get data from source")
        return resp.json()

    def get_rate(self, data: dict) -> float:
        return data["rates"][0]["mid"]