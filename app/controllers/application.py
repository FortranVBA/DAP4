"""Project OC DAP 4 file with tournament related class."""

from app.controllers.mainmenu import MainMenuController


class Application:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        self.change_controller(MainMenuController())
        self.is_exit = False

    def run(self):
        """Run  Application class."""
        while not self.is_exit:
            self.controller.display()

            self.controller.get_command()
            self.is_exit = self.controller.command.exe_command()

            self.separate_screen()
        return

    def get_command(self):
        """(Put description here)."""
        command = input("Enter your command: ")
        return command

    def display(self):
        """(Put description here)."""
        self.controller.display()

    def separate_screen(self):
        """(Put description here)."""
        print(" ")
        print(" ")
        print("-----------------------------------")
        print("-----------------------------------")
        print("-----------------------------------")
        print(" ")
        print(" ")

    def exe_command(self, command):
        """(Put description here)."""
        return self.commands_controllers[self.current_view].exe_command(command)

    def change_controller(self, new_controller):
        """(Put description here)."""
        self.controller = new_controller
        self.controller._app = self
