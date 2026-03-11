import requests
import pandas as pd
import numpy as np
from datetime import datetime

BASE_URL = "https://www.meteo.physik.uni-muenchen.de/request-beta/data/"


class meteo_data:
    """Interface to the LMU Meteorology API."""

    def __init__(self, timeout: int = 30) -> None:
        self.timeout = timeout

    def _z_score(self, series: pd.Series) -> pd.Series:
        """Returns the absolute z-score for each value in the series."""
        return np.abs((series - series.mean()) / series.std())

    def get_meteo_data(
        self,
        parameters: list[str],
        station_id: str,
        start_time: datetime | str,
        end_time: datetime | str,
        celcius: bool = True,
    ) -> pd.DataFrame:
        """Retrieve meteorological data from the LMU meteo API.

        Args:
            parameters: Meteo parameters to download.
            station_id: Station identifier (e.g. 'MIM01' for city, 'MIM03' for Garching).
            start_time: Start of the retrieval period (datetime or 'YYYY-MM-DDTHH-MM-SS').
            end_time: End of the retrieval period (datetime or 'YYYY-MM-DDTHH-MM-SS').
            celcius: Whether to convert temperature parameters from Kelvin to Celsius.
        Returns:
            DataFrame with cleaned meteo data indexed by UTC timestamp.

        Raises:
            requests.HTTPError: If the API returns a non-200 status code.
            requests.RequestException: If the request fails (e.g. network error).
            ValueError: If the response cannot be parsed.
        """
        if isinstance(start_time, datetime):
            start_time = start_time.strftime("%Y-%m-%dT%H-%M-%S")
        if isinstance(end_time, datetime):
            end_time = end_time.strftime("%Y-%m-%dT%H-%M-%S")

        url = (
            f"{BASE_URL}var={'+'.join(parameters)}"
            f"&station={station_id}"
            f"&start={start_time}&end={end_time}"
        )
        r = requests.get(url, timeout=self.timeout)
        r.raise_for_status()

        lmu_data = r.json()
        lmu_weather = pd.DataFrame(columns=parameters)
        lmu_weather["time"] = pd.to_datetime(lmu_data["time"], unit="s", utc=True)
        for par in parameters:
            lmu_weather[par] = pd.DataFrame(lmu_data[station_id][par])
            lmu_weather[par] = lmu_weather[par].loc[self._z_score(lmu_weather[par]) < 3]
        lmu_weather = lmu_weather.dropna()
        lmu_weather.set_index("time", inplace=True)
        lmu_weather.sort_index(inplace=True)
        
        if celcius:
            temp_parameters = [par for par in parameters if "temperature" in par.lower()]
            lmu_weather = self.to_celcius(lmu_weather, temp_parameters)

        return lmu_weather


    def to_celcius(self, df: pd.DataFrame, parameters: list[str]) -> pd.DataFrame:
        """Convert temperature parameters from Kelvin to Celsius."""
        for par in parameters:
            if "temp" in par.lower():
                df[par] = df[par] - 273.15
        return df
