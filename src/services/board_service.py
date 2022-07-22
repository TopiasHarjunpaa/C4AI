import pygame
from entities.sprites import Sprites

class BoardService:
    """A class to represent game board services.
    Attributes:
        width: Width of the display.
        height: Heigth of the display.
    """

    def __init__(self, width, height):
        """Constructs all the necessary attributes for the board service object.
        Args:
            width (int): Width of the display.
            height (int): Heigth of the display.
        """
        self.grid = [[0 for row in range(7)] for col in range(6)]
        self.sprites = Sprites(self, width, height)
        self.all_sprites = self.sprites.all_sprites
        self.update()

    def update(self):
        """To be added
        """
        self.all_sprites.update()


    def add_token(self, col_number, player_number):
        """To be added
        """
        for row_number in reversed(range(6)):
            if self.grid[row_number][col_number] == 0:
                self.grid[row_number][col_number] = player_number
                self.sprites.draw_new_token(row_number ,col_number, player_number)
                return True
        return False


    def test_grid(self):
        for row in self.grid:
            print(row)
    
    def check_win(self, player_number):
        """To be added
        """
        # Vertical check
        for row in range(3):
            for col in range(6):
                if (self.grid[row][col] == player_number and 
                    self.grid[row+1][col] == player_number and 
                    self.grid[row+2][col] == player_number and 
                    self.grid[row+3][col] == player_number):
                    return True

        # Horizontal check
        for row in range(5):
            for col in range(4):
                if (self.grid[row][col] == player_number and 
                    self.grid[row][col+1] == player_number and 
                    self.grid[row][col+2] == player_number and 
                    self.grid[row][col+3] == player_number):
                    return True     

        # Up diagonal check
        for row in range(3,6):
            for col in range(4):
                if (self.grid[row][col] == player_number and 
                    self.grid[row-1][col+1] == player_number and 
                    self.grid[row-2][col+2] == player_number and 
                    self.grid[row-3][col+3] == player_number):
                    return True 

        # Up diagonal check
        for row in range(3):
            for col in range(4):
                if (self.grid[row][col] == player_number and 
                    self.grid[row+1][col+1] == player_number and 
                    self.grid[row+2][col+2] == player_number and 
                    self.grid[row+3][col+3] == player_number):
                    return True 

        return False