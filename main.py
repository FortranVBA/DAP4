"""Project OC DAP 4 main file."""

from app.controllers.application import Application


def main():
    """Program entry point."""
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
next
