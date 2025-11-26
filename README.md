# LMU Meteo Data API

The Meteorological Institute of the Ludwig-Maximilian University (LMU) in Munich provides free high-quality meteodata for non-commercial use through a web API that can be accessed without authentication. This package should help to access the API and return the data as a dataframe.<br>
The package is published on PyPi for easy installation using pip.

> Don't forget to acknowledge the [Meteorological Institute of the LMU](https://www.meteo.physik.uni-muenchen.de/) if you use the data!

## API documentation
<url>https://www.meteo.physik.uni-muenchen.de/request-beta/</url>

## How to install

```
pip install lmu_meteo_api
```

## For developers

Set up you virtual environment
```bash
python3.10 -m venv .venv
```

Install dependencies
```bash
poetry install
```

(Optional) Publish new package
```bash
poetry build
poetry publish
```
