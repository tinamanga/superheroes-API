# Superheroes API

A RESTful Flask API to manage Superheroes, their Powers, and how they relate through HeroPowers.

---

## Description

This project was built as part of a backend software engineering curriculum using **Flask**, **SQLAlchemy**, and **Flask-Migrate**. The API handles three key models:

- `Hero`: The superhero entity with attributes like name and supername.
- `Power`: Special powers that can be assigned to heroes.
- `HeroPower`: A join table that links Heroes and Powers, with a `strength` field.

It supports full CRUD operations and follows RESTful routing conventions.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Credits](#credits)
- [License](#license)

---

## ⚙️ Installation

1. Clone the repository:
  ```bash```
 git clone https://github.com/tinamanga/superheroes-API.git
 cd superheroes-API

2. Create and activate virtual environment:
```bash```
 python3 -m venv venv
 source venv/bin/activate  # on Linux/macOS
 venv\Scripts\activate     # on Windows

3. Install dependencies:
```bash```
   pip install -r requirements.
   
4. Run migrations:
```bash```
  flask db init
  flask db migrate -m "Initial"
  flask db upgrade

5. Seed the database:
```bash```
   python app/seed.py

6. Run the app:
```bash```
    flask run or
    python run.py

App will be available at http://localhost:5555.

####  Usage
Test the API using Postman, cURL, or a browser.

### Sample Endpoints:
- GET /heroes – List all heroes

- GET /heroes/<id> – Get hero with associated powers

- POST /hero_powers – Assign power to hero

- PATCH /powers/<id> – Update power description

All responses return appropriate status codes (200, 201, 400, 404) and JSON-formatted responses.

## Project Structure
```bash```
superheroes-api/
├── app/
│   ├── __init__.py           # Initializes the Flask app and       database
│   ├── models.py             # SQLAlchemy models and relationships
│   ├── routes.py             # API route definitions
│   └── seed.py               # Seed script to populate the database
├── instance/
│   └── app.db                # SQLite database (automatically created)
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/             # Auto-generated migration scripts
├── superheros.json           # Postman collection for testing
├── run.py                    # App entry point (runs on port 5555)
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── LICENSE                   # License information
└── venv/                     # Python virtual environment (excluded from Git)


## Features
- Full CRUD API for Heroes and Powers

- Nested JSON serialization

- Relationship management via join table

- Model validation (e.g., strength must be 'Strong', 'Weak', or 'Average')

- Error handling with appropriate status codes

Uses Flask-Migrate for database versioning

## Technologies Used
1. Python

2. Flask

3. Flask-SQLAlchemy

4. Flask-Migrate

5. SQLite (can be switched to PostgreSQL or MySQL)


## API Testing with Postman

To test the API, import the included Postman collection:

**File:** `challenge-2-superheroes.postman_collection.json`

### Available Endpoints

| Method | Endpoint               | Description                       |
|--------|------------------------|-----------------------------------|
| GET    | `/heroes`              | Get all heroes                    |
| GET    | `/heroes/<id>`         | Get a specific hero by ID         |
| GET    | `/powers`              | Get all powers                    |
| GET    | `/powers/<id>`         | Get a specific power by ID        |
| POST   | `/hero_powers`         | Assign a power to a hero          |
| PATCH  | `/powers/<id>`         | Update power description          |

To run the API locally, ensure the server is running at `http://localhost:5555`.

## Credits

Developed by **Christina Wachia Manga**  
Email: [christinamanga28@gmail.com](mailto:christinamanga28@gmail.com)

Project completed as part of the **Software Engineering Program at Moringa School**.

Inspired by Moringa School curriculum labs and learning materials, with additional reference from [freeCodeCamp](https://www.freecodeca Running on http://127.0.0.1:5000mp.org/), [Hashnode](https://hashnode.com/), and the official [Flask documentation](https://flask.palletsprojects.com/).

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Future Improvements
- Implement JWT Authentication

- Add Swagger API documentation

- Dockerize the app for easy deployment