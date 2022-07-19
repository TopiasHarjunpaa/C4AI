import os
from dotenv import load_dotenv

TITLE = "C4AI"
FPS = 60

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass
