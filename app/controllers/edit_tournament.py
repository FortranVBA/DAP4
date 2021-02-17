"""Project OC DAP 4 file with tournament related class."""

from app.controllers.turns import TurnsController
from app.controllers.tournament_ranking import TournamentRankingController

from app.views.edit_tournament import EditTournamentViewer

from app.config import CommandField
from app.config import ViewName

from app.models.tournament import Tournament


class EditTournamentController:
    """Project application class."""

    def __init__(self, tournament, is_new):
        """Init Application class."""
        self.current_view = ViewName.EDIT_TOURNAMENT
        self.sub_controller = None

        if is_new:
            name_new = input("Enter your tournament name : ")
            self.tournament = Tournament(name_new)
        else:
            self.tournament = tournament

        self.command_names = {
            CommandField.EXIT: self.exit_application,
            CommandField.BACK: self.goto_tournaments_menu,
            CommandField.TURNS: self.goto_turns_menu,
            CommandField.UNKNOWN: self.print_unknown_command,
            CommandField.RANKING: self.goto_ranking_menu,
        }

        self.viewer = EditTournamentViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.EDIT_TOURNAMENT:
            self.viewer.display(self.tournament)
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.EDIT_TOURNAMENT:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                return self.command_names[CommandField.UNKNOWN]()
        else:
            is_exit = self.sub_controller.exe_command(command)
            if self.sub_controller.current_view == ViewName.EDIT_TOURNAMENT:
                self.current_view = ViewName.EDIT_TOURNAMENT
                self.sub_controller = None
            return is_exit

    def exit_application(self):
        """(Put description here)."""
        return True

    def goto_tournaments_menu(self):
        """(Put description here)."""
        self.current_view = ViewName.TOURNAMENTS

        self.viewer.warning = ""

        return False

    def goto_turns_menu(self):
        """(Put description here)."""
        self.sub_controller = TurnsController(self.tournament)

        self.current_view = ViewName.TURNS

        self.viewer.warning = ""

        return False

    def goto_ranking_menu(self):
        """(Put description here)."""
        self.sub_controller = TournamentRankingController(self.tournament)

        self.current_view = ViewName.RANKING

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False
