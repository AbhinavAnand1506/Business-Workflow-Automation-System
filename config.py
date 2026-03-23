import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"

UPLOAD_FOLDER = os.path.join(BASE_DIR, 'data')

LOG_FILE = os.path.join(BASE_DIR, 'logs', 'app.log')
