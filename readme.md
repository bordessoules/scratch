# Flask REST API with Docker

## Overview

This project is a RESTful API built with Flask and containerized using Docker. It provides a robust foundation for managing items with features such as database integration (PostgreSQL), JWT authentication, and RESTful endpoints.

## Features

- RESTful API endpoints for CRUD operations on items
- PostgreSQL database integration using SQLAlchemy ORM
- JWT Authentication
- Dockerized application and database
- Modular Flask application structure
- Database migrations using Flask-Migrate

## Project Structure

```
project_root/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   └── item.py
│   ├── resources/
│   │   └── item.py
│   ├── services/
│   │   ├── api_routes.py
│   │   └── item_service.py
│   ├── utils/
│   │   └── image_handler.py
│   └── config.py
├── migrations/
├── uploads/
├── .env
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── run.py
└── start.sh
```

## Prerequisites

- Docker
- Docker Compose

## Setup and Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create a `.env` file in the project root and add the following environment variables:
   ```
   FLASK_APP=run.py
   FLASK_ENV=development
   SECRET_KEY=your_secret_key
   JWT_SECRET_KEY=your_jwt_secret_key
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_DB=your_db_name
   DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@db/${POSTGRES_DB}
   ```

3. Build and start the Docker containers:
   ```
   docker-compose up --build
   ```

## API Endpoints

- `GET /`: Root endpoint, returns a welcome message
- `POST /login`: Login endpoint, returns a JWT token
- `GET /items`: Retrieve all items
- `POST /items`: Create a new item
- `GET /items/<id>`: Retrieve a specific item
- `PUT /items/<id>`: Update a specific item
- `DELETE /items/<id>`: Delete a specific item

## Usage

To interact with the API, you can use tools like cURL, Postman, or write scripts using libraries like `requests` in Python.

Example using cURL:

1. Login to get a token:
   ```
   curl -X POST http://localhost:5000/login
   ```

2. Create an item (replace `<token>` with the token received from login):
   ```
   curl -X POST -H "Authorization: Bearer <token>" -H "Content-Type: application/json" -d '{"description":"Test item", "labels":["test"], "images":[]}' http://localhost:5000/items
   ```

3. Get all items:
   ```
   curl -H "Authorization: Bearer <token>" http://localhost:5000/items
   ```

## Development

To add new features or modify existing ones:

1. Make your changes in the appropriate files.
2. If you've made changes to the models, create a new migration:
   ```
   docker-compose exec web flask db migrate -m "Description of changes"
   ```
3. Apply the migration:
   ```
   docker-compose exec web flask db upgrade
   ```
4. Rebuild and restart the containers:
   ```
   docker-compose up --build
   ```

## Testing

(Add information about your testing strategy and how to run tests)

## Contributing

(Add guidelines for contributing to the project)

## License

(Add license information)
