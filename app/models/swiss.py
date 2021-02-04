"""Project OC DAP 4 file with tournament related class."""


class SwissSystem:
    """Round characteristics to be handled by application."""

    def __init__(self):
        """Init Tournament class."""
        pass

    @staticmethod
    def get_next_turn(previous_matchs, players_rank):
        """Init Tournament class."""
        matchs_keys = []

        sorted_dict = dict(sorted(players_rank.items(), key=lambda item: item[1]))
        sorted_players_keys = list(sorted_dict.keys())

        if previous_matchs == []:
            # Implémenter : Si nombre impair, enlever le dernier joueur
            middle = int(len(sorted_players_keys) / 2)
            opponents_1 = sorted_players_keys[:middle]
            opponents_2 = sorted_players_keys[middle:]

            for oppenent_1, oppenent_2 in zip(opponents_1, opponents_2):
                matchs_keys.append([oppenent_1, oppenent_2])

        else:
            while not sorted_players_keys == []:
                next_player = sorted_players_keys[0]
                if len(sorted_players_keys) == 1:
                    matchs_keys.append([next_player])
                    sorted_players_keys.remove(next_player)

                else:
                    next_opponent_int = 1
                    next_opponent = sorted_players_keys[next_opponent_int]
                    while [next_player, next_opponent] in previous_matchs or [
                        next_opponent,
                        next_player,
                    ] in previous_matchs:
                        next_opponent_int += 1
                        next_opponent = sorted_players_keys[next_opponent_int]

                    matchs_keys.append([next_player, next_opponent])
                    sorted_players_keys.remove(next_player)
                    sorted_players_keys.remove(next_opponent)

        return matchs_keys
