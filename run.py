import logging
import os

cwd = os.getcwd()

from app.bot import Bot


def main() -> None:
    os.chdir(cwd)
    logging.basicConfig(level=logging.DEBUG)
    Bot().run()


if __name__ == '__main__':
    main()
