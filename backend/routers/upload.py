from fastapi import APIRouter, Depends, HTTPException , APIRouter, File, UploadFile
import os
import shutil

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

    # Process the uploaded file (you can add your processing logic here)

    return {"filename": file.filename, "message": "File uploaded successfully"}


