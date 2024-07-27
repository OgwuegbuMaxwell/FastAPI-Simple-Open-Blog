# FastAPI Simple Open Blog

This project is the backend part of a full-stack application using FastAPI. It provides APIs for a simple open blog where users can create, retrieve, and delete blog posts.

## Features

- Create blog posts with images.
- Retrieve all blog posts.
- Delete specific blog posts.
- CORS enabled for integration with the frontend.

## Technologies

- FastAPI
- SQLAlchemy for ORM
- SQLite for the database

## Setup and Installation

1. **Clone the Repository**:
    ```bash
   git clone https://github.com/OgwuegbuMaxwell/FastAPI-Simple-Open-Blog.git
   cd FastAPI-Simple-Open-Blog
    ```

2. **Clone the Repository**:
Create and Activate a Virtual Environment (Recommended):

    ```bash
    python -m venv env
    env\Scripts\activate  # On Windows
    source env/bin/activate  # On Unix or MacOS
    ```

3. Install Required Packages:
`pip install -r requirements.txt`


4. Run the Application:
`uvicorn main:app --reload`


### Endpoints

- POST /post/: Create a new post.
- GET /post/all: Get all posts.
- DELETE /post/{id}: Delete a specific post by ID.
- POST /post/image: Upload an image for the post.


### CORS Configuration
This project is configured to allow requests from the React frontend running on `http://localhost:3000`.

### Interaction with React Frontend
The backend is designed to work seamlessly with the React frontend, which is responsible for displaying the blog posts and interacting with these APIs. You can find the frontend at [React Simple Open Blog](https://github.com/OgwuegbuMaxwell/React-Simple-Open-Blog).


