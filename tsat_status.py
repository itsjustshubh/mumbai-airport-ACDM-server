# tsat_status.py
import os
import json
from utils import fetch_data, get_current_timestamp, get_headers
from bs4 import BeautifulSoup


def get_tsat_status(URL):
    HEADERS = get_headers()
    PARAMS = {'_': get_current_timestamp()}

    # Fetch HTML content from the TSAT status URL
    html_content = fetch_data(URL, HEADERS, PARAMS)
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Adjusting to find the table directly since there's no div with an ID that wraps it
        table = soup.find('table', id='datatables')
        if not table:
            return json.dumps({"error": "Table not found in the HTML content"})

        headers = [th.get_text(strip=True)
                   for th in table.find('thead').find_all('th')]
        rows = []
        for tr in table.find('tbody').find_all('tr'):
            cells = [td.get_text(strip=True) for td in tr.find_all('td')]
            row_data = {headers[i]: cells[i] for i in range(len(cells))}
            rows.append(row_data)

        json_data = json.dumps(rows, indent=4)
        return json_data
    else:
        return json.dumps({"error": "Failed to retrieve TSAT data"})


if __name__ == '__main__':
    # Print out the TSAT data in JSON format
    print(get_tsat_status())
