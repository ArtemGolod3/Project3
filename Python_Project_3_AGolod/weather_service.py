import requests
from typing import Dict, Any, List

from config import ACCUWEATHER_API_KEY


def get_city_data(city_name: str) -> Dict[str, Any]:
    search_url = "http://dataservice.accuweather.com/locations/v1/cities/search"
    params = {
        "apikey": ACCUWEATHER_API_KEY,
        "q": city_name,
        "language": "en-us"
    }

    resp = requests.get(search_url, params=params, timeout=10)
    resp.raise_for_status()
    results: List[Dict[str, Any]] = resp.json()

    if not results:
        raise ValueError(f"Город не обнаружен: {city_name}")

    best_match = results[0]
    location_key = best_match.get("Key", "")
    geo_info = best_match.get("GeoPosition", {})
    lat = geo_info.get("Latitude", 0.0)
    lon = geo_info.get("Longitude", 0.0)

    return {
        "city_key": location_key,
        "latitude": lat,
        "longitude": lon,
        "city_name": city_name
    }


def get_extended_forecast(city_key: str, days: int) -> Dict[str, Any]:
    if days not in [1, 3, 5]:
        raise ValueError("Допустимое количество дней прогноза: 1, 3 или 5.")

    base_url = f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{city_key}"
    params = {
        "apikey": ACCUWEATHER_API_KEY,
        "language": "en-us",
        "metric": "true"
    }

    response = requests.get(base_url, params=params, timeout=10)
    response.raise_for_status()
    data: Dict[str, Any] = response.json()

    if "DailyForecasts" in data:
        data["DailyForecasts"] = data["DailyForecasts"][:days]

    return data
