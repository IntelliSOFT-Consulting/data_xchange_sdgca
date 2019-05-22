"""
Fetch org units from one dhis2 instance to another
July 7th, 2018
Python 3.6.5
"""
import argparse

import requests


USERNAME = 'admin'
PASSWORD = 'K3lvin123!'
AUTH = requests.auth.HTTPBasicAuth(USERNAME, PASSWORD)
FILE_NAME = 'SDGA2063DataEthiopia.csv'
FETCHURL="https://test.ethiopia.intellisoftkenya.com/dhis/api/29/dataValueSets.csv?dataSet=" 
PERIOD = "2015"
SDGDATASETUID="Zr3CUESFpaV"
A2063DATASETUID="NIpCsdrXF5T"
ORGUNIT = 'dG3dUrdW1Yi'

def fetch_data():
    url=FETCHURL+SDGDATASETUID+"&dataSet="+A2063DATASETUID+"&period="+PERIOD+"&orgUnit="+ORGUNIT
    request = requests.get(
            url,
            auth=AUTH
        )
    open(FILE_NAME, 'wb').write(request.content)
    return 1

if __name__ == '__main__':
    data_instance = fetch_data()
    print(data_instance)
    # list_data = create_array(data_instance)
