"""Project OC DAP 4 file with tournament related class."""

from app.views.edit_tournament import EditTournamentViewer
from app.controllers.edit_turn import EditTurnController

from app.config import CommandField
from app.config import ViewName

from app.models.tournament import Tournament
from app.models.player import Player


class EditTournamentController:
    """Project application class."""

    def __init__(self, tournament, is_new):
        """Init Application class."""
        self.current_view = ViewName.view_edit_tournament
        self.sub_controller = None

        if is_new:
            name_new = input("Enter your tournament name : ")
            self.tournament = Tournament(name_new)
        else:
            self.tournament = tournament

        self.command_names = {
            CommandField.exit_c: self.exit_application,
            CommandField.back_c: self.goto_tournaments_menu,
            CommandField.add_player_c: self.add_player,
            CommandField.generate_players_c: self.generate_player,
            CommandField.turns_c: self.goto_turns_menu,
            CommandField.create_next_turn_c: self.create_next_turn,
        }

        self.viewer = EditTournamentViewer()

    def display(self):
        """(Put description here)."""
        if self.current_view == ViewName.view_edit_tournament:
            self.viewer.display(self.tournament)
        else:
            self.sub_controller.display()

    def exe_command(self, command):
        """(Put description here)."""
        if self.current_view == ViewName.view_edit_tournament:
            if command in self.command_names:
                return self.command_names[command]()
            else:
                return self.command_names[CommandField.unknown_c]()
        else:
            return self.sub_controller.exe_command(command)

    def exit_application(self):
        """(Put description here)."""
        return True

    def return_arguments_tournaments_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        arguments.append("tournaments_controller")
        arguments.append("tournament_list")

        return arguments

    def goto_tournaments_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view
        tournaments_controller = arguments[1]
        tournament_list = arguments[2]

        current_view = ViewName.view_tournaments
        tournaments_controller.set_tournament_names(tournament_list)

        self.viewer.warning = ""

        arguments[0].current_view = current_view
        arguments[1] = tournaments_controller
        arguments[2] = tournament_list

        return False

    def add_player(self, arguments):
        """(Put description here)."""
        player_list = arguments[0]
        tournament_list = arguments[1]

        name_new = input("Enter player name : ")
        surname_new = input("Enter player surname : ")
        birthday_new = input("Enter player birth date : ")
        sex_new = input("Enter player sex : ")
        ranking_new = input("Enter player ranking : ")
        player_index_new = name_new + surname_new

        player_index_new = player_list.add_player(
            name_new, surname_new, birthday_new, sex_new, ranking_new
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        self.set_selected_tournament(tournament_list[self.selected_tournament])

        arguments[0] = player_list
        arguments[1] = tournament_list

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

    def return_arguments_turns_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_turns_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view

        current_view = ViewName.view_turns

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def return_arguments_create_next_turn(self):
        """(Put description here)."""
        arguments = []
        arguments.append("tournament_list")
        arguments.append("player_list")
        arguments.append("controller")
        arguments.append("edit_turn_controller")
        return arguments

    def create_next_turn(self):
        """(Put description here)."""
        self.sub_controller = EditTurnController(self.tournament, None, True)

        self.current_view = ViewName.view_edit_turn

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False
