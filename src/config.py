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

FULL_GRID = int('0111111' * COLUMNS, 2)
TOP_ROW = int('1000000' * COLUMNS, 2)
BORDERS = int('1' * 15 + '1000000' * COLUMNS, 2)
MID_COL = int('1' * (ROWS) + '0' * 3 * (ROWS + 1), 2)

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

BOARD0_FILENAME = os.getenv("BOARD0_FILENAME") or "Board0.png"
BOARD0_PATH = os.path.join(dirname, "assets", "images", BOARD0_FILENAME)

COIN1_FILENAME = os.getenv("COIN1_FILENAME") or "Coin1.png"
COIN1_PATH = os.path.join(dirname, "assets", "images", COIN1_FILENAME)

COIN2_FILENAME = os.getenv("COIN1_FILENAME") or "Coin2.png"
COIN2_PATH = os.path.join(dirname, "assets", "images", COIN2_FILENAME)
