import requests
from pprint import pprint


def get_census_tract(address: str) -> str:
    url = "https://geocoding.geo.census.gov/geocoder/geographies/onelineaddress"  # noqa: E501
    query_string = {
        "benchmark": "Public_AR_Current",
        "vintage": "Current_Current",
        "address": address,
        "format": "json",
    }
    r = requests.get(url, params=query_string)
    pprint(s := r.json())
    return s["result"]["addressMatches"][0]["geographies"]["Census Tracts"][0][
        "GEOID"
    ]  # noqa: E501
