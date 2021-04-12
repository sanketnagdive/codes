import requests
result =requests.get("https://api.covid19india.org/v4/min/data.min.json")
print(result)
result.status_code
result.json()
print(result.json())
result['Active'] = result['confirmed'] - result['vaccinated'] - result['recovered']
result = result.groupby('state')['confirmed', 'vaccinated', 'recovered', 'tested'].sum().reset_index()
print(result) 


