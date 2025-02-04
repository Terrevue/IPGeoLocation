#!/usr/bin/env python3
# encoding: UTF-8

"""
    This file is part of IPGeoLocation tool.
    Copyright (C) 2015-2016 @maldevel
    https://github.com/maldevel/IPGeoLocation
    
    IPGeoLocation - Retrieve IP Geolocation information 
    Powered by http://ip-api.com
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    For more see the file 'LICENSE' for copying permission.
"""

__author__ = 'maldevel'

import traceback
import sys

import csv
from xml.etree import ElementTree as etree
from collections import OrderedDict

class FileExporter:
    
    def __init__(self):
        pass
    
    def ExportListToCSV(self, ipGeoLocObjs, filename):
        return self.__ExportToCSV(ipGeoLocObjs, filename)
        
    def ExportToCSV(self, ipGeoLocObj, filename):
        return self.__ExportToCSV([ipGeoLocObj], filename)
    
    def ExportListToXML(self, ipGeoLocObjs, filename):
        return self.__ExportToXML(ipGeoLocObjs, filename)
    
    def ExportToXML(self, ipGeoLocObj, filename):
        return self.__ExportToXML([ipGeoLocObj], filename)

    def ExportListToTXT(self, ipGeoLocObjs, filename):
        return self.__ExportToTXT(ipGeoLocObjs, filename)
        
    def ExportToTXT(self, ipGeoLocObj, filename):
        return self.__ExportToTXT([ipGeoLocObj], filename)
    
    def __ExportToTXT(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w') as txtfile:
                txtfile.write('Results IPGeolocation\n')
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        txtfile.write('Target: {}\n'.format(ipGeoLocObj.Query))
                        txtfile.write('IP: {}\n'.format(ipGeoLocObj.IP))
                        txtfile.write('ASN: {}\n'.format(ipGeoLocObj.ASN))
                        txtfile.write('City: {}\n'.format(ipGeoLocObj.City))
                        txtfile.write('Country: {}\n'.format(ipGeoLocObj.Country))
                        txtfile.write('Country Code: {}\n'.format(ipGeoLocObj.CountryCode))
                        txtfile.write('ISP: {}\n'.format(ipGeoLocObj.ISP))
                        txtfile.write('Latitude: {}\n'.format(ipGeoLocObj.Latitude))
                        txtfile.write('Longtitude: {}\n'.format(ipGeoLocObj.Longtitude))
                        txtfile.write('Organization: {}\n'.format(ipGeoLocObj.Organization))
                        txtfile.write('Region: {}\n'.format(ipGeoLocObj.Region))
                        txtfile.write('Region Name: {}\n'.format(ipGeoLocObj.RegionName))
                        txtfile.write('Timezone: {}\n'.format(ipGeoLocObj.Timezone))
                        txtfile.write('Zip: {}\n'.format(ipGeoLocObj.Zip))
                        txtfile.write('Google Maps: {}\n'.format(ipGeoLocObj.GoogleMapsLink))
                        txtfile.write('\n')
            return True
        except:
            return False
        
        
    def __ExportToXML(self, ipGeoLocObjs, filename):
        try:
            root = etree.Element('Results')
            
            for ipGeoLocObj in ipGeoLocObjs:
                if ipGeoLocObj:
                    orderedData = OrderedDict(sorted(ipGeoLocObj.ToDict().items()))
                    self.__add_items(etree.SubElement(root, 'IPGeolocation'),
                      ((key.replace(' ', ''), value) for key, value in orderedData.items()))
        
                    tree = etree.ElementTree(root)

            tree.write(filename, xml_declaration=True, encoding='utf-8')
                        
            return True
        except:
            return False
               
    def __ExportToCSV(self, ipGeoLocObjs, filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                fieldnames = ['Query','IP','ASN','City','Country','CountryCode','ISP','Latitude','Longtitude','Organization','Region','RegionName','Timezone','Zip','GoogleMapsLink']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                writer.writeheader()
                
                #writer.writerows(ipGeoLocObjs)
                for ipGeoLocObj in ipGeoLocObjs:
                    if ipGeoLocObj:
                        
                        ipGeoLocObj.ToDictMatch()
                        
                        writer.writerow({
                            'Query': ipGeoLocObj.Query,
                            'IP': ipGeoLocObj.IP,
                            'ASN': ipGeoLocObj.ASN,
                            'City': ipGeoLocObj.City,
                            'Country': ipGeoLocObj.Country,
                            'CountryCode': ipGeoLocObj.CountryCode,
                            'ISP': ipGeoLocObj.ISP,
                            'Latitude': ipGeoLocObj.Latitude,
                            'Longtitude': ipGeoLocObj.Longtitude,
                            'Organization': ipGeoLocObj.Organization,
                            'Region': ipGeoLocObj.Region,
                            'RegionName': ipGeoLocObj.RegionName,
                            'Timezone': ipGeoLocObj.Timezone,
                            'Zip': ipGeoLocObj.Zip,
                            'GoogleMapsLink': ipGeoLocObj.GoogleMapsLink
                        })
            return True
        except:
            print(sys.exc_info()[2])
            print(traceback.format_exc())
            return False
    
    def __add_items(self, root, items):
        for name, text in items:
            elem = etree.SubElement(root, name)
            elem.text = text

