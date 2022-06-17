#!/usr/bin/env python3
#Create API call to a public API to get domain or IP info

import requests

def get_data(domain):
    response = requests.get('https://api.threatminer.org/v2/domain.php?q=' + str(domain) + '&rt=1')
    apioutput = response.json()
#Print out raw data
    print(apioutput)

    print('--------- Filtered----------')
    filter_results = apioutput['results'][0]['whois']
    print(filter_results)

'''
    print('--------- First----------')
    first_result = filter_results[0]
    print(first_result)

    print('--------- Second----------')
    second_result = first_result['whois']
    print(second_result)
'''

result = get_data('amazon.com')