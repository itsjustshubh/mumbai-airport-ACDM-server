# create_env.py

from pathlib import Path

# Define the contents of the .env file
env_contents = """HOST=acdm.in
REFERER=http://acdm.in/cdm/acdm_mumbai.php
PHPSESSID={PHPSESSID}
URL_DEP_STATUS=http://acdm.in/cdm/dep_status.php
URL_ARR_STATUS=http://acdm.in/cdm/arr_status.php
URL_TSAT_STATUS=http://acdm.in/cdm/tsat_status_new.php
URL_DIV_CHART_TEST=http://acdm.in/cdm/div_chart_test.php
"""

# Prompt the user to enter the PHPSESSID
phpsessid = input("Please enter the PHPSESSID: ")

# Replace the placeholder with the actual PHPSESSID
env_contents = env_contents.format(PHPSESSID=phpsessid)

# Write the contents to the .env file
env_path = Path('.env')
env_path.write_text(env_contents)

print(".env file has been created successfully.")
