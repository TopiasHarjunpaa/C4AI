from config import RED, YELLOW, GREEN

class SetupView:
    """A class to represent setup view of UI.
    
    Attributes:
        renderer: Renderer object.
    """

    def __init__(self, renderer):
        """Constructs all the necessary attributes for finish view.
        
        Args:
            renderer (Renderer): Renderer object which renders the display.
        """

        self._renderer = renderer
        self._width = self._renderer.width
        self._height = self._renderer.height
        self._small = int(self._height / 20)
        self._extra_small = int(self._height / 30)
        self._lines = []

    def show(self, player_setup):
        """Prepares all information to show for the renderer object.
        Information is forwarded inside list of lines.
        Following information will be rendered:
        
        1. Game and view name
        2. Player setup (1. player name versus 2. player name)
        4. Back to main menu key
        """

        self._lines.append([str(player_setup[0]), self._small,
                                self._width / 2, self._height / 2 - (self._small * 1), RED])
        self._lines.append(["( press 1 to scroll options )", self._extra_small,
                            self._width / 2, self._height / 2 - (self._small * 0.2)])          
        self._lines.append(["vs.", self._small, self._width / 2,
                            self._height / 2 + (self._small * 1.2), GREEN])         
        self._lines.append([str(player_setup[1]), self._small, self._width /
                                2, self._height / 2 + (self._small * 2.6), YELLOW])  
        self._lines.append(["( press 2 to scroll options )", self._extra_small,
                            self._width / 2, self._height / 2 + (self._small * 3.4)])

        self._lines.append(["EXIT ( press ESC )", self._small,
                            self._width / 2, self._height / 2 + (self._small * 5.6)])
        self._renderer.render_menu("GAME SETUP", self._lines)