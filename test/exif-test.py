#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019-03-15

@author: laok
@copyright: Apache License, Version 2.0
'''
import sys
sys.path.append('../')
from pprint import pprint
from laok.image.exif import get_exif
#===============================================================================
# 
#===============================================================================

def exif_lktest():
    imgf = r'../resource/SolarPanel.jpg'
    info = get_exif(imgf)
    print("=" * 20)
    pprint(info)
    
def gps_lktest():
    imgf = r'../resource/SolarPanel.jpg'
    info = get_exif(imgf)
    
    latitude = info['GPSInfo']['GPSLatitudeValue']
    longitude = info['GPSInfo']['GPSLongitudeValue']
    altitude = info['GPSInfo']['GPSAltitudeValue']
    
    msg = "=" * 20 + "\n"
    msg += '纬度:%s 经度:%s 高度:%s' % (latitude,longitude,altitude)
    print(msg)
    
if __name__ == '__main__':
    exif_lktest()
    
    gps_lktest()
    