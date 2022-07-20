import os
from dotenv import load_dotenv

TITLE = "C4AI"
FPS = 60

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

FONT_FILENAME = os.getenv("FONT_FILENAME") or "fontstyle.ttf"
FONT_PATH = os.path.join(dirname, "assets", "fonts", FONT_FILENAME)