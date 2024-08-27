# Flask API Starter Template

This repository contains a basic template to kickstart API projects using Flask. It includes initial setup, recommended directory structure, and example code to get started quickly.

## Project Structure

- `app/` - Contains the main application code.
  - `__init__.py` - Initializes the Flask application and sets up the modules.
  - `routes/`
    - `__init__.py`  - Defines the API routes.
    - `api/`
        - `__init__.py` - Blueprint API.
        - `verify.py` - Verify API_KEY (Authorization).
- `config.py` - Application configuration.
- `requirements.txt` - Lists the project dependencies.
- `run.py` - Script to run the application.

## Prerequisites

Ensure that you have [Python](https://www.python.org/downloads/) installed. It is recommended to use a virtual environment.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/joao-coimbra/flask-api.git
    cd flask-api
    cp .env.example .env
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the following command:

```bash
python run.py
```

The application will be available at `http://localhost:5000`.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/joao-coimbra/flask-api/blob/main/LICENSE) file for details.
