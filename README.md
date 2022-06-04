# sra_py
A python wrapper for [some-random-api](https://some-random-api.ml)

## Requirements
[Python 3.8.6 or more](https://python.org)  

## Installation
```cmd
pip install git+https://github.com/Atidipt123/sra_py.git
```

## Examples
```py
from sra_py import Client

# cat image
client = Client()

x = client.animal.get_image('cat')
print(x.image_url)
x.save('cat.png')
```

```py
# pixelate image
from sra_py import Client
import os

client = Client()
client.canvas.pixelate('IMAGE URL').save('pixelated.png')
os.startfile('pixelated.png')
```

## Links
[Documentation](https://sra_py.rtfd.io)  
[Some Random API](https://some-random-api.ml)  
[PyPI](https://pypi.org/project/sra_py)