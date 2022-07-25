import pygame
from config import FONT_PATH, WHITE, YELLOW, RED, PINK, RED, GREEN


class Renderer:
    """A class to represent renderer object which renders the display.

    Attributes:
        display: Pygame display object.
        width (int): Width of the display.
        height (int): Heigth of the display.
    """

    def __init__(self, display, width, height):
        """Constructs all the necessary attributes for the renderer object.
        Background images will be scaled according to screen size.

        Args:
            display (Display): Pygame display object.
            width (int): Width of the display.
            height (int): Heigth of the display.
        """

        self._display = display
        self.width = width
        self.height = height
        self._big = int(self.height / 10)
        self._small = int(self.height / 20)
        self._extra_small = int(self.height / 30)
        self._cell_size = width / 20
        self._start_x = width / 2 - 3 * self._cell_size
        self._start_y = height / 2 - 2.5 * self._cell_size

    def render_game(self, board, player_number, game_ended):
        """Renders the display during game loop.
        Fills the display and draws all sprites and texts to the screen.

        Args:
            board (BoardService): Board service object.
            player_number (int): Player number (1 = first player, 2 = second player)
            game_ended (bool): Renders game ended screen if set to True.
            Otherwise renders normal game screen. Defaults to False.
        """
        
        color = RED
        if player_number ==  2:
            color = YELLOW
        
        player_text = f"PLAYER {player_number} TURN"
        if game_ended:
            player_text = f"PLAYER {player_number} HAS WON! (press N to play again)"

        self._display.fill((0, 0, 0))
        board.all_sprites.draw(self._display)
        self._draw_text("FOUR CONNECT GAME", self._small,
                        self.width / 2 + 3, self.height / 8 + 3, WHITE)
        self._draw_text("FOUR CONNECT GAME", self._small,
                        self.width / 2, self.height / 8, PINK)
        self._draw_text(player_text, self._extra_small,
                        self.width / 2 + 1.5, self.height / 5 + 1.5, WHITE)                
        self._draw_text(player_text, self._extra_small,
                        self.width / 2, self.height / 5, color)
        for i in range(7):
            self._draw_text(str(i+1), self._small, self._start_x + i * self._cell_size + 3, self._start_y + 6 * self._cell_size + 3, WHITE)
            self._draw_text(str(i+1), self._small, self._start_x + i * self._cell_size, self._start_y + 6 * self._cell_size, PINK)
        pygame.display.flip()      

    def render_menu(self, title, lines: list):
        """Renders the display during menu screens.
        Fills the display and draw texts with multiple colors.
        Read the information from each line and draw text according
        to the information.

        Args:
            title (str): Screen title text.
            lines (list): Information which is stored into multiple lines.
        """

        self._display.fill((0, 0, 0))
        self._draw_text("4CAI GAME", self._big,
                        self.width / 2 + 3, self.height / 5 + 3)
        self._draw_text("4CAI GAME", self._big,
                        self.width / 2, self.height / 5, (150, 50, 255))
        self._draw_text(title, self._big, self.width / 2 + 3,
                        self.height / 5 + 3 + (self._big * 1.2))
        self._draw_text(title, self._big, self.width / 2,
                        self.height / 5 + (self._big * 1.2), GREEN)

        for line in lines:
            if len(line) == 5:
                self._draw_text(line[0], line[1], line[2], line[3], line[4])
            else:
                self._draw_text(line[0], line[1], line[2], line[3])

        pygame.display.flip()

    def _draw_text(self, text, font_size, x_coordinate, y_coordinate, color=(255, 255, 255)):
        """Draws the text according to all necessary attributes.

        Args:
            text (str): Text
            font_size (int): Font size
            x_coordinate (int): Spawn location at the x-axis.
            y_coordinate (int): Spawn location at the y-axis.
            color (tuple, optional): Text color. Defaults to (255, 255, 255).
        """

        font = pygame.font.Font(FONT_PATH, font_size)
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect()
        text_rect.center = (x_coordinate, y_coordinate)
        self._display.blit(text_surf, text_rect)
