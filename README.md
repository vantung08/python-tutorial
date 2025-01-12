# python-tutorial
Just a Hello-World for Python

Commandline
    source env_python_tutorial/bin/activate
    cd projects/python-tutorial/

Deactivate webapp in compose.yaml

Start local DB
    POSTGRESQL_URL = "postgresql://vantung08:12345678@localhost:5432/python-tutorial-postgresql"
    docker compose up

Start FastAPI app
    uvicorn users_management.main:users_management --host 0.0.0.0 --port 8000
    uvicorn auth_service.main:auth_service --host 0.0.0.0 --port 8001
