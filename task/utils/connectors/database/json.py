import json
from ...config import JSON_DATABASE_NAME
from dataclasses import dataclass
from dacite import from_dict

@dataclass(frozen=True)
class DbEntity:
    id: float
    currency: str
    rate: float
    price_in_pln: float
    date: str


class JsonFileDatabaseConnector:
    def __init__(self) -> None:
        self._data = self._read_data()

    @staticmethod
    def _read_data() -> dict:
        with open(JSON_DATABASE_NAME, "r") as file:
            return json.load(file)
        
    def _write_data(self) -> None:
        with open(JSON_DATABASE_NAME, "w") as file:
            json.dump(self._data, file)

    def save(self, entity: dict) -> int:
        new_id = max(map(int, self._data.keys()), default=0) + 1
        entity["id"] = new_id
        self._data[str(new_id)] = entity
        self._write_data()
        return new_id

    def get_all(self) -> list[DbEntity]:
        all = []
        for v in self._data.values():
            item = from_dict(data_class=DbEntity, data=v)
            all.append(item)
        return all

    def get_by_id(self, id: int) -> DbEntity:
        try:
            obj = from_dict(data_class=DbEntity, data=self._data[str(id)])
        except KeyError:
            raise KeyError(f"Entity with id {id} not found in the database")
        return obj

