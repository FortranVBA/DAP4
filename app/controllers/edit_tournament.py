"""Project OC DAP 4 file with tournament related class."""

from app.models.player import Player

from app.config import CommandField


class EditTournamentController:
    """Project application class."""

    def __init__(self):
        """Init Application class."""
        pass

    @staticmethod
    def get_command(tournament_list, player_list, viewer):
        """(Put description here)."""
        command = input("Enter your command: ")

        if command == CommandField.exit_c:
            return True
        elif command == CommandField.back_c:
            viewer.current_view = CommandField.tournaments_c
            viewer.current_error = ""
        elif command == CommandField.add_player_c:
            name_new = input("Enter player name : ")
            surname_new = input("Enter player surname : ")
            birthday_new = input("Enter player birth date : ")
            sex_new = input("Enter player sex : ")
            ranking_new = input("Enter player ranking : ")
            player_index_new = name_new + surname_new
            player_list[player_index_new] = Player(
                name_new, surname_new, birthday_new, sex_new, ranking_new
            )

            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

        elif command == CommandField.generate_players_c:

            player_index_new = "p1"
            player_list[player_index_new] = Player(
                "Name1", "Surname1", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p2"
            player_list[player_index_new] = Player(
                "Name2", "Surname2", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p3"
            player_list[player_index_new] = Player(
                "Name3", "Surname3", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p4"
            player_list[player_index_new] = Player(
                "Name4", "Surname4", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p5"
            player_list[player_index_new] = Player(
                "Name5", "Surname5", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p6"
            player_list[player_index_new] = Player(
                "Name6", "Surname6", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p7"
            player_list[player_index_new] = Player(
                "Name7", "Surname7", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

            player_index_new = "p8"
            player_list[player_index_new] = Player(
                "Name8", "Surname8", "birthday_new", "sex_new", 5
            )
            tournament_list[viewer.selected_tournament].players_index.append(
                player_index_new
            )

        elif command == CommandField.edit_turns:
            viewer.current_view = CommandField.edit_turns
            viewer.current_error = ""
        elif command == CommandField.create_next_turn:
            name_new = input("Enter turn name : ")
            tournament_list[viewer.selected_tournament].get_next_turn(
                name_new, player_list
            )

        else:
            viewer.current_error = "command unknown"

        return False
