"""Project OC DAP 4 file with the tournament_ranking viewer."""

from app.models.player import Player

from app.config import CommandField


class TournamentRankingViewer:
    """Project tournament_ranking viewer class."""

    def __init__(self):
        """Init tournament_ranking viewer class."""
        self.warning = ""

    def display(self, tournament):
        """Display the view and the command list."""
        self.display_warning(tournament)

        print(f"You are editing tournament {tournament.name}")
        print("List of players :")
        number = 1
        for player_name, score in tournament.get_player_scores().items():
            player = Player.get_all[player_name]
            print(f" - {number} - {player.name} {player.surname} - {score}")
            number += 1
        print(" ")
        print("Command list :")
        number = 1
        for player_name, score in tournament.get_player_scores().items():
            player = Player.get_all[player_name]
            print(
                f" - {number}{CommandField.EDIT_PLAYER} "
                + f"to edit {player.name} {player.surname}"
            )
            number += 1
        if len(tournament.turns) == 0:
            print(" - " + CommandField.ADD_PLAYER + " to add player")
            print(" - " + CommandField.GENERATE_PLAYERS + " to generate 8 players")
        print(
            " - "
            + CommandField.PLAYERS_ALPHABETIC
            + " to list players in alphabetic order"
        )
        print(
            " - " + CommandField.PLAYERS_RANKING + " to list players in ranking order"
        )
        print(" - " + CommandField.BACK + " to go back to tournament")
        print(" - " + CommandField.EXIT + " to quit application")

    def get_warning(self, tournament):
        """Return the current warning message or the requested list."""
        if self.warning == "command unknown":
            print("Warning : this command is not valid")

        elif self.warning == "players alphabetical":
            tournament_players = {}
            for player_name in tournament.players_index:
                tournament_players[player_name] = Player.get_all[player_name]

            sorted_list = dict(
                sorted(
                    tournament_players.items(),
                    key=lambda item: str(item[1].name).lower(),
                )
            )
            print("The list of players (aphabetic order) is the following :")
            for player in sorted_list.values():
                print(f" - {player.name} {player.surname}")

        elif self.warning == "players ranking":
            tournament_players = {}
            for player_name in tournament.players_index:
                tournament_players[player_name] = Player.get_all[player_name]

            sorted_list = dict(
                sorted(
                    tournament_players.items(), key=lambda item: int(item[1].ranking)
                )
            )
            print("The list of players (ranking order) is the following :")
            for player in sorted_list.values():
                print(f" - {player.name} {player.surname} : {player.ranking}")

        else:
            print("Warning : unknown error occured")

    def display_warning(self, tournament):
        """Display additional warnings or information."""
        print(" ")
        print(" ")
        if not self.warning == "":
            self.get_warning(tournament)
