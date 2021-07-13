# Introduction
A summary of the usage of all python's configuration files that include `INI`, `XML`, `JSON`, `YAML`, and `PY`, 

# Usage
## INI
[config/config.ini](config/config.ini)
```ini
[params]
a=1
b=2
```
[example/test_ini.py](example/test_ini.py)
```python
import configparser


def test_ini():
    cf = configparser.ConfigParser()
    cf.read('./config/config.ini')
    a = cf['params']['a']
    b = cf['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_ini()
```
## XML
[config/config.xml](config/config.xml)
```xml
<?xml version="1.0"?>
<params>
    <a>1</a>
    <b>2</b>
</params>
```
[example/test_xml.py](example/test_xml.py)
```python
import xml.etree.ElementTree as ET


def test_xml():
    tree = ET.parse('./config/config.xml')
    root = tree.getroot()
    a = root[0].text
    b = root[1].text
    print(a, b)


if __name__ == '__main__':
    test_xml()
```
## JSON
[config/config.json](config/config.json)
```json
{
    "params": {
        "a": 1,
        "b": 2
    }
}
```
[example/test_json.py](example/test_json.py)
```python
import json


def test_json():
    data = json.load(open('./config/config.json'))
    a = data['params']['a']
    b = data['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_json()
```
## YAML👍
[config/config.yaml](config/config.yaml)
```yaml
params:
  a: 1
  b: 2
```
[example/test_yaml.py](example/test_yaml.py)
```python
import yaml


def test_yaml():
    data = yaml.load(open('./config/config.yaml'), Loader=yaml.FullLoader)
    a = data['params']['a']
    b = data['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_yaml()
```
## PY👍
[config/config.py](config/config.py)
```python
params = {
    'a': 1,
    'b': 2
}
```
[example/test_py.py](example/test_py.py)
```python
import sys
sys.path.append('./')
from config.config import params


def test_py():
    a = params['a']
    b = params['b']
    print(a, b)


if __name__ == '__main__':
    test_py()
```

# Reference
> [https://zh.wikipedia.org/wiki/INI文件](https://zh.wikipedia.org/wiki/INI文件)
> 
> [https://zh.wikipedia.org/wiki/XML](https://zh.wikipedia.org/wiki/XML)
> 
> [https://zh.wikipedia.org/wiki/JSON](https://zh.wikipedia.org/wiki/JSON)
> 
> [https://zh.wikipedia.org/wiki/YAML](https://zh.wikipedia.org/wiki/YAML)