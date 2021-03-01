"""Project OC DAP 4 main file."""

from app.controllers.application import Application

""" flake8 --format=html --htmldir=flake-report --max-line-length=119 --exclude=.venv"""


def main():
    """Program entry point."""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
next
