# div_chart_test.py
"""
This module provides functionalities to fetch and parse real-time chart data for movements at an airport from a web page.
It extracts JavaScript variables embedded in the HTML content of the page and converts them into structured JSON format.
"""

import os
import re
import json
import requests
from bs4 import BeautifulSoup
from utils import fetch_data, get_current_timestamp, get_headers
import pandas as pd


def extract_data_from_js(html_content):
    """
    Parses the HTML content to extract JavaScript data variables using regular expressions.

    Args:
        html_content (str): The HTML content from which data needs to be extracted.

    Returns:
        dict: A dictionary containing datasets as lists if extraction is successful, or error messages if not.
    """
    datasets = {}
    patterns = {
        'dataset1': r"var dataset1 = (\[.*?\]);",
        'dataset2': r"var dataset2 = (\[.*?\]);",
        'dataset3': r"var dataset3 = (\[.*?\]);"
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, html_content, re.DOTALL)
        if match:
            datasets[key] = json.loads(match.group(1))
        else:
            datasets[key] = f"No data found for {key}"
    return datasets


def get_div_chart_test_status(URL):
    """
    Fetches real-time movement data from a specified URL and extracts structured data from embedded JavaScript.

    Args:
        URL (str): The URL from which the HTML content is to be fetched.

    Returns:
        dict or str: A structured dictionary of extracted data if successful, or an error message if not.
    """
    HEADERS = get_headers()
    PARAMS = {'_': get_current_timestamp()}
    html_content = fetch_data(URL, HEADERS, PARAMS)
    if html_content:
        return extract_data_from_js(html_content)
    else:
        return {"error": "Failed to retrieve HTML content"}


if __name__ == '__main__':
    URL = os.getenv('URL_DIV_CHART_TEST',
                    'http://acdm.in/cdm/div_chart_test.php')
    data = get_div_chart_test_status(URL)
    if 'error' not in data:
        for key, value in data.items():
            print(f"\n{key.upper()} Data:")
            df = pd.DataFrame(value, columns=['Timestamp', 'Value'])
            df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
            print(df)
    else:
        print(data['error'])
