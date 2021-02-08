"""Project OC DAP 4 file with tournament related class."""

from app.controllers.edit_tournament import EditTournamentController
from app.controllers.edit_turn import EditTurnController
from app.controllers.mainmenu import MainMenuController
from app.controllers.print import PrintMenuController
from app.controllers.tournaments import TournamentMenuController
from app.controllers.turns import TurnsController
from app.controllers.players import PlayersController


from app.config import ViewName

import os


class Controller:
    """Project application class."""

    def __init__(self, player_list, tournament_list):
        """Init Application class."""
        self.current_view = ViewName.view_main

        self.commands_controllers = {}
        self.commands_controllers[ViewName.view_main] = MainMenuController()
        self.commands_controllers[
            ViewName.view_edit_tournament
        ] = EditTournamentController()
        self.commands_controllers[ViewName.view_print] = PrintMenuController()
        self.commands_controllers[
            ViewName.view_tournaments
        ] = TournamentMenuController()
        self.commands_controllers[ViewName.view_edit_turn] = EditTurnController()
        self.commands_controllers[ViewName.view_turns] = TurnsController()
        self.commands_controllers[ViewName.view_players] = PlayersController()

        self.current_error = ""
        self.selected_turn = 0

    def display(self):
        """(Put description here)."""
        self.commands_controllers[self.current_view].display()

    def clear_screen(self):
        """(Put description here)."""
        os.system("cls")

    def get_arguments(self, command):
        """(Put description here)."""
        return self.commands_controllers[self.current_view].get_arguments(command)

    def exe_command(self, command, arguments):
        """(Put description here)."""
        return self.commands_controllers[self.current_view].exe_command(
            command, arguments
        )
