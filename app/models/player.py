"""Project OC DAP 4 file with tournament related class."""


class Player:
    """Player characteristics to be handled by application."""

    def __init__(self, name, surname, birth, gender, ranking):
        """Init Player class."""
        self.name = name
        self.surname = surname
        self.birth_date = birth
        self.gender = gender
        self.ranking = ranking

    def return_serialized_player(self):
        """(Put description here)."""
        return {
            "name": self.name,
            "surname": self.surname,
            "birth_date": self.birth_date,
            "gender": self.gender,
            "ranking": self.ranking,
        }
