#### Autors: Anna Iluk, P.S.

- `example_currency_rates.json` - lokalne źródło danych z kursami walut
- `database.json` - testowa baza danych z zapisanymi kursami walut
- `database.sqlite3`- produkcyjna baza danych z zapisanymi kursami walut

Parametry wejściowe (w kolejności):
- kwota do wymiany
- waluta, z której nastąpi wymiana
- źródło danych dotyczących aktualnego kursu waluty
    - http://api.nbp.pl/api/
    - `example_currency_rates.json`

Tryb pracy jest ustawiany w pliku `task/utils/config.py` za pomocą zmiennej `MODE`.

