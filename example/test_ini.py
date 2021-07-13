import configparser


def test_ini():
    cf = configparser.ConfigParser()
    cf.read('./config/config.ini')
    a = cf['params']['a']
    b = cf['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_ini()
