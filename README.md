# pydelivengo 
[![Build Status](https://travis-ci.org/alexandriagroup/pydelivengo.svg?branch=master)](https://travis-ci.org/alexandriagroup/pydelivengo)

pydelivengo is a Python library using the MyDelivengo API


## Documentation

PyDelivengo : https://alexandriagroup.github.io/pydelivengo/

MyDelivengo (La Poste API documentation) : http://www.assistance-mydelivengo.fr/api/

You can find the list of parameters for each function into this
documentation.

## How to use

```python
api = PyDelivengo(api_authorization="your_mydelivengo_api_key")
api.get_user_info()  # Get your user info
api..get_envois()  # get all your "envois"
api.get_pli(11437479, print_pdf=True)  # Get the "pli" with ID 11437479 and generate PDF to print
api.get_depots(params={'date[from]':'30/11/2017'})  # Get the "depots" from November 30th
```


Looks to [MyDelivengo](http://www.assistance-mydelivengo.fr/api/documentation/) documentation to see all parameters.

## Tools

### Decode and save PDF from API

An example for decode and save the Base64 Encoded String return by the
MyDelivengo API:

```python
import os
from base64 import decodebytes

with open(os.path.expanduser('path/test.pdf'), 'wb') as f:
    f.write(decodebytes(api_data.encode('ascii')))
```
