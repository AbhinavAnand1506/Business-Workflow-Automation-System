from flask import Flask, request, jsonify
from sqlalchemy import create_engine
import os

from config import DATABASE_URI, UPLOAD_FOLDER
from services.workflow_service import handle_workflow
from models.db_model import init_db

app = Flask(__name__)

engine = create_engine(DATABASE_URI)
init_db(engine)

# Home route
@app.route('/')
def home():
    return {"message": "Workflow Automation System Running"}

# Upload API
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = handle_workflow(file_path)

    return jsonify(result)

# Get stored data
@app.route('/health', methods=['GET'])
def health():
    return {"status": "running"}

if __name__ == '__main__':
    app.run(debug=True)
