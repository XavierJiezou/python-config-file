import sys
sys.path.append('./')
from config.config import params


def test_py():
    a = params['a']
    b = params['b']
    print(a, b)


if __name__ == '__main__':
    test_py()
