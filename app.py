import os
import sys
from views.interface import festivalis

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)  # pyright: ignore


def main():
    festivalis()


if __name__ == "__main__":
    main()
