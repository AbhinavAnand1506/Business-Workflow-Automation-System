from utils.data_processor import process_data
from utils.validators import validate_data

def handle_workflow(file_path):
    df, summary = process_data(file_path)

    errors = validate_data(df)

    if errors:
        return {"status": "error", "errors": errors}

    return {
        "status": "success",
        "summary": summary,
        "records": df.to_dict(orient='records')
    }
