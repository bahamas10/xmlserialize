xmlserialize
============

XML Serializer for python.  Convert a python dictionary into XML.


Usage
=====

#### Obect-Oriented Approach

``` python
>>> import XMLDict
>>> obj =  { "people" : { "person" : [ "dave", "john", "steve", "mike", "jack" ] } }
>>> xml_dict = XMLDict.XMLDict(obj)
>>> print xml_dict.get_xml()
<people><person>dave</person><person>john</person><person>steve</person><person>mike</person><person>jack</person></people>
>>> print xml_dict.get_pretty_xml()
<?xml version="1.0" ?>
<people>
    <person>
        dave
    </person>
    <person>
        john
    </person>
    <person>
        steve
    </person>
    <person>
        mike
    </person>
    <person>
        jack
    </person>
</people>
>>>
```

#### Convenience Methods

``` python
>>> import XMLDict
>>> obj =  { "people" : { "person" : [ "dave", "john", "steve", "mike", "jack" ] } }
>>> print XMLDict.convert_dict_to_xml(obj)
<people><person>dave</person><person>john</person><person>steve</person><person>mike</person><person>jack</person></people>
>>> print XMLDict.prettify(XMLDict.convert_dict_to_xml(obj))
<?xml version="1.0" ?>
<people>
    <person>
        dave
    </person>
    <person>
        john
    </person>
    <person>
        steve
    </person>
    <person>
        mike
    </person>
    <person>
        jack
    </person>
</people>
>>>
```


Command Line
============

    dave @ [ bahamas10 :: (SunOS) ] ~/dev/xmlserialize $ ./XMLDict.py
    <?xml version="1.0" ?>
    <people>
    	<person>
    		dave
    	</person>
    	<person>
    		john
    	</person>
    	<person>
    		steve
    	</person>
    	<person>
    		mike
    	</person>
    	<person>
    		jack
    	</person>
    </people>

Copying
=======

Released under the BSD 3-clause license, see LICENSE for details.
