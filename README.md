# LMU Meteo Data API

The LMU provides free high-quality meteodata through a web API, accessible without authentication. This package helps access the API and returns data as a DataFrame.

The package is published on PyPI.

> **Note:** Data access is free for non-commercial use. No accuracy guarantees are provided. If you publish anything based on this data, please acknowledge the [Meteorological Institute of LMU](https://www.meteo.physik.uni-muenchen.de/) in your acknowledgements.

## API documentation

<https://www.meteo.physik.uni-muenchen.de/request-beta/>

## Installation

```bash
pip install lmu-weather-api
```

Or with [uv](https://docs.astral.sh/uv/):

```bash
uv add lmu-weather-api
```

## For developers

Clone the repository and set up the environment with uv:

```bash
git clone <repo-url>
cd lmu_weather_api
uv sync --group dev
```

Run scripts or notebooks:

```bash
uv run jupyter notebook
uv run python your_script.py
```

### Publishing

Build and publish a new release:

```bash
uv build
uv publish
```
