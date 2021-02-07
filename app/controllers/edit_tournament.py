"""Project OC DAP 4 file with tournament related class."""

from app.views.edit_tournament import EditTournamentViewer

from app.models.player import Player

from app.config import CommandField
from app.config import ViewName


class EditTournamentController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.selected_tournament = ""

        self.command_names = {}
        self.command_names[CommandField.exit_c] = self.exit_application
        self.command_names[CommandField.back_c] = self.goto_tournaments_menu
        self.command_names[CommandField.add_player_c] = self.add_player
        self.command_names[CommandField.generate_players_c] = self.generate_player
        self.command_names[CommandField.turns_c] = self.goto_turns_menu
        self.command_names[CommandField.create_next_turn_c] = self.create_next_turn

        self.arguments_needed = {}
        self.arguments_needed[CommandField.exit_c] = self.return_no_argument
        self.arguments_needed[
            CommandField.back_c
        ] = self.return_arguments_tournaments_menu
        self.arguments_needed[
            CommandField.add_player_c
        ] = self.return_arguments_add_player
        self.arguments_needed[
            CommandField.generate_players_c
        ] = self.return_arguments_generate_player
        self.arguments_needed[CommandField.turns_c] = self.return_arguments_turns_menu
        self.arguments_needed[
            CommandField.create_next_turn_c
        ] = self.return_arguments_create_next_turn

        self.viewer = EditTournamentViewer()

    def display(self):
        """(Put description here)."""
        self.viewer.display()

    def set_selected_tournament(self, name, tournament):
        """(Put description here)."""
        self.selected_tournament = name
        self.viewer.set_selected_tournament(
            tournament.name,
            tournament.location,
            tournament.date,
            tournament.turn_number,
            len(tournament.turns),
            len(tournament.players_index),
            tournament.time_control,
            tournament.description,
        )

    def get_arguments(self, command):
        """(Put description here)."""
        return self.arguments_needed[command]()

    def exe_command(self, command, arguments):
        """(Put description here)."""
        if command in self.command_names:
            return self.command_names[command](arguments)
        else:
            return self.command_names[CommandField.unknown_c](arguments)

    def exit_application(self, arguments):
        """(Put description here)."""
        return True

    def return_arguments_tournaments_menu(self):
        """(Put description here)."""
        arguments = []
        arguments.append("controller")
        return arguments

    def goto_tournaments_menu(self, arguments):
        """(Put description here)."""
        current_view = arguments[0].current_view

        current_view = ViewName.view_tournaments

        arguments[0].current_view = current_view

        self.viewer.warning = ""

        return False

    def return_arguments_add_player(self):
        """(Put description here)."""
        arguments = []
        arguments.append("player_list")
        arguments.append("tournament_list")
        return arguments

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
        player_list[player_index_new] = Player(
            name_new, surname_new, birthday_new, sex_new, ranking_new
        )

        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        arguments[0] = player_list
        arguments[1] = tournament_list

        return False

    def return_arguments_generate_player(self):
        """(Put description here)."""
        arguments = []
        arguments.append("player_list")
        arguments.append("tournament_list")
        return arguments

    def generate_player(self, arguments):
        """(Put description here)."""
        player_list = arguments[0]
        tournament_list = arguments[1]

        player_index_new = "p1"
        player_list[player_index_new] = Player(
            "Name1", "Surname1", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p2"
        player_list[player_index_new] = Player(
            "Name2", "Surname2", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p3"
        player_list[player_index_new] = Player(
            "Name3", "Surname3", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p4"
        player_list[player_index_new] = Player(
            "Name4", "Surname4", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p5"
        player_list[player_index_new] = Player(
            "Name5", "Surname5", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p6"
        player_list[player_index_new] = Player(
            "Name6", "Surname6", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p7"
        player_list[player_index_new] = Player(
            "Name7", "Surname7", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        player_index_new = "p8"
        player_list[player_index_new] = Player(
            "Name8", "Surname8", "birthday_new", "sex_new", 5
        )
        tournament_list[self.selected_tournament].players_index.append(player_index_new)

        arguments[0] = player_list
        arguments[1] = tournament_list

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

    def return_arguments_create_next_turn(self, arguments):
        """(Put description here)."""
        arguments = []
        arguments.append("tournament_list")
        arguments.append("player_list")
        arguments.append("controller")
        arguments.append("edit_turn_controller")
        return arguments

    def create_next_turn(self, arguments):
        """(Put description here)."""
        tournament_list = arguments[0]
        player_list = arguments[1]
        current_view = arguments[2].current_view
        edit_turn_controller = arguments[3]

        name_new = input("Enter turn name : ")
        tournament_list[self.selected_tournament].get_next_turn(name_new, player_list)
        current_view = ViewName.view_edit_turn
        edit_turn_controller.selected_turn = (
            len(tournament_list[self.selected_tournament].turns) - 1
        )

        arguments[0] = tournament_list
        arguments[1] = player_list
        arguments[2].current_view = current_view
        arguments[3] = edit_turn_controller

        self.viewer.warning = ""

        return False

    def print_unknown_command(self, arguments):
        """(Put description here)."""
        self.viewer.warning = "command unknown"

        return False

    def return_no_argument(self):
        """(Put description here)."""
        return []
