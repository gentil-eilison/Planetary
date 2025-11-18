# Planetary - Your API for Managing Planets
A Django REST Framework API for managing planets, containing a CRUD API.
The user can manage the planets and their climates and terrains through RESTful API endpoints.

# Tech Stack
For this project, I used:
- Django
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker
- Docker Compose

# Setup & Installation
You can install the requirements by using the `pyroject.yaml` file and passing the `--group dev` flag.  
Start the project by runing `python3 manage.py runserver` and the Celery thread by using `celery -A st_planets.celery worker --loglevel=INFO`.  
Celery and Redis are needed for the data collection asynchronous task to get data from the SWAPI.  
If you want to, you can simply run the `docker-compose.local.yml` file. Just make sure you set the `.envs/local/.django` and `.envs/local/.postgres` beforehand.  
API documentation is available at `/api/docs/swagger-ui` or `/api/docs/redoc`.

# Use-Case Diagram
![ST Planets Use-Case](https://github.com/user-attachments/assets/cab9094b-6b0b-449e-adf3-f26b57c7dbb1)

# Entity-Relationship Diagram
![ST Planets ER](https://github.com/user-attachments/assets/38c098b5-9512-4852-8d6e-fffcd0198dc6)
