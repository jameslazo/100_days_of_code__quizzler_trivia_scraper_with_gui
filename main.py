from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# def true_button():
#     global user_answer
#     user_answer = "True"
#
#
# def false_button():
#     global user_answer
#     user_answer = "False"
#
# def check_user_answer():
#     return user_answer


user_answer = None
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)
# quiz_ui.true_bu.config(command=true_button)
# quiz_ui.false_bu.config(command=false_button)
# quiz.check_answer()





# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
