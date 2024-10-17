

from pathlib import Path

try:
    ROOT_DIR = Path(__file__).parent.parent

    ASSIGNMENTS_DIR = ROOT_DIR / "assignments"

    LOGS_DIR = ROOT_DIR / "logs"
    LOG_PATH = LOGS_DIR / ".log"

    QUIZ_DIR = ROOT_DIR / "quizzes"

    TEST_DIR = ROOT_DIR / "tests"

    UTILS_DIR = ROOT_DIR / "utils"

except Exception as e:
    print(f"An error occured while setting file paths.\n{e}")
    exit()



