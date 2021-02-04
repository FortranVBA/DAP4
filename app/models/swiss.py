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

        if not previous_matchs:
            # Implémenter : Si nombre impair, enlever le dernier joueur
            middle = len(sorted_players_keys) // 2
            players = sorted_players_keys[middle:]
            opponents = sorted_players_keys[:middle]

            for player, opponent in zip(players, opponents):
                matchs_keys.append([player, opponent])

            return matchs_keys

        while sorted_players_keys:
            player = sorted_players_keys.pop(0)
            if not sorted_players_keys:
                matchs_keys.append((player,))

            else:
                opponent_index = 0
                opponent = sorted_players_keys[opponent_index]
                while (player, opponent) in previous_matchs or (
                    opponent,
                    player,
                ) in previous_matchs:
                    opponent_index += 1
                    opponent = sorted_players_keys[opponent_index]

                matchs_keys.append((player, opponent))
                sorted_players_keys.remove(player)
                sorted_players_keys.remove(opponent)

        return matchs_keys
