# FastAPI Supercharged
![FastAPI Supercharged](https://i.ibb.co/QfVhcV8/Create-A-Horizontal-Logo-For-Fast-Api-Supercharged-c-pia.png)

This is a project template for a scalable, high-performance, and sustainable API using FastAPI.

**Key Features**:
- Scalability: Designed to handle increasing loads by distributing the workload efficiently.
- High Performance: Optimized for speed and responsiveness to ensure quick data processing and retrieval.
- Sustainability: Built with best practices to ensure maintainability and long-term viability.


# Technologies Used in the Project

## 🚀 Main Technologies

| Technology   | Description                                                |
|--------------|-----------------------------------------------------------|
|  **FastAPI** | A modern and fast web framework for building APIs with Python 3.7+ based on standards like OpenAPI. |
| **SQLAlchemy** | A Python ORM that provides a powerful and efficient way to interact with databases. |
| **Pydantic** | A data validation and settings management library using Python type annotations. |
| **PostgreSQL** | An open-source relational database management system with an emphasis on extensibility and standards compliance. |
|  **Redis** | An in-memory data structure store, used as a database, cache, and message broker. |
| **Pytest** | A testing framework for Python that allows you to write simple and scalable test cases. |

## 🛠 Other Tools and Libraries

| Technology   | Description                                                |
|--------------|-----------------------------------------------------------|
| **Alembic** | A database migration tool for SQLAlchemy used to manage database schemas. |
| **Flake8** | A code analysis framework that combines several static analysis tools into one. |


## Setup

### Bash

You must execute chmod command for permissions:
```
chmod +x hooks/install 
chmod +x hooks/verify_tests
chmod +x run
```

Install the Git hooks:
```
./hooks/install
```

### Server

You need to copy and paste the file named config.sample.py:
```
cp config/config.sample.py config/config.py
```

Update the configuration to add your database:
```
DATABASE_URL = "postgresql+psycopg://youruser:yourpassword@localhost:5432/namedatabase"
```

You need to install dependencies:
```
python3 -m venv .venv
source .venv/bin/active
pip install -r requirements.txt
```

Start the backend server:
```
./run server
```

Execute the tests:
```
./run tests
```

Execute the coverage:
```
./run coverage
```

## Project Directory Structure

```
├── app                 # App Folder
│   ├── controllers     # Interface client - services
│   ├── domain          # Domain models and business logic
│   ├── repository      # Data access and persistence
│   └── schemas         # Pydantic models used for data validation
|       ├── requests    # Request models for data validation
|       └── responses   # Response models for data validation
│   ├── services        # business logic layer of the application
│   └── utils           # Utility functions 
├── config              # Contains configuration files
├── hooks               # Git hooks
├── migrations          # Configuration database migrations
├── routes              # Route definitions
├── tests               # All unit tests
├── requirements.txt    # Dependencies of project
└── main.py             # Main script of project
```
