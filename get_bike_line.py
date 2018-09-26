#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 00:24:28 2018

@author: caiboqin
"""

import requests
import json

start_x=116.334307
start_y=39.90909
end_x=116.437307
end_y=39.924901

key="你的key"

url="https://restapi.amap.com/v4/direction/bicycling?origin={0},{1}&destination={2},{3}&key={4}".format(start_x,start_y,end_x,end_y,key)
data=requests.get(url).text

#返回距离
def get_distance(data):
    distance=json.loads(data)['data']['paths'][0]['distance']
    return distance

# 返回经过的路名
def get_roads(data):
    return [i['road'] for i in json.loads(data)['data']['paths'][0]['steps']]

# 返回经过的路径
def get_polyline(data):
    polyline=[i['polyline'][i['polyline'].index(';')+1:] if index!=0 else i['polyline'] for index,i in enumerate(json.loads(data)['data']['paths'][0]['steps'])]
    polyline=';'.join(polyline)
    polyline=[(float(i.split(',')[0]),float(i.split(',')[1])) for i in polyline.split(';')]
    return polyline

print(get_distance(data))
print(get_polyline(data))
print(get_roads(data))
