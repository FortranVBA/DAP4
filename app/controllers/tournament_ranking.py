"""Project OC DAP 4 file with tournament related class."""

from app.views.tournament_ranking import TournamentRankingViewer

from app.config import CommandField
from app.config import ViewName

from app.models.player import Player


class TournamentRankingController:
    """Project application class."""

    def __init__(self, tournament):
        """Init Application class."""
        self.current_view = ViewName.RANKING
        self.sub_controller = None

        self.tournament = tournament

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.ADD_PLAYER: self.add_player,
            CommandField.GENERATE_PLAYERS: self.generate_player,
            CommandField.BACK: self.goto_edit_tournament_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
        }

        self.viewer = TournamentRankingViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.RANKING:
            self.viewer.display(self.tournament)
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.RANKING:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                return self.command_names[CommandField.UNKNOWN]()
        else:
            is_exit = self.sub_controller.exe_command(command)
            if self.sub_controller.current_view == ViewName.RANKING:
                self.current_view = ViewName.RANKING
                self.sub_controller = None
            return is_exit

    def exit_application(self):
        """(Put description here)."""
        return True

    def add_player(self):
        """(Put description here)."""
        name_new = input("Enter player name : ")
        surname_new = input("Enter player surname : ")
        birthday_new = input("Enter player birth date : ")
        sex_new = input("Enter player sex : ")
        ranking_new = input("Enter player ranking : ")

        new_player = Player(
            name_new, surname_new, birthday_new, sex_new, int(ranking_new)
        )
        self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

        return False

    def generate_player(self):
        """(Put description here)."""
        for number in range(1, 9):
            new_player = Player(
                "Name" + str(number),
                "Surname" + str(number),
                "birthday_new",
                "sex_new",
                21 + 2 * number,
            )
            self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def goto_edit_tournament_menu(self):
        """(Put description here)."""
        self.current_view = ViewName.EDIT_TOURNAMENT

        self.viewer.warning = ""

        return False
