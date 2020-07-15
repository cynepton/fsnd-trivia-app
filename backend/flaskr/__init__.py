import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_books(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    '''
    @TODO: Set up CORS. Allow '*' for origins.
    Delete the sample route after completing the TODOs
    '''
    #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    '''
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    '''
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    '''
    @app.route("/categories")
    def get_all_categories():
        categories = {}
        all_categories = Category.query.order_by(Category.id).all()
        for each_category in all_categories:
            categories[each_category.id] = each_category.type
        return jsonify({
            "success": True,
            "categories": categories
        })

    '''
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories. 

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page,
    and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    '''
    @app.route("/questions")
    def get_all_questions():
        selection = Question.query.order_by(Question.id).all()
        total_questions = len(selection)
        current_questions = paginate_books(request, selection)

        if len(current_questions) == 0:
            abort(404)

        # categories
        categories = {}
        all_categories = Category.query.order_by(Category.id).all()
        for each_category in all_categories:
            categories[each_category.id] = each_category.type

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': total_questions,
            'categories': categories,
            # 'current_category': None
        })

    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 

    TEST: When you click the trash icon next to a question, 
    the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            # leng = len(question)
            # req_len = 1
            # print(question, leng, req_len)
            print(question)
            if question is None:
                abort(404)
            else:
                print('question contains a row')
                question.delete()
                print('question delete works')
                return jsonify({
                    'success': True,
                    'deleted': question_id
                })

        except Exception:
            print('question delete failed completely')
            abort(400)

    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    @app.route('/questions', methods=['POST'])
    def post_question():
        new_question = request.get_json()
        question = new_question.get('question')
        answer = new_question.get('answer')
        difficulty = new_question.get('difficulty')
        category = new_question.get('category')
        if question is None:
            abort(400)
        if answer is None:
            abort(400)
        if difficulty is None:
            abort(400)
        if category is None:
            abort(400)
        try:
            new_entry = Question(question, answer, category, difficulty)
            new_entry.insert()
            return jsonify({
                'success': True,
                'question': new_entry.format()
            })
        except Exception:
            abort(400)
    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''
    @app.route('/searchquestions', methods=['POST'])
    def search_quetions():
        search_body = request.get_json()
        if search_body is None:
            print('No search term received')
            abort(400)
        search_term = search_body.get('searchTerm')
        null = ''
        if search_term == null:
            print('searchTerm is empty or couldnt read search term')
            abort(406)
        else:
            print('searchTerm is ' + search_term)
            questions = Question.query.filter(Question.question.ilike('%' + search_term + '%'))
            question_list = [question.format() for question in questions]
            print(question_list)
            return jsonify({
                'success': True,
                'total_questions': len(question_list),
                'questions': question_list
            })

    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''
    @app.route('/categories/<int:category_id>/questions')
    def get_by_category(category_id):
        try:
            print(category_id)
            selection = Question.query.filter(Question.category == category_id).all()
            question_list = [question.format() for question in selection]
            total_questions = len(question_list)
            print(question_list)

            return jsonify({
                'success': True,
                'questions': question_list,
                'total_questions': total_questions,
                'current_category': category_id
            })
        except Exception:
            abort(400)


    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''
    @app.route('/quizzes', methods=['POST'])
    def post_quizzes():
        body_data = request.get_json()
        previous_questions = body_data.get('previous_questions')
        quiz_category = body_data.get('quiz_category')
        category_id = quiz_category.get('id')
        print('___________________________________________________')
        print('Previous questions')
        print(previous_questions)
        print('___________________________________________________')
        pq_len = len(previous_questions)

        if pq_len == 0:
            print('-----------------------------------------------')
            print('First Question')
            print('-----------------------------------------------')
            if category_id == 0:
                next_question = Question.query.first()
            else:
                next_question = Question.query.filter(Question.category == category_id).first()
        else:
            if category_id == 0:
                all_questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
                if len(all_questions) == 0:
                    print('-----------------------------------------------')
                    print('No more Questions')
                    print('-----------------------------------------------')
                    return jsonify({
                        'success': True,
                        'question': False
                    })
                else:
                    next_question = all_questions[0]
            else:
                all_questions = Question.query.filter(Question.id.notin_(previous_questions), Question.category == category_id).all()
                if len(all_questions) == 0:
                    print('-----------------------------------------------')
                    print('No more Questions')
                    print('-----------------------------------------------')
                    return jsonify({
                        'success': True,
                        'question': False
                    })
                else:
                    next_question = all_questions[0]
                    
        print('-----------------------------------------------')
        print(next_question.format())
        print('-----------------------------------------------')
        return jsonify({
            'success': True,
            'question': next_question.format()
        })

    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    @app.errorhandler(400)
    def not_found(error):
        return jsonify({
        'success': False,
        'error': 400,
        'message': 'Bad Request'
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
        'success': False,
        'error': 404,
        'message': 'Resource not found'
        }), 404

    @app.errorhandler(406)
    def not_found(error):
        return jsonify({
        'success': False,
        'error': 406,
        'message': 'Not Acceptable'
        }), 406

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
        'success': False,
        'error': 422,
        'message': 'unprocessable'
        }), 422
    

    return app