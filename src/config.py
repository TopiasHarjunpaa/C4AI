import os
from dotenv import load_dotenv

TITLE = "C4AI"
FPS = 60

ROWS = 6
COLUMNS = 7

BLACK = (0, 0, 0)
PINK = (255, 0, 255)
WHITE = (255, 255, 255)
YELLOW = (255, 204, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 87, 217)

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

FONT_FILENAME = os.getenv("FONT_FILENAME") or "fontstyle.ttf"
FONT_PATH = os.path.join(dirname, "assets", "fonts", FONT_FILENAME)

LOGO_FILENAME = os.getenv("GAME_LOGO_FILENAME") or "game_logo.png"
LOGO_PATH = os.path.join(dirname, "assets", "fonts", LOGO_FILENAME)

BG_IMG_FILENAME = os.getenv("BG_IMG_FILENAME") or "background.png"
BG_IMG_PATH = os.path.join(dirname, "assets", "images", BG_IMG_FILENAME)
