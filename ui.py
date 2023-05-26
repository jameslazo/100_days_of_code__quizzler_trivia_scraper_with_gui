from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Ariel", 18, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        # self.canvas.config()
        self.canvas = Canvas(width=300, height=250, bg="white", borderwidth=0, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            fill=THEME_COLOR,
            font=FONT,
            width=280
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_bu = Button(
            image=true_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.user_answers_true
        )
        self.true_bu.grid(column=0, row=2)

        false_img = PhotoImage(file="images/false.png")
        self.false_bu = Button(
            image=false_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.user_answers_false
        )
        self.false_bu.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_bu.config(state="disabled")
            self.false_bu.config(state="disabled")

    def user_answers_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def user_answers_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

