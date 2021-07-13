import json


def test_json():
    data = json.load(open('./config/config.json'))
    a = data['params']['a']
    b = data['params']['b']
    print(a, b)


if __name__ == '__main__':
    test_json()
