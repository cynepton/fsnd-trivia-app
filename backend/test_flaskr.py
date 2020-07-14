import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('cynepton', 'cynepton',  'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {
            'question': 'What is Batman Beyonds secret Identity',
            'answer': 'Terry Mcginnis',
            'difficulty': 3,
            'category': 5
        }
        self.search_term = {
            'searchTerm': 'what'
        }

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    '''
    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        print('---------get all categories test response-----------')
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertGreaterEqual(len(data['categories']), 0)
    
    def test_get_paginated_questions(self):
        res = self.client().get('/questions?page=1')
        data = json.loads(res.data)

        print('---------get paginated questions test response-----------')
        print(data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['questions'], list)
        self.assertLessEqual(len(data['questions']), 10)
        self.assertIsInstance(data['total_questions'], int)
        self.assertIsInstance(data['categories'], dict)

    def test_404_error_requesting_questions_beyond_valid_page(self):
        res = self.client().get('/questions?page=100')
        data = json.loads(res.data)

        print('---------get paginated questions test error 404-----------')
        print(data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['error'], 404)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Resource not found')
    
    
    def test_delete_question_by_id(self):
        res = self.client().delete('/questions/2')
        data = json.loads(res.data)

        print('---------delete a question test -----------------------')
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(data['deleted'], 2)
    
    def test_delete_question_by_id_not_existing(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)

        print('---------delete a question test error 404 -----------------------')
        print(data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Bad Request')

    def test_post_new_question(self):
        question = self.new_question

        res = self.client().post('/questions', json=question)
        data = json.loads(res.data)
        print('---------Posted a new question -----------------------')
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['question'], dict)

    def test_post_new_question_without_content(self):

        res = self.client().post('/questions', json={})
        data = json.loads(res.data)
        print('---------Posted a new question without content-----------------------')
        print(data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Bad Request')

    def test_search_for_question(self):
        search_term = self.search_term

        res = self.client().post('/searchquestions', json=search_term)
        data = json.loads(res.data)
        print('---------Searched for a question -----------------------')
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
    
    def test_search_for_question_with_empty_string(self):
        search_term = {
            'searchTerm': ''
        }

        res = self.client().post('/searchquestions', json=search_term)
        data = json.loads(res.data)
        print('---------Searched for a question with an empty string -----------------------')
        print(data)

        self.assertEqual(res.status_code, 406)
        self.assertEqual(data['error'], 406)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Not Acceptable')

    
    def test_search_for_question_with_no_content(self):

        res = self.client().post('/searchquestions')
        data = json.loads(res.data)
        print('---------Searched for a question with no content -----------------------')
        print(data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['error'], 400)
        self.assertFalse(data['success'])
        self.assertEqual(data['message'], 'Bad Request')

    def test_get_questions_by_category(self):

        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        print('--------- Get questions by category -----------------------')
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(data['current_category'], 1)
    '''

    def test_get_questions_by_category(self):

        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        print('--------- Get questions by category -----------------------')
        print(data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertIsInstance(data['questions'], list)
        self.assertIsInstance(data['total_questions'], int)
        self.assertEqual(data['current_category'], 1)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()