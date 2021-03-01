"""Project OC DAP 4 file with the player commands."""

from app.config import CommandField


class AddPlayer:
    """Project add_player command class."""

    def __init__(self, _app, viewer, tournament):
        """Init add_player command class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.player import Player
        import re

        name_new = input("Enter player name : ")
        surname_new = input("Enter player surname : ")

        date_format = re.compile(".{2}/.{2}/.{4}")
        birthday_new = input("Enter player birth date (format dd/mm/yyyy): ")
        while not date_format.match(birthday_new):
            print("Only authorized format is dd/mm/yyyy")
            birthday_new = input("Enter player birth date (format dd/mm/yyyy): ")

        sex_new = input("Enter player sex (M or F): ")
        while sex_new not in ["M", "F"]:
            print("Only authorized values are 'M' or 'F'")
            sex_new = input("Enter player sex (M or F): ")

        ranking_new = input("Enter player ranking : ")
        while not self.is_string_positive_integer(ranking_new):
            print("Only authorized values are positive integers")
            ranking_new = input("Enter player ranking : ")

        new_player = Player(
            name_new, surname_new, birthday_new, sex_new, int(ranking_new)
        )
        self.tournament.players_index.append(new_player.player_index)

        self.viewer.warning = ""

        return False

    def is_string_positive_integer(self, input_string):
        """Return if a string is a positive integer."""
        try:
            int(input_string)
            if int(input_string) > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.ADD_PLAYER:
            return True
        else:
            return False


class GeneratePlayers:
    """Project generate_players command class."""

    def __init__(self, _app, viewer, tournament):
        """Init generate_players command class."""
        self._app = _app
        self.viewer = viewer
        self.tournament = tournament

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.player import Player

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

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.GENERATE_PLAYERS:
            return True
        else:
            return False


class ListPlayersAlphabeticalCommand:
    """Project list_players_alphabetical command class."""

    def __init__(self, viewer):
        """Init list_players_alphabetical command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        self.viewer.warning = "players alphabetical"
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.PLAYERS_ALPHABETIC:
            return True
        else:
            return False


class ListPlayersRankingCommand:
    """Project list_players_ranking command class."""

    def __init__(self, viewer):
        """Init list_players_ranking command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        self.viewer.warning = "players ranking"
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.PLAYERS_RANKING:
            return True
        else:
            return False


class LoadPlayerDatabase:
    """Project load_player_database command class."""

    def __init__(self, viewer):
        """Init load_player_database command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.player import Player

        Player.load_fromtinyDB()
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.LOAD_PLAYERS:
            return True
        else:
            return False


class SavePlayerDatabase:
    """Project save_player_database command class."""

    def __init__(self, viewer):
        """Init save_player_database command class."""
        self.viewer = viewer

    def exe_command(self):
        """Execute command and return False to not exit application."""
        from app.models.player import Player

        Player.save_tinyDB()
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.SAVE_PLAYERS:
            return True
        else:
            return False


class UpdatePlayerRanking:
    """Project update_player_ranking command class."""

    def __init__(self, viewer, player):
        """Init update_player_ranking command class."""
        self.viewer = viewer
        self.player = player

    def exe_command(self):
        """Execute command and return False to not exit application."""
        ranking_new = input("Enter new player ranking : ")

        self.player.ranking = ranking_new
        self.viewer.warning = ""
        return False

    def is_valid(self, command_name):
        """Return if user input matches the command name from config file."""
        if command_name == CommandField.UPDATE_RANKING:
            return True
        else:
            return False
