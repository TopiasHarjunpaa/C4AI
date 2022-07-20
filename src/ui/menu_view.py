class MenuView:
    """A class to represent menu view of UI.
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
        self.small = int(self._height / 20)
        self._lines = []

    def show(self):
        """Prepares all information to show for the renderer object.
        Information is forwarded inside list of lines.
        Following information will be rendered:
        1. Game and view name
        2. New game view key
        3. Exit key
        Args:
            records (list): List of save objects.
        """

        self._lines.append(["NEW GAME ( press N )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 2.4)])
        self._lines.append(["GAME SETUP ( press S )", self.small, self._width /
                            2, self._height / 2 + (self.small * 3.6)])
        self._lines.append(["EXIT ( press ESC )", self.small,
                            self._width / 2, self._height / 2 + (self.small * 4.8)])
        self._renderer.render_menu("MAIN MENU", self._lines)