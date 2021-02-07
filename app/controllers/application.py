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
        self.get_argument_functions["controller"] = self.get_controller
        self.get_argument_functions[
            "edit_tournament_controller"
        ] = self.get_edit_tournament_controller

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
            arguments.append(self.get_argument_functions[argument]())

        return arguments

    def get_tournament_list(self):
        """(Put description here)."""
        return self.tournament_list

    def get_controller(self):
        """(Put description here)."""
        return self.controller

    def get_edit_tournament_controller(self):
        """(Put description here)."""
        return self.controller.commands_controllers[ViewName.view_edit_tournament]


" sty -> coloration de la console"
