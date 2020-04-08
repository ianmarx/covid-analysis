import requests as r

baseUrl = 'https://covidtracking.com/api/v1/'

def pullData(endpoint, filename):
    url = baseUrl + endpoint
    data = r.get(url)

    with open('data/{}'.format(filename), 'w') as f:
        f.write(data.text)

pullData('states/current.json', 'states.json')
pullData('states/daily.json', 'statesDaily.json')
