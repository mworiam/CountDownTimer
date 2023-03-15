import tkinter as tk

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

questions = [
    Question("What is the capital of Kenya?", "Nairobi"),
    Question("What is the highest mountain in Africa?", "Mount Kilimanjaro"),
    Question("Who was the first president of Kenya?", "Mzee Jomo Kenyatta"),
    Question("Which is the smallest country in Africa?", "Seychelles"),
    Question("What is the largest ocean in the world?", "Pacific Ocean")
]

class Game:
    def __init__(self, master):
        self.master = master
        master.title("Question and Answer Game")

        self.label = tk.Label(master, text="Welcome to the game!")
        self.label.pack()

        self.score = 0
        self.question_number = 0

        self.ask_question()

    def ask_question(self):
        question = questions[self.question_number]
        self.prompt = tk.Label(self.master, text=question.prompt)
        self.prompt.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.master, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        user_answer = self.answer_entry.get().lower()
        correct_answer = questions[self.question_number].answer.lower()
        if user_answer == correct_answer:
            self.score += 1
            self.label.config(text="Correct! Your score is " + str(self.score))
        else:
            self.label.config(text="Incorrect. The correct answer was " + correct_answer)

        self.question_number += 1
        if self.question_number < len(questions):
            self.ask_question()
        else:
            self.label.config(text="Game over. Your final score is " + str(self.score))

root = tk.Tk()
game = Game(root)
root.mainloop()
