from fastapi import APIRouter, Depends, HTTPException , APIRouter, File, UploadFile
import os
import shutil
from ..process import get_pdf_text, get_text_chunks

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
    responses={404: {"description": "Not found"}},
)

UPLOAD_FOLDER = "uploaded_files"

@router.post("/")
async def upload_file(file: UploadFile = File(...)):

    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Unsupported file format. Only PDF files are allowed.")

    with open(os.path.join(UPLOAD_FOLDER, file.filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # Processing of the text
    text = get_pdf_text(file.filename)
    chunks = get_text_chunks(text)


    return {"filename": file.filename, "message": "File uploaded successfully", "chunks": chunks}


