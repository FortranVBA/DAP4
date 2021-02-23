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
        match_results = []

        sorted_dict = dict(sorted(players_rank.items(), key=lambda item: item[1]))
        sorted_players_keys = list(sorted_dict.keys())

        if not previous_matchs:
            if len(sorted_players_keys) % 2 == 1:
                last_player = sorted_players_keys[-1]
                matchs_keys.append((last_player,))
                match_results.append(())
                sorted_players_keys.remove(last_player)

            middle = len(sorted_players_keys) // 2
            players = sorted_players_keys[:middle]
            opponents = sorted_players_keys[middle:]

            for player, opponent in zip(players, opponents):
                matchs_keys.append((player, opponent))
                match_results.append(())

            return matchs_keys, match_results

        while sorted_players_keys:
            player = sorted_players_keys.pop(0)
            if not sorted_players_keys:
                matchs_keys.append((player,))

            else:
                opponent_index = 0
                opponent = sorted_players_keys[opponent_index]
                while SwissSystem.is_match_played(opponent, player, previous_matchs):
                    opponent_index += 1
                    opponent = sorted_players_keys[opponent_index]

                matchs_keys.append((player, opponent))
                match_results.append(())
                sorted_players_keys.remove(opponent)

        print(matchs_keys)
        print(match_results)

        return matchs_keys, match_results

    @staticmethod
    def is_match_played(opponent, player, previous_matchs):
        """Init Tournament class."""
        match_player_opponent_played = (player, opponent) in previous_matchs
        match_opponent_player_played = (opponent, player) in previous_matchs

        return match_player_opponent_played or match_opponent_player_played
