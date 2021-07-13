import yaml


def test_yaml():
    data = yaml.load(open('./config/config.yaml'), Loader=yaml.FullLoader)
    a = data['params']['a']
    b = data['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_yaml()
