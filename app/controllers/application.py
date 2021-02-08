"""Project OC DAP 4 file with tournament related class."""

from app.controllers.controller import Controller

from app.config import ViewName


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.player_list = {}
        self.tournament_list = {}
        self.controller = Controller(self.player_list, self.tournament_list)
        self.exit = False

        self.get_argument_functions = {}
        self.get_argument_functions["tournament_list"] = self.get_tournament_list
        self.get_argument_functions["player_list"] = self.get_player_list
        self.get_argument_functions["controller"] = self.get_controller
        self.get_argument_functions[
            "edit_tournament_controller"
        ] = self.get_edit_tournament_controller
        self.get_argument_functions[
            "tournaments_controller"
        ] = self.get_tournaments_controller
        self.get_argument_functions[
            "edit_turn_controller"
        ] = self.get_edit_turn_controller
        self.get_argument_functions[
            "players_controller"
        ] = self.get_players_controller
        self.get_argument_functions["match"] = self.get_specific_match
        self.get_argument_functions["turns_controller"] = self.get_turns_controller
        self.get_argument_functions["active_tournament"] = self.get_active_tournament
        self.get_argument_functions["turn"] = self.get_specific_turn

    def run(self):
        """Run  Application class."""
        while not self.exit:
            self.controller.display()

            command = self.get_command()
            arguments = self.get_arguments(command)
            self.exit = self.controller.exe_command(command, arguments)

            # self.controller.clear_screen()
        return

    def get_command(self):
        """(Put description here)."""
        command = input("Enter your command: ")
        return command

    def get_arguments(self, command):
        """(Put description here)."""
        arguments = []
        needed_arguments = self.controller.get_arguments(command)

        for argument in needed_arguments:
            if argument in self.get_argument_functions:
                arguments.append(self.get_argument_functions[argument]())
            elif "match" in argument:
                number = int(argument.replace("match", ""))
                arguments.append(self.get_argument_functions["match"](number))
            elif "turn" in argument:
                number = int(argument.replace("turn", ""))
                arguments.append(self.get_argument_functions["turn"](number))
            else:
                print("Error get_arguments for command : " + command)

        return arguments

    def get_tournament_list(self):
        """(Put description here)."""
        return self.tournament_list

    def get_player_list(self):
        """(Put description here)."""
        return self.player_list

    def get_controller(self):
        """(Put description here)."""
        return self.controller

    def get_edit_tournament_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_edit_tournament]

    def get_tournaments_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_tournaments]

    def get_edit_turn_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_edit_turn]

    def get_specific_match(self, selected_match):
        """(Put description here)."""
        selected_tournament = self.controller.commands_controllers[
            ViewName.view_edit_tournament
        ].selected_tournament
        selected_turn = self.controller.commands_controllers[
            ViewName.view_edit_turn
        ].selected_turn

        return (
            self.tournament_list[selected_tournament]
            .turns[selected_turn]
            .matches[selected_match]
        )

    def get_specific_turn(self, selected_turn):
        """(Put description here)."""
        selected_tournament = self.controller.commands_controllers[
            ViewName.view_edit_tournament
        ].selected_tournament

        key_turn = list(self.tournament_list[selected_tournament].turns.keys())[
            selected_turn
        ]

        return self.tournament_list[selected_tournament].turns[key_turn]

    def get_turns_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_turns]

    def get_active_tournament(self):
        """(Put description here)."""
        selected_tournament = self.controller.commands_controllers[
            ViewName.view_edit_tournament
        ].selected_tournament

        return self.tournament_list[selected_tournament]

    def get_players_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_players]


" sty -> coloration de la console"
