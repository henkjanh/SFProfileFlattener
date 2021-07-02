#!/usr/bin/env python3

#------------------------------------------------------------------------------------------------------
# This script takes Salesforce Profile XML files and flattens it so that it's easier to read
# @author: Henkjan Havenaar (henkjan@havenaar.nl)
#| @created: July 2021
#| @github: https://github.com/henkjanh
#------------------------------------------------------------------------------------------------------

import os, glob
import xml.etree.ElementTree as ET

def stripNs(el):
  '''Recursively search this element tree, removing namespaces.'''
  if el.tag.startswith("{"):
    el.tag = el.tag.split('}', 1)[1]  # strip namespace
  for k in el.attrib.keys():
    if k.startswith("{"):
      k2 = k.split('}', 1)[1]
      el.attrib[k2] = el.attrib[k]
      del el.attrib[k]
  for child in el:
    stripNs(child)

print("\n*********************************************")
print("*                                             *")
print("*           SF Profile Flattener              *")
print("*                                             *")
print("***********************************************\n\n")

output_subdir = "output"

try:
    print("Creating output directory...")
    os.mkdir(output_subdir)
except Exception:
    print("Output directory already exists...\n")
    pass

filenames = glob.glob("*.profile")

for file in filenames:
    with open(file, 'r', encoding="utf-8") as content:
        filename = os.path.basename(file)

        print("Working on file: %s" %filename)

        XML = ET.parse(content)
        rootOfXML = XML.getroot()

        stripNs(rootOfXML)

        XMLtoBuild = '''<?xml version="1.0" encoding="UTF-8"?>
        <Profile xmlns="http://soap.sforce.com/2006/04/metadata">\n'''

        XMLtoBuild += str('\n<!-- GENERAL INFORMATION -->\n')

        XMLtoBuild += str('\n<!-- USER PERMISSIONS -->\n')
        for elem in rootOfXML.iter('userPermissions'):   
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')        

        XMLtoBuild += str('\n<!-- OBJECT PERMISSIONS -->\n')
        for elem in rootOfXML.iter('objectPermissions'):
            # i = len(elem)
            # print(i)
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'<'+elem[2].tag+'>'+elem[2].text+'</'+elem[2].tag+'>'+'<'+elem[3].tag+'>'+elem[3].text+'</'+elem[3].tag+'>'+'<'+elem[4].tag+'>'+elem[4].text+'</'+elem[4].tag+'>'+'<'+elem[5].tag+'>'+elem[5].text+'</'+elem[5].tag+'>'+'<'+elem[6].tag+'>'+elem[6].text+'</'+elem[6].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- RECORDTYPE VISIBILITIES -->\n')
        for elem in rootOfXML.iter('recordTypeVisibilities'):
            if len(elem) == 3:
                XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'<'+elem[2].tag+'>'+elem[2].text+'</'+elem[2].tag+'>'+'</'+elem.tag+'>''\n')
            elif len(elem) == 4:
                XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'<'+elem[2].tag+'>'+elem[2].text+'</'+elem[2].tag+'>'+'<'+elem[3].tag+'>'+elem[3].text+'</'+elem[3].tag+'>'+'</'+elem.tag+'>''\n')
        
        XMLtoBuild += str('\n<!-- LAYOUT ASSIGNMENTS -->\n')
        for elem in rootOfXML.iter('layoutAssignments'):
            # i = len(elem)
            # print(i)
            if len(elem) == 1:
                XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'</'+elem.tag+'>''\n')
            elif len(elem) == 2:
                XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- FIELD PERMISSIONS -->\n')
        for elem in rootOfXML.iter('fieldPermissions'):
            # i = len(elem)
            # print(i)
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'<'+elem[2].tag+'>'+elem[2].text+'</'+elem[2].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- TAB VISIBILITIES -->\n')
        for elem in rootOfXML.iter('tabVisibilities'):
            # i = len(elem)
            # print(i)
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('<!-- APPLICATION VISIBILITIES -->\n')
        for elem in rootOfXML.iter('applicationVisibilities'):
            # i = len(elem)
            # print(i)

            # elemCounter = 0
            # while i != 0:
            #     print('hoi')
            #     i -= 1
            #     elemCounter + 1
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'<'+elem[2].tag+'>'+elem[2].text+'</'+elem[2].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- CLASS ACCESSES -->\n')
        for elem in rootOfXML.iter('classAccesses'):
            # i = len(elem)
            # print(i)
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- PAGE ACCESSES -->\n')
        for elem in rootOfXML.iter('pageAccesses'):
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- CUSTOM METADATA TYPES ACCESSES -->\n')
        for elem in rootOfXML.iter('customMetadataTypeAccesses'):
            XMLtoBuild += str('<'+elem.tag+'>'+'<'+elem[0].tag+'>'+elem[0].text+'</'+elem[0].tag+'>'+'<'+elem[1].tag+'>'+elem[1].text+'</'+elem[1].tag+'>'+'</'+elem.tag+'>''\n')

        XMLtoBuild += str('\n<!-- CUSTOM PERMISSIONS -->\n')
        XMLtoBuild += '''\n</Profile>'''

        myfile = open('output/%s' %filename, "w")
        myfile.write(XMLtoBuild)

        print("Done\n")

print("All done now. Ivo will take care of the rest...")