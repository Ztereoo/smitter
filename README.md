# smitter

Smitter is a learning project built with Flask. 
It serves as a simple web application that allows users to:
-login/logout
-authenticate
-create posts (like twitter)
The project helps to practice Flask fundamentals, including working with templates and databases.

## Project Structure

- `__init__.py`: Main application file
- `models.py`: Database models
- `routes.py` : endpoint router 
- `templates/`: HTML templates
- `static/`: Static files (CSS, images)
- `requirements.txt`: Project dependencies

## Endpoints
  

### `/`
- **Method**: `GET`
- **Description**: The homepage of the application. Renders the main landing page.

### `/posts`
- **Method**: `GET`
- **Description**: Displays a list of all posts. Accessible only by logged-in users.
- **Response**: Renders a template with a list of posts.

### `/create`
- **Method**: `GET`, `POST`
- **Description**: Allows logged-in users to create a new post.
- **Parameters**:
  - `title`: The title of the post.
  - `content`: The content of the post.
- **Response**: Redirects to the posts page after successful creation. Displays a flash message on success or failure.

### `/update/<int:post_id>`
- **Method**: `GET`, `POST`
- **Description**: Allows users to update an existing post by ID.
- **Parameters**:
  - `post_id`: The ID of the post to update.
  - `title`: The updated title.
  - `content`: The updated content.
- **Response**: Redirects to the posts page after successful update. Displays a flash message on success.

### `/delete/<int:post_id>`
- **Method**: `POST`
- **Description**: Deletes a post by ID.
- **Parameters**:
  - `post_id`: The ID of the post to delete.
- **Response**: Redirects to the posts page after successful deletion. Displays a flash message on success.

### `/search`
- **Method**: `GET`, `POST`
- **Description**: Allows users to search posts by keyword.
- **Parameters**:
  - `keyword`: The search term to filter posts by title or content.
- **Response**: Displays the filtered posts. Redirects back if no keyword is provided.

### `/login`
- **Method**: `GET`, `POST`
- **Description**: Login page for users. Users can log in with their credentials.
- **Parameters**:
  - `login`: Username or email.
  - `password`: User's password.
- **Response**: Redirects to the home page upon successful login or shows an error on failure.


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ztereoo/smitter.git

2. Install dependencies:
  pip install -r requirements.txt

3. Run the application:
  python run.py

4. Open your browser and go to http://127.0.0.1:5000/.

This project is licensed under the Apache-2.0 License - see the LICENSE.txt file for details.


   
