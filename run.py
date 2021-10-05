import logging

from app.bot import Bot


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)
    Bot().run()


if __name__ == '__main__':
    main()
