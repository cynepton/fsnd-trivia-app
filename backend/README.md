# Full Stack Trivia API Backend

## Getting Started

The Backend is a flask application making use of `flask`, `flask_sqlalchemy` and `flask_cors`.

### Setting up the database
The database used for this project is [PostgreSQL](https://www.postgresql.org/download/), although, thanks to [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/), the syntax should work fine with other database dialects, postgreSQL is advised to avoid any unforseen errors. 
Create two new postgres databases, one titled `trivia` and the other `trivia_test`, for the application's unittests. 

In the [models.py](models.py) file, adjust the database configuration for the main database, and in the [test_flaskr.py](test_flaskr.py) file, adjust the necessary configuration values for the test database file.

**Note**: *The database names `trivia` and `trivia_test` are arbitrary and can be renamed. 

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Endpoints

- [GET `/categories`](https://github.com/cynepton/fsnd-trivia-app/tree/dev/backend#categories)
- GET `/questions`
- POST `/questions`
- DELETE `/questions/<int:question_id>`
- GET `/categories/<int:category_id>/questions`
- POST `/quizzes`

### /categories

**Method**: GET

- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs.

***sample response***
```json
{
    '1' : "Science",
    '2' : "Art",
    '3' : "Geography",
    '4' : "History",
    '5' : "Entertainment",
    '6' : "Sports"
}
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```