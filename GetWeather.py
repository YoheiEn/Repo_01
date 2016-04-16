# -*- coding: utf-8 -*-
#2016/03/13
#App for getting weather forecast at Oasaka

import requests
import json
    
location = 270000 #大阪
print("大阪の天気")
proxies = None

weather_json = requests.get("http://weather.livedoor.com/forecast/webservice/json/v1?city={0}" \
                .format(location),proxies = proxies, timeout = 5).json()

#print(json.dumps(weather_json, indent = 2, ensure_ascii=False))

for forecast in weather_json["forecasts"]:
    #最低気温
    if forecast["temperature"]["min"] != None:
        min = forecast["temperature"]["min"]["celsius"]
    else:
        min = "--"
    #最高気温
    if forecast["temperature"]["max"] != None:
        max = forecast["temperature"]["max"]["celsius"]
    else:
        max = "--"
    #日付、天気、最低気温／最高気温
    str_forecast = forecast["dateLabel"] + ", " + forecast["telop"] \
                    + ", " + min + "/" + max
    print(str_forecast)

else:
    print("done")


