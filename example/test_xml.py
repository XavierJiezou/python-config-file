import xml.etree.ElementTree as ET


def test_xml():
    tree = ET.parse('./config/config.xml')
    root = tree.getroot()
    a = root[0].text
    b = root[1].text
    print(a, b)


if __name__ == '__main__':
    test_xml()
