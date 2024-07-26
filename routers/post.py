from fastapi import APIRouter, Depends, UploadFile, File
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database import db_post
import string, random, shutil


router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('')
def create(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get('/all')
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db)):
    return db_post.delete(id, db)


@router.post('/image')
def upload_image(image: UploadFile = File(...)):  # Function that handles image uploads. UploadFile is a FastAPI class for handling uploaded files.
    letter = string.ascii_letters  # Get all ASCII letters (both lowercase and uppercase)
    rand_str = ''.join(random.choice(letter) for i in range(6))  # Generate a random string of 6 letters
    new = f'_{rand_str}.'  # Create a new string that begins with an underscore followed by the random string and a dot
    filename = new.join(image.filename.rsplit('.', 1))  # Split the original filename to insert the random string before the file extension
    path = f'images/{filename}'  # Define the path where the image will be saved, including the new filename
    
    with open(path, "w+b") as buffer:  # Open a file at the given path in write-binary mode
        shutil.copyfileobj(image.file, buffer)  # Copy the uploaded image file to the newly created file on the server
    
    return {'filename': path}  # Return a JSON response with the path to the saved file


