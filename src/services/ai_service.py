import random

class AiService:
    """A class to represent AI services.

    Attributes:
        situation: Situation service object.
    """
    def __init__(self, situation):
        """Constructs all the necessary attributes for the AI service object.

        Args:
            situation (Situation): Situation service object
        """
        self._situation = situation
    
    def calculate_move_randomly(self):
        """Calculates next move randomly.
        Checks first available columns to put coin
        and chooses randomly one of the available columns.

        Returns:
            int: Index of the chosen column.
        """

        available_columns = self._situation.get_available_columns()
        column_number = random.choice(available_columns)
        return column_number

