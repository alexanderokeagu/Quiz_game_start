from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for items in question_data:
    questions = items["text"]
    answers = items["answer"]
    new_question = Question(questions,answers)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"your final score is {quiz.score}/{quiz.question_number}")
