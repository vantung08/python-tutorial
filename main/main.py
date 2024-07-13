import logging
from greeting import greeting


logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def main():
    return greeting()

if __name__ == '__main__':
    print(main())

