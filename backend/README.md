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
psql -U <postgres_username> trivia < trivia.psql
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
    "1" : "Science",
    "2" : "Art",
    "3" : "Geography",
    "4" : "History",
    "5" : "Entertainment",
    "6" : "Sports"
}
```

### /questions

**Method**: GET

*Arguments*: page
Default is 1

*Example:*
/questions?page=1

- Fetches a dictionary within the following items:
    - A dictionary of all the categories exactly like the `/categories` endpoint would return it. 
    - A list of the questions within that page, the default page being 1 if none is supplied. There is a maximum of 10 questions per page. Each question being returned as a dictionary of key:value parameters within.
        - question: The question string 
        - answer: The answer string
        - id: The question id
        - category: The category of the question
        - difficulty: The difficulty level of the question
    - A boolean value of `true` indicating that the operation was sucessful
    - The total number of all questions within the database.

***sample response***
```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",        
    "4": "History",
    "5": "Entertainment",    
    "6": "Sports"
  },
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"       
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 23
}
```

**Method**: POST

- Receives a JSON body containing key value pairs of the `question`, `answer`, `difficulty` and `category` and adds the new question to the database.
- Returns a dictionary containing:
    - A success value of `True`
    - A dictionary containing the details of the newly posted question.

***sample `curl` request***
```sh
curl -d '{"question":"test","answer":"test","difficulty":1,"category":1}' -H 'Content-Type: appli 
cation/json' -X "POST" http://localhost:5000/questions
```

***sample response***
```json
{
  "question": {
    "answer": "test",
    "category": 1,
    "difficulty": 1,
    "id": 36,
    "question": "test"
  },
  "success": true
}
```
**Method**: DELETE
Endpoint: `/questions/<int:question_id>` 

- Deletes the question row corresponding to the question id supplied.
- Returns a dictionary containing a `success` value of `True` and the id of the deleted question with a value of `deleted`. 

***sample `curl`request***
```sh
curl -X "DELETE" http://localhost:5000/questions/1
```

***sample response***
```json
{
    "success": true,
    "deleted": 1
}
```

### /categories/<int:category_id>/questions

**Method**: GET

- Returns all questions within the category Id specified.

***sample `curl`request***
```sh
curl http://localhost:5000/categories/1/questions
```

***sample response***
```json
{
  "current_category": 1,
  "questions": [
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

### /searchquestions

**Method**: POST

- Takes a JSON request containing one key:value pair of the `searchTerm` and the search term string
- Return all questions with the search term within the name. The search is case insensitive

***sample `curl` request***
```sh
curl -X "POST" -d '{"searchTerm":"test"}' -H 'Content-Type: application/json' http://localhost:50 
00/searchquestions
```

***sample response***
```json
{
  "questions": [
    {
      "answer": "test",
      "category": 1,
      "difficulty": 1,
      "id": 36,
      "question": "test"
    }
  ],
  "success": true,
  "total_questions": 1
}
```
## Testing
To run the tests, make sure the terminal is currently active within the root of the `backend` folder and then run: 
```
dropdb trivia_test
createdb trivia_test
psql -U <postgres_username> trivia_test < trivia.psql
python test_flaskr.py
```