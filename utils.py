# utils.py
"""
A utility module for fetching and parsing web data. This module contains functions to interact with web APIs,
extract data from HTML content, and manage time-based operations. It also configures HTTP headers for requests
based on environment variables.
"""

import json
import os
import time
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file


def fetch_data(url, headers, params):
    """
    Sends a GET request to the specified URL with given headers and query parameters.

    Args:
        url (str): The URL to which the GET request is made.
        headers (dict): Headers to be sent with the GET request.
        params (dict): Query parameters to be appended to the URL.

    Returns:
        str: The response content as text if the request was successful; otherwise, None.
    """
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raises an error for bad responses
        return response.text
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


def extract_table_data(html_content, table_id):
    """
    Parses HTML content to extract data from a table identified by its ID.

    Args:
        html_content (str): The HTML content containing the table.
        table_id (str): The ID of the table to extract data from.

    Returns:
        list of dict: A list of dictionaries, each representing a row in the table with column headers as keys.
    """
    soup = BeautifulSoup(html_content, 'lxml')
    table = soup.find('div', id=table_id).find('table')
    headers = [th.get_text(strip=True)
               for th in table.find('thead').find_all('th')]
    rows = []
    for tr in table.find('tbody').find_all('tr'):
        cells = [td.get_text(strip=True) for td in tr.find_all('td')]
        row_data = {headers[i]: cells[i] for i in range(len(cells))}
        rows.append(row_data)
    return rows


def get_current_timestamp():
    """
    Retrieves the current time as a UNIX timestamp in milliseconds.

    Returns:
        int: The current time in milliseconds.
    """
    return int(time.time() * 1000)


def get_headers():
    """
    Constructs HTTP headers for requests, utilizing environment variables for certain values.

    Returns:
        dict: A dictionary of HTTP headers.
    """
    return {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': f"PHPSESSID={os.getenv('PHPSESSID')}",
        'DNT': '1',
        'Host': os.getenv('HOST'),
        'Referer': os.getenv('REFERER'),
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }


def get_status_data(url, table_ids):
    """
    Fetches and parses structured data from a specified URL based on table identifiers.

    Args:
        url (str): The URL from which to fetch data.
        table_ids (list of str): A list of table identifiers to extract data for.

    Returns:
        str: A JSON string containing parsed table data or an error message if data retrieval fails.
    """
    params = {'_': get_current_timestamp()}
    headers = get_headers()
    html_content = fetch_data(url, headers, params)
    if html_content:
        all_data = {table_id: extract_table_data(
            html_content, table_id) for table_id in table_ids}
        return json.dumps(all_data, indent=4)
    else:
        return json.dumps({'error': 'Failed to retrieve data'})
