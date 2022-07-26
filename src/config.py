import os
from dotenv import load_dotenv

TITLE = "C4AI"
FPS = 60

ROWS = 6
COLUMNS = 7

PINK = (255, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 204, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

FONT_FILENAME = os.getenv("FONT_FILENAME") or "fontstyle.ttf"
FONT_PATH = os.path.join(dirname, "assets", "fonts", FONT_FILENAME)
