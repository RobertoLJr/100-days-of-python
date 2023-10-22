from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Populate a question bank with questions from question_data
question_bank = []
for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)


quiz = QuizBrain(question_bank)

while quiz.has_questions_remaining():
    quiz.next_question()

print(f"You've completed the quiz.\nYour final score was {quiz.score}/{quiz.question_number}.")
