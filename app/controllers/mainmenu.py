"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_tournament import EditTournamentController
from app.controllers.edit_turn import EditTurnController
from app.controllers.print import PrintMenuController
from app.controllers.tournaments import TournamentMenuController
from app.controllers.turns import TurnsController
from app.controllers.players import PlayersController


from app.views.mainmenu import MainMenuViewer

from app.config import CommandField
from app.config import ViewName


class MainMenuController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.current_view = ViewName.view_main
        self.sub_controller = None

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.new_c] = self.goto_create_menu
        self.command_names[CommandField.tournaments_c] = self.goto_tournaments_menu
        self.command_names[CommandField.players_c] = self.goto_players_menu
        self.command_names[CommandField.print_c] = self.goto_print_menu
        self.command_names[CommandField.unknown_c] = self.print_unknown_command

        self.viewer = MainMenuViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.view_main:
            self.viewer.display()
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.view_main:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                return self.command_names[CommandField.unknown_c]()
        else:
            self.sub_controller.exe_command(command)

    def exit_application(self):
        """(Put description here)."""
        return True

    def return_arguments_create_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("tournament_list")
        arguments.append("controller")
        arguments.append("edit_tournament_controller")
        return arguments

    def goto_create_menu(self):
        """(Put description here)."""
        self.sub_controller = EditTournamentController(None, True)

        self.current_view = ViewName.view_edit_tournament

        self.viewer.warning = ""

        return False

    def return_arguments_tournaments_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("tournaments_controller")
        arguments.append("tournament_list")
        return arguments

    def goto_tournaments_menu(self):
        """(Put description here)."""
        current_view = ViewName.view_tournaments
        tournaments_controller.set_tournament_names(tournament_list)

        arguments[0].current_view = current_view
        arguments[1] = tournaments_controller
        arguments[2] = tournament_list

        self.viewer.warning = ""

        return False

    def return_arguments_print_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_print_menu(self):
        """(Put description here)."""
        current_view = ViewName.view_print

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def return_arguments_players_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("players_controller")
        arguments.append("player_list")
        return arguments

    def goto_players_menu(self):
        """(Put description here)."""
        current_view = ViewName.view_players
        players_controller.set_player_names(player_list)

        arguments[0].current_view = current_view
        players_controller = arguments[1]
        arguments[2] = player_list

        self.viewer.warning = ""

        return False

    def print_unknown_command(self):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_no_argument(self):
        """(Put description here)."""
        return []
