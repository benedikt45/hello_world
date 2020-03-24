import requests

gismeteoAPI = 'https://api.gismeteo.net/v2/weather/current/'
headers = {'X-Gismeteo-Token': '56b30cb255.3443075'}

def returnCityId(name):
    params = {'query': name}
    req = requests.get(gismeteoAPI, params=params, headers=headers)
    json_req = req.json()
    if 'meta' in json_req:
        if 'code' in json_req['meta']:
            return ['error', json_req['meta']['message']]
    return json_req['id']

def getWeather(cityName):
    cityID = returnCityId(cityName)
    if isinstance(cityID, list):
        print('Error '+cityID[1])
        raise SystemExit
    reqWeather = requests.get(gismeteoAPI+'/'+cityID,headers=headers)
    jsonWeather = reqWeather.json()

if __name__ == '__main__':
    getWeather('москв')