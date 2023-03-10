
from flask import Flask,jsonify,request
from __init__ import app, db
from flask import request
# The purpose of this database is to be used as API and have all the questions along with points and answers
questions = [
    {
        'category': 'UFC',
        'question': 'Who won the Welterweight title from Tyron Woodley',
        'answer': 'Kamaru Usman',
        'points' : '100'
    },
    {
        'category': 'UFC',
        'question': 'Who has most title defenses of all time?',
        'answer': 'Demetrius Johnson',
        'points' : '200'
    },
    {    
        'category': 'UFC',
        'question': 'Who was the first UFC Champ from England',
        'answer': 'Michael Bisping',
        'points' : '300'
    },
    {
        'category': 'UFC',
        'question': 'Who beat Connor Mcgregor at UFC 229?',
        'answer': 'Khabib',
        'points' : '400'
    },
    
    {
        'category': 'UFC',
        'question': 'Who has most wins in the UFC all time before a champsionship fight?',
        'answer': 'Jorge Masvidal',
        'points' : '500'
    },
    {
        'category': 'NFL',
        'question': 'Which round was Tom Brady Drafted in?',
        'answer': '6th',
        'points' : '100'
    },
    {
        'category': 'NFL',
        'question': 'Which NFL player has most rings?',
        'answer': 'Tom Brady',
        'points' : '200'
    },
    {    
        'category': 'NFL',
        'question': 'Which team won the first superbowl',
        'answer': 'Packers',
        'points' : '300'
    },
    {
        'category': 'NFL',
        'question': 'Which player retired during halftime',
        'answer': 'Vontae Davis',
        'points' : '400'
    },
    
    {
        'category': 'NFL',
        'question': 'Which overall pick was traded for AJ Brown',
        'answer': '18th',
        'points' : '500'
    },
    {
        'category': 'NBA',
        'question': 'Which team did Kareem Abdul Jabar play for as a rookie',
        'answer': 'Bucks',
        'points' : '100'
    },
    {
        'category': 'NBA',
        'question': 'Who leads in all time assits',
        'answer': 'John Stockton',
        'points' : '200'
    },
    {    
        'category': 'NBA',
        'question': 'When did Lebron leave Cleveland the first time',
        'answer': '2010',
        'points' : '300'
    },
    {
        'category': 'NBA',
        'question': 'Who was the most recent back to back MVP winner',
        'answer': 'Nikola Jokic',
        'points' : '400'
    },
    
    {
        'category': 'NBA',
        'question': 'How many career 3pts has Steph Curry made',
        'answer': '3302',
        'points' : '500'
    },
    {
        'category': 'MLB',
        'question': 'Who has the most home runs in MLB history',
        'answer': 'Barry Bonds',
        'points' : '100'
    },
    {
        'category': 'MLB',
        'question': 'Who has the most strikeouts in MLB history',
        'answer': 'Nolan Ryan',
        'points' : '200'
    },
    {    
        'category': 'MLB',
        'question': 'Who is the oldest Major Leaguer ever to hit a home run?',
        'answer': 'Julio Franco',
        'points' : '300'
    },
    {
        'category': 'MLB',
        'question': 'How many home runs did Aaron Judge have when he broke the record',
        'answer': '62',
        'points' : '400'
    },
    
    {
        'category': 'MLB',
        'question': 'How many intentional walks did Roger Maris get in his 61 home run season?',
        'answer': '0',
        'points' : '500'
    },
    {
        'category': 'Soccer',
        'question': 'Which team has the most LaLiga titles?',
        'answer': 'Real Madrid',
        'points' : '100'
    },
    {
        'category': 'Soccer',
        'question': 'How many world cups has Ronaldo Won',
        'answer': '0',
        'points' : '200'
    },
    {    
        'category': 'Soccer',
        'question': 'What year did Vinicius Jr. Transfer to Real Madrid',
        'answer': '2017',
        'points' : '300'
    },
    {
        'category': 'Soccer',
        'question': 'Which club is known as the "Red Devils" ?',
        'answer': 'Manchester United',
        'points' : '400'
    },
    
    {
        'category': 'Soccer',
        'question': 'Who won the first Ballon dOR?',
        'answer': 'Stanley Matthews',
        'points' : '500'
    },
]
#This is what I will use to have all the questions using GET COMMAND
@app.route("/questions", methods=["GET"])
def get_questions():
    return jsonify(questions)
#This is used to check the answer with the Post Method and set up the query for the questions
# This checks the answer if its correct or not, and gives the response to user to tell them they were wrong/right
@app.route("/api/check_answer", methods=["POST"])
def check_answer():
    category = request.args.get('category')
    points = request.args.get('points')
    print(category,points)
    print(request.get_json())
    answer = request.get_json()["answer"]
    for question in questions:
        if category == question["category"] and points == question["points"]:
            if answer == question["answer"]:
                return jsonify({"result": "Correct"})
    return jsonify({"result": "Incorrect"})

# This is used to give the questions for user to answer
# THe way I dealt with errors the API may have is by giving a message if the query cannot be found to give a question
@app.route('/api/jeopardy')
def data():
    category = request.args.get('category')
    points = request.args.get('points')
    print(category,points)
    # Iterates through questions
    for question in questions:
        if category == question["category"] and points == question["points"]:
            response = {
                "question": question["question"]
            }
            return jsonify(response)
    return '{ "Question": "Not found" }'



# This is used to delete questions from the list of questions
@app.route("/api/delete_question", methods=["DELETE"])
def delete():
    category = request.args.get('category')
    points = request.args.get('points')
    print(category,points)
    for index, question in enumerate(questions):
        if category == question["category"] and points == question["points"]:
            del questions[index]
            response = {
                "message": "Delete Successful"
            }
            return jsonify(response)
    return '{ "message": "Failed To Find Question" }'

if __name__ == '__main__':
    app.run()

# This is my class to create the database with all the questions, answers and points
class Jeopardy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Text)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
    points = db.Column(db.Integer)
    def __repr__(self):
        return f'Question: {self.question}'

db.drop_all()
db.create_all()

# The use of this function was to make the database and then fill it up with the columns that I want,
#which is category,question,points,and answer
def makedb():
    for question in questions:
        question = Jeopardy(category=question["category"],points=int(question["points"]),answer=question["answer"],question=question["question"])
        db.session.add(question)
    db.session.commit()
makedb()
#print(Jeopardy.query.all())