# app.py
"""
This Flask application provides several RESTful API endpoints to access real-time data for airport operations,
including arrival status, departure status, TSAT status, and minute-by-minute movement data.
Each endpoint fetches data from specific URLs configured via environment variables and returns JSON-formatted responses.
"""

import os
from flask import Flask, jsonify
from utils import get_status_data
from tsat_status import get_tsat_status
from div_chart_test import get_div_chart_test_status
# Assuming this function exists and is configured to fetch ATIS data
from show_stations import get_atis_data


app = Flask(__name__)


@app.route('/arr_status')
def arr_status():
    """
    API endpoint to retrieve arrival status data from the configured URL.
    Retrieves data such as estimated arrival, final arrival, and landed status.

    Returns:
        json: A JSON object containing structured data for estimated arrivals, final arrivals, and landed statuses.
    """
    URL = os.getenv('URL_ARR_STATUS')
    table_ids = ['arr_estimated', 'arr_final', 'arr_landed']
    data = get_status_data(URL, table_ids)
    return jsonify(data)


@app.route('/dep_status')
def dep_status():
    """
    API endpoint to retrieve departure status data from the configured URL.
    Retrieves data such as boarding status, pushback, and actual departure status.

    Returns:
        json: A JSON object containing structured data for boarding, pushback, and departed statuses.
    """
    URL = os.getenv('URL_DEP_STATUS')
    table_ids = ['dep_boarding', 'dep_pushback', 'dep_departed']
    data = get_status_data(URL, table_ids)
    return jsonify(data)


@app.route('/tsat_status')
def tsat_status():
    """
    API endpoint to retrieve TSAT (Target Start-up Approval Time) status data.
    TSAT data includes scheduled times for aircraft pushback and gate departure.

    Returns:
        json: A JSON object containing TSAT status data, providing detailed timings for aircraft operations.
    """
    URL = os.getenv('URL_TSAT_STATUS')
    data = get_tsat_status(URL)
    return jsonify(data)


@app.route('/div_chart_test')
def div_chart_test():
    """
    API endpoint to retrieve real-time movement data based on minute-by-minute charts from the configured URL.
    This includes movement data for departures and arrivals at the airport.

    Returns:
        json: A JSON object containing minute-by-minute real-time movement data visualized through charts.
    """
    URL = os.getenv('URL_DIV_CHART_TEST')
    data = get_div_chart_test_status(URL)
    return jsonify(data)

@app.route('/show_stations')
def show_stations():
    """
    API endpoint to retrieve ATIS data for stations from the configured URL.
    This data includes detailed ATIS messages for specific stations like VABB.
    """
    URL = 'http://acdm.in/cdm/ShowStations.php?q=VABB'
    data = get_atis_data(URL)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
