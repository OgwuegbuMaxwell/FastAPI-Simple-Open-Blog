from fastapi import FastAPI
from database import models
from database.database import engine
from fastapi.staticfiles import StaticFiles

# Import CORS Middleware
from fastapi.middleware.cors import CORSMiddleware

from routers import post

app = FastAPI()


app.include_router(post.router)


# handle database creation
models.Base.metadata.create_all(engine)


# handle static files
app.mount('/images', StaticFiles(directory='images'), name='images')


# Handle CORS Middleware
# without properly setting up the middleware, we may not be able to make api calls in the same machine
origins = [
    'http://localhost:3000' # we will use port 3000 for react application
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Specify your trusted domains
    allow_credentials=True,
    allow_methods=["*"],  # Restrict methods
    allow_headers=["*"],  # Restrict headers
)
