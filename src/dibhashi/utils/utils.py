import os
import uuid
from dotenv import load_dotenv

# Define the path to .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

def get_session_id():
    session_id = uuid.uuid4().hex  # 32‑char hex string from a random UUID :contentReference[oaicite:4]{index=4}
    return session_id


def get_existing_session_dir(session_id: str) -> str:
    """
    Returns the existing session directory path under DOWNLOAD_DIR.
    Raises if the directory does not exist or DOWNLOAD_DIR is unset.
    
    Example:
      DOWNLOAD_DIR="src/dibhashi/static/downloads"
      session_id="abc123"
      → returns "src/dibhashi/static/downloads/abc123"
    """
    download_dir = os.getenv("DOWNLOAD_DIR")
    if not download_dir:
        raise RuntimeError("DOWNLOAD_DIR is not set in .env")

    path = os.path.join(download_dir, session_id)
    if not os.path.isdir(path):
        raise FileNotFoundError(f"Session directory not found: {path}")

    return path

def make_session_output_dir(session_id):
    """
    Example:
      DOWNLOAD_DIR="src/dibhashi/static/downloads"
      → returns: "src/dibhashi/static/downloads/3f2a1e4b6c7d8e9fabcd1234567890ab"
    """
    download_dir = os.getenv("DOWNLOAD_DIR")
    if not download_dir:
        raise RuntimeError("✅ DOWNLOAD_DIR is not set in .env")

    output_dir = os.path.join(download_dir, session_id)
    os.makedirs(output_dir, exist_ok=True)
    return output_dir
