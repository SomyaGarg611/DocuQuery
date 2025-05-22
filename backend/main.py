from fastapi import FastAPI, HTTPException, File, Depends
from core.config import settings
from apis.base import api_router
from fastapi import UploadFile
from sqlalchemy.orm import Session
from db.session import get_db
from upload import upload_user_file

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION)
    include_router(app)
    return app

app=start_application()

@app.get("/")
def hello():
    return {"msg":"Welcome to Intelligent Query Processing System"}

import os
os.environ['GROQ_API_KEY'] = settings.GROQ_API_KEY 

@app.post("/upload", response_model=str)
async def upload_user_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file:
        raise HTTPException(status_code=400, detail="File not found")
    if not os.path.exists('/tmp'):
        os.makedirs('/tmp')
 
    #Creating temporary file in /tmp directory
    tempfile_path = os.path.join('/tmp', file.filename)
 
    with open(tempfile_path, 'wb+') as temp_file:
        content = await file.read()
        temp_file.write(content)
 
    #Passing this path to the upload_user_file function
    upload_user_file(tempfile_path)
    contents = await file.read()
    return "file"





