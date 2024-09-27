from typing import Union

dict_lists = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(list_of_dicts: Union[list[dict[str, int]]], state: str = "EXECUTED") -> list[dict]:
    """Фильтр словарей по переданному значению"""
    filtered_dicts = [i for i in list_of_dicts if i.get("state") == state]

    return sorted(filtered_dicts, key=lambda x: x["state"])


def sort_by_date(list_of_dicts: Union[list[dict[str, int]]], sort: bool = True) -> list[dict]:
    """Фильтр словарей по дате"""
    for i in list_of_dicts:
        list_of_dicts.sort(key=lambda x: x["date"], reverse=sort)
    return list_of_dicts


result_filter_by_state = filter_by_state(dict_lists)
result_sort_by_date = sort_by_date(dict_lists)
