import os

from dotenv import load_dotenv

load_dotenv()

CHECKPOINT_PATH = os.getenv("CHECKPOINT_PATH")
CHECKPOINT_REPO_ID = "google/timesfm-2.0-500m-pytorch"
BACKEND = "gpu"
CONTEXT_LEN = 32
HORIZON_LEN = 8
FORECASTABLE_THRESHOLD = 1
