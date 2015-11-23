# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/andrew/.spyder2/.temp.py
"""
import logging
from lxml import etree

logger = logging.getLogger(__name__)

def validate_xml(xmlschemafile, xmlfilename):

    with open(xmlschemafile, 'r') as f:
        schema_root = etree.XML(f.read())

    schema = etree.XMLSchema(schema_root)
    
    xmlparser = etree.XMLParser(schema=schema)

    try:
        with open(xmlfilename, 'r') as f:
            etree.fromstring(f.read(), xmlparser)
        return True
        
#    except etree.XMLSyntaxError:
#        logger.warning('%s returned XMLSyntaxError.' % (xmlfilename))
#        return False
    except etree.XMLSchemaError:
        logger.warning('%s returned XMLSchemaError.' % (xmlfilename))
        return false


if __name__ == '__main__':
    print '##########################################'
    xmlschema = 'B2MML-V0401-Material.xsd'
    filenames = ['example.xml']
    for filename in filenames:
        if validate_xml(xmlschema, filename):
            print "File: %s validates." % filename
            
            with open(filename, 'r') as fin:
                print fin.read()
        else:
            print "File: %s does not validate." % filename
            
    with open(xmlschema, 'r') as f:
        schema_root = etree.XML(f.read())
        
        
        