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
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- OBJECT PERMISSIONS -->\n')
        for elem in rootOfXML.iter('objectPermissions'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- RECORDTYPE VISIBILITIES -->\n')
        for elem in rootOfXML.iter('recordTypeVisibilities'):
            i = len(elem)
            count = 0

            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- LAYOUT ASSIGNMENTS -->\n')
        for elem in rootOfXML.iter('layoutAssignments'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- FIELD PERMISSIONS -->\n')
        for elem in rootOfXML.iter('fieldPermissions'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- TAB VISIBILITIES -->\n')
        for elem in rootOfXML.iter('tabVisibilities'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('<!-- APPLICATION VISIBILITIES -->\n')
        for elem in rootOfXML.iter('applicationVisibilities'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- CLASS ACCESSES -->\n')
        for elem in rootOfXML.iter('classAccesses'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- PAGE ACCESSES -->\n')
        for elem in rootOfXML.iter('pageAccesses'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- CUSTOM METADATA TYPES ACCESSES -->\n')
        for elem in rootOfXML.iter('customMetadataTypeAccesses'):
            i = len(elem)
            count = 0
            
            XMLtoBuild += str('<'+elem.tag+'>')
            while count < i:
                XMLtoBuild += str('<'+elem[count].tag+'>'+elem[count].text+'</'+elem[count].tag+'>')
                count += 1
            XMLtoBuild += str('</'+elem.tag+'>\n')
            print('\n')

        XMLtoBuild += str('\n<!-- CUSTOM PERMISSIONS -->\n')
        XMLtoBuild += '''\n</Profile>'''

        myfile = open('output/%s' %filename, "w")
        myfile.write(XMLtoBuild)

        print("Done\n")

print("All done now. Ivo will take care of the rest...")