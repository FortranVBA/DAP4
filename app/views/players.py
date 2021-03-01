"""Project OC DAP 4 file with the players viewer."""

from app.models.player import Player

from app.config import CommandField


class PlayersViewer:
    """Project players viewer class."""

    def __init__(self):
        """Init players viewer class."""
        self.warning = ""

    def display(self):
        """Display the view and the command list."""
        self.display_warning()

        print("The list of players is the following :")
        if not (
            self.warning == "players alphabetical" or self.warning == "players ranking"
        ):
            for player in Player.get_all.values():
                print(f" - {player.name} {player.surname}")
        print(" ")
        print("Command list :")
        number = 1
        for player in Player.get_all.values():
            print(
                f" - {number}{CommandField.EDIT_PLAYER} "
                + f"to edit {player.name} {player.surname}"
            )
            number += 1
        print(" - " + CommandField.SAVE_PLAYERS + " to save players to database")
        print(" - " + CommandField.LOAD_PLAYERS + " to load players to database")
        print(
            " - "
            + CommandField.PLAYERS_ALPHABETIC
            + " to list players in alphabetic order"
        )
        print(
            " - " + CommandField.PLAYERS_RANKING + " to list players in ranking order"
        )
        print(" - " + CommandField.BACK + " to go back to main menu")
        print(" - " + CommandField.EXIT + " to quit application")

    def get_warning(self):
        """Return the current warning message or the requested list."""
        if self.warning == "command unknown":
            print("Warning : this command is not valid")

        elif self.warning == "players alphabetical":
            sorted_list = dict(
                sorted(
                    Player.get_all.items(), key=lambda item: str(item[1].name).lower()
                )
            )
            print("The list of players (aphabetic order) is the following :")
            for player in sorted_list.values():
                print(f" - {player.name} {player.surname}")

        elif self.warning == "players ranking":
            sorted_list = dict(
                sorted(Player.get_all.items(), key=lambda item: int(item[1].ranking))
            )
            print("The list of players (ranking order) is the following :")
            for player in sorted_list.values():
                print(f" - {player.name} {player.surname} : {player.ranking}")

        else:
            return "Warning : unknown error occured"

    def display_warning(self):
        """Display additional warnings or information."""
        print(" ")
        print(" ")
        if not self.warning == "":
            self.get_warning()
