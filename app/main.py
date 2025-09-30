from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse
import os
import uuid

app = FastAPI(title="Meeting Assistant - Local Test")

UPLOAD_DIR = "data/audio"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head>
            <title>Upload de Reunião</title>
        </head>
        <body>
            <h1>Upload de Reunião</h1>
            <form action="/upload" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload_meeting(file: UploadFile = File(...)):
    try:
        file_ext = file.filename.split(".")[-1]
        unique_name = f"{uuid.uuid4()}.{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_name)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        return {
            "message": "Arquivo de reunião recebido com sucesso!",
            "file_path": file_path
        }

    except Exception as e:
        return {"error": str(e)}
