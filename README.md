# FastAPI Project

This project is a FastAPI-based web application with PostgreSQL as the database. It uses **Poetry** for dependency management and includes features like database session handling, modular routing, and middleware.

# **Requirements**

Before starting, ensure you have the following installed:

* Python 3.13 or higher
* PostgreSQL
* Poetry (for dependency management)

# To Start

Create a [.env](vscode-file://vscode-app/Applications/Visual%20Studio%20Code.app/Contents/Resources/app/out/vs/code/electron-sandbox/workbench/workbench.html) file in the root directory and add the following:

DATABASE_URL=postgresql+asyncpg://`<username>`:`<password>`@`<host>`:`<port>`/`<database>`

Then run several commands in terminal:

```
poetry run alembic upgrade head

poetry run uvicorn app.app:app --reload
```
