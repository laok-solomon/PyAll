#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2019-03-15

@author: laok
@copyright: Apache License, Version 2.0
'''
from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
#===============================================================================
# 
#===============================================================================
__all__ = ["sphere_to_decimal",
           "get_exif"
           ]

def sphere_to_decimal(degrees, minutes, seconds):
    '''将 (度,分,秒)经纬度转换为小数
    '''
    return degrees + minutes/60.0 + seconds/3600.0

def _get_exif(im):
    '''提取 exif信息
    '''
    data = {}
    
    if not hasattr(im, '_getexif'):
        return data
    
    exifinfo = im._getexif()    #获取 exif信息
    
    if not exifinfo:    #判空
        return data
    
    #遍历
    for tag, value in exifinfo.items():
        tag = TAGS.get(tag, tag)
        
        if tag == 'GPSInfo':#遍历 gps信息,进行 特殊处理
        
            gps = {}
            for _t, _v in value.items():
                
                _t = GPSTAGS.get(_t, _t)
                
                if _t in ["GPSLatitude", "GPSLongitude"]: #转换 经纬度
                    _dvalue = sphere_to_decimal(_v[0][0]*1.0/_v[0][1], _v[1][0]*1.0/_v[1][1], _v[2][0]*1.0/_v[2][1])
                    gps[_t+"Value"] = _dvalue
                    
                elif _t == 'GPSAltitude': #转换高度
                    gps[_t+"Value"] = _v[0]*1.0/_v[1]
                
                gps[_t] = _v      
            
            data[tag] = gps
        
        elif tag == 'XMLPacket': #XMLPacket数据
            data[tag] = value.decode('utf8')
        else:
            data[tag] = value
    return data


def get_exif(img):
    '''提取 exif信息
        img 图片路径 或者 PIL图像对象
        ret: 返回exif数据字典,或者 空字典
    '''
    if isinstance(img, str):
        with Image.open(img) as im:
            return _get_exif(im)
    else:
        return _get_exif(img)

if __name__ == '__main__':
    imgf = r'C:\workspace\data\SolarPanel\test.jpg'
    info = get_exif(imgf)
    from pprint import pprint
    pprint(info)
    

