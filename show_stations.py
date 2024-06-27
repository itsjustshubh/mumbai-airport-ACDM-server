# show_stations.py
import os
from utils import fetch_data, get_headers, parse_atis_data
import json


def get_atis_data(URL):
    """
    Fetches and parses ATIS data from the web page.

    Returns:
        str: A JSON string of parsed ATIS data.
    """
    headers = get_headers()
    html_content = fetch_data(URL, headers, {})
    if html_content:
        return parse_atis_data(html_content)
    else:
        return json.dumps({'error': 'Failed to retrieve data'})


if __name__ == '__main__':
    # Fetch and print the ATIS data in JSON format
    atis_data_json = get_atis_data()
    print(atis_data_json)
