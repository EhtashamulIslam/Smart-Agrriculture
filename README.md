
## Setting Up the Development Environment

Follow these steps to set up and run the project locally:

1. **Create a Virtual Environment**  
    Run the following command to create a virtual environment:
    ```bash
    python -m venv .venv
    ```

2. **Activate the Virtual Environment**  
    On Windows:
    ```bash
    .\.venv\Scripts\Activate
    ```
    On macOS/Linux:
    ```bash
    source .venv/bin/activate
    ```

3. **Install Dependencies**  
    Install the required dependencies using:
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Database Migrations**  
    Run the migrations to set up the database schema:
    ```bash
    python manage.py migrate
    ```

5. **Start the Development Server**  
    Launch the application locally:
    ```bash
    python manage.py runserver
    ```

Your application should now be running and accessible at `http://127.0.0.1:8000/`.

