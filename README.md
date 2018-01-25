# pydelivengo
pydelivengo is a Python library using the MyDelivengo API


## MyDelivengo API documentation

http://www.assistance-mydelivengo.fr/api/

You can find the list of parameters for each function into this
documentation.


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
