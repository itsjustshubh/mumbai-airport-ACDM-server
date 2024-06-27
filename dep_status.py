# dep_status.py
"""
This module is designed to fetch departure status data from a specified URL. It uses predefined table identifiers
to extract and display departure data like boarding, pushback, and actual departure statuses.
"""

import os
from utils import get_status_data


def fetch_departure_data():
    """
    Fetches departure data using environment variables to determine the source URL and specific data tables.

    Environment Variables:
        URL_DEP_STATUS (str): The URL from which to fetch the departure data.

    Returns:
        dict: A dictionary containing structured departure data categorized by boarding, pushback, and departed statuses.
    """
    URL = os.getenv('URL_DEP_STATUS')
    table_ids = ['dep_boarding', 'dep_pushback', 'dep_departed']
    return get_status_data(URL, table_ids)


if __name__ == '__main__':
    print(fetch_departure_data())
