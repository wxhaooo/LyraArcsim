import os
import sys
import json
import jstyleson as js

ARCSimPath = None

width = 20

OS = sys.platform

if OS == 'win32':
    ARCSimPath = '../build/Release/Arcsim.exe'
elif OS == 'linux':
    ARCSimPath = '../build/Arcsim'

jsonConfigPath = '../conf/uniform_grid_drop.json'

jsonData = None

with open(jsonConfigPath,'r') as f:
    jsonDataWithoutComment = ''.join(line for line in f if not line.startswith('//'))
    jsonData = js.loads(jsonDataWithoutComment)

for i in range(0,width + 1):
    jsonData['handles'][0]['nodes'] = i
    configFileName = 
    js.dumps(jsonData)
    # print(jsonData['handles'][0]['nodes'])