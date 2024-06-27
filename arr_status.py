# arr_status.py
"""
This module is designed to fetch arrival status data for an airport from a specified URL.
It utilizes environment variables to retrieve the data source URL and employs utility functions to parse and return the data.
"""

import os
from utils import get_status_data


def fetch_arrival_data():
    """
    Fetches arrival data from a specified environmental URL and extracts specific tables based on predefined identifiers.
    The function queries data for estimated arrivals, final arrivals, and landed statuses.

    Environment Variables:
        URL_ARR_STATUS (str): The URL from which to fetch the arrival data, set as an environment variable.

    Returns:
        dict: A dictionary containing structured arrival data categorized into estimated, final, and landed statuses.
              Each category will include the respective data as a list of dictionaries representing table rows.
    """
    URL = os.getenv('URL_ARR_STATUS')
    table_ids = ['arr_estimated', 'arr_final', 'arr_landed']
    return get_status_data(URL, table_ids)


if __name__ == '__main__':
    # Demonstrate fetching and printing arrival status data
    print(fetch_arrival_data())
