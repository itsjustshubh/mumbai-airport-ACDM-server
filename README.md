# Airport Status Dashboard

This project provides a Flask-based backend API to fetch various airport-related statuses such as arrival, departure, TSAT, and real-time movement data. The data is fetched from specified URLs and parsed into structured JSON formats.

## Project Structure

```
airport-status-dashboard/
├── app.py
├── arr_status.py
├── dep_status.py
├── div_chart_test.py
├── tsat_status.py
├── show_stations.py
├── utils.py
├── requirements.txt
├── Makefile
└── README.md
```

## Files Description

- **app.py**: The main Flask application that provides endpoints to retrieve different statuses.
- **arr_status.py**: Fetches and prints arrival status data.
- **dep_status.py**: Fetches and prints departure status data.
- **div_chart_test.py**: Fetches, processes, and prints real-time movement data from JavaScript datasets.
- **tsat_status.py**: Fetches and prints TSAT status data.
- **show_stations.py** Fethes and prints live Weather data for (VABB) Bombay Airport.
- **utils.py**: Utility functions for fetching data, extracting table data, and generating headers.
- **requirements.txt**: Contains the Python dependencies for the project.
- **Makefile**: Provides commands to set up, run, and clean the project.
- **README.md**: This file, which provides an overview and setup instructions for the project.

## Setup Instructions

### Prerequisites

- Python 3.12+
- pip (Python package installer)
- make (build automation tool)

### Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/itsjustshubh/airport-status-dashboard.git
   cd airport-status-dashboard
   ```

2. **Set up the environment and install dependencies:**

   You may copy the PHPSESSID provided if you don't have your own

   ```sh
   make setup
   ```

3. **Launch the application:**

   ```sh
   make run
   ```

The Flask application should now be running on `http://127.0.0.1:5000`.

### Makefile Commands

- `make install`: Sets up the virtual environment and installs the required dependencies.
- `make run`: Runs the Flask application.
- `make clean`: Cleans the virtual environment and removes cache files.
- `make setup`: Cleans the environment and installs dependencies.
- `make launch`: Sets up the environment and runs the Flask application.

## API Endpoints

- **GET /arr_status**: Retrieves arrival status data.
- **GET /dep_status**: Retrieves departure status data.
- **GET /tsat_status**: Retrieves TSAT status data.
- **GET /div_chart_test**: Retrieves real-time movement data.
- **GET /show_stations**: Retrieves real-time weather data.

## Environment Variables

Ensure the following environment variables are set in your environment or in a `.env` file:

- `URL_ARR_STATUS`: The URL to fetch arrival status data.
- `URL_DEP_STATUS`: The URL to fetch departure status data.
- `URL_TSAT_STATUS`: The URL to fetch TSAT status data.
- `URL_DIV_CHART_TEST`: The URL to fetch real-time movement data.
- `PHPSESSID`: PHP session ID for authentication.
- `HOST`: Host for the requests.
- `REFERER`: Referer URL for the requests.

## Example Usage

To fetch arrival status data manually:

```python
# arr_status.py
import os
from utils import get_status_data

def fetch_arrival_data():
    URL = os.getenv('URL_ARR_STATUS')
    table_ids = ['arr_estimated', 'arr_final', 'arr_landed']
    return get_status_data(URL, table_ids)

if __name__ == '__main__':
    print(fetch_arrival_data())
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

This project utilizes BeautifulSoup for HTML parsing and Flask for creating the backend API.
