"""Project OC DAP 4 file with tournament related class."""

from app.controllers.mainmenu import MainMenuController

import os


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.main_controller = MainMenuController()

        self.is_exit = False

    def run(self):
        """Run  Application class."""
        while not self.is_exit:
            self.main_controller.display()

            command = self.get_command()
            self.is_exit = self.main_controller.exe_command(command)

            # self.controller.clear_screen()
        return

    def get_command(self):
        """(Put description here)."""
        command = input("Enter your command: ")
        return command

    def display(self):
        """(Put description here)."""
        self.main_controller.display()

    def clear_screen(self):
        """(Put description here)."""
        os.system("cls")

    def exe_command(self, command):
        """(Put description here)."""
        return self.commands_controllers[self.current_view].exe_command(command)


" sty -> coloration de la console"
