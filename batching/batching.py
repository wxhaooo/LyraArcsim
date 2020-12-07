import os
import sys
import json
import jstyleson as js

ARCSimPath = None

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

jsonData['handles'][0]['nodes'] = 1

print(jsonData['handles'][0]['nodes'])