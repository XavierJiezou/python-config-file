from example.test_ini import test_ini
from example.test_xml import test_xml
from example.test_json import test_json
from example.test_yaml import test_yaml
from example.test_py import test_py


def main():
    test_ini()
    test_xml()
    test_json()
    test_yaml()
    test_py()


if __name__ == '__main__':
    main()
