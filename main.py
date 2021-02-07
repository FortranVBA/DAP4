"""Project OC DAP 4 main file."""

from app.controllers.application import Application

# from app.models.tournament import Tournament


def main():
    """Program entry point."""
    # Tournament.get_next_turn()
    app = Application()
    app.run()


if __name__ == "__main__":
    main()
next
