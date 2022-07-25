import random

class AiService:
    """A class to represent AI services.

    Attributes:
        board: Board object.
    """
    def __init__(self, board):
        """Constructs all the necessary attributes for the AI service object.

        Args:
            board (Board: Board object
        """
        self._board = board
    
    def calculate_move_randomly(self):
        """Calculates next move randomly.
        Checks first available columns to put coin
        and chooses randomly one of the available columns.

        Returns:
            int: Index of the chosen column.
        """

        available_columns = self._board.get_available_columns()
        column_number = random.choice(available_columns)
        return column_number

