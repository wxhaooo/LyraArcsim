import os
import sys
import json
import jstyleson as js

ARCSimPath = None

width = 20
height = 20

totalPointNumber = width * height 

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

dirBatchingConfPathPrefix = os.getcwd() + '/batching_conf/'

dirPathName = jsonConfigPath.split('/')[-1]
dirPathName = dirPathName[:dirPathName.rfind('.')]
dirBatchingConfPathPrefix += dirPathName
# dirBatchingConfPathPrefix += '/'

if(not os.path.exists(dirBatchingConfPathPrefix)):
    print('Folder {} is not existed! Create it!'.format(dirBatchingConfPathPrefix))
    os.makedirs(dirBatchingConfPathPrefix)

for i in range(0,totalPointNumber):
    jsonData['handles'][0]['nodes'] = i
    configFileName = dirBatchingConfPathPrefix + '/' + dirPathName + '_{:0>8d}.json'.format(i)
    with open(configFileName,'a') as f:
        js.dump(jsonData,f)