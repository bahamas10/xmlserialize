#!/usr/bin/env python
#
# Copyright (c) 2012, Dave Eddy <dave@daveeddy.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the project nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
XMLDict.py

Convert a Python dictionary to XML
"""

from xml.dom.minidom import parse, parseString

# Convenience Functions
def convert_dict_to_xml(d):
    """Convenience Function: This creates an XMLDict object, and returns the XML string"""
    return XMLDict(d).get_xml()

def prettify(xml):
    """Convenience Function: This returns a pretty version of the XML"""
    return parseString(xml).toprettyxml()

class XMLDict:
    """Class used to convert a python dictionary to XML"""
    def __init__(self, d):
        """Create the XML and store it"""
        self.d = d
        self.xml = self._convert_dict_to_xml(self.d)

    def get_xml(self):
        """Returns the XML"""
        return self.xml

    def get_pretty_xml(self):
        """Returns the pretty XML"""
        return parseString(self.xml).toprettyxml()

    def _convert_dict_to_xml(self, d):
        """Converts a dictionary to XML"""
        xml = ''
        for k,v in d.iteritems(): # iterate through the dictionary
            if isinstance(v, dict): # the value is a dictionary
                xml += "<%s>" % (k)
                xml += self._convert_dict_to_xml(v) # recursive :)
                xml += "</%s>" % (k)
            else: # value is not a dictionary
                if not isinstance(v, list):
                    v = [v]
                for value in v:
                    if isinstance(value, dict):
                        xml += "<%s>" % (k)
                        xml += self._convert_dict_to_xml(value) # recursively call itself
                        xml += "</%s>" % (k)
                    else:
                        xml += "<%s>%s</%s>" % (str(k), str(value), str(k))
        return xml

if __name__ == '__main__':
    import sys

    obj = { "people" : { "person" : [ "dave", "john", "steve", "mike", "jack" ] } }

    xml_dict = XMLDict(obj)

    print xml_dict.get_pretty_xml()
