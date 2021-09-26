import os
import logging

cwd = os.getcwd()

from app.bot import Bot


def main() -> None:
    os.chdir(cwd)
    logging.getLogger(__name__).setLevel(logging.DEBUG)
    Bot().run()


if __name__ == '__main__':
    main()
