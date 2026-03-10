import os
from pathlib import Path
from dotenv import load_dotenv

# load env file
load_dotenv()

# load key for llm service
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ROOT_DIR = Path(__file__).resolve().parent
DB_PATH = ROOT_DIR / "smart_campus.sqlite"