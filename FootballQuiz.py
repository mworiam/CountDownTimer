#Quiz game bsed on my favourite team and the best team in the world, REAL MADRID CF

questions = ("Who is Real Madrid's all time top goal scorer?: ",
             "How many Champions League titles have Real Madrid won?: ",
             "Who has the most appearances for Real Madrid?: ",
             "In which Stadium was La Decima won?: ",
             "Which Real Madrid Manager has the most wins?: ")

options = (("A. Raul Gonzalez", "B. Karim Benzema", "C. Cristiano Ronaldo", "D. Alfredo DiStefano"),
            ("A. 6", "B. 13", "C. 10", "D. 14"),
            ("A. Raul Gonzalez", "B. Iker Casillas", "C. Sergio Ramos", "D. Karim Benzema"),
            ("A. Estadio Da Luz, Lisbon", "B. San Siro, Milan", "C. Parc De France, Paris", "D. Millenium Stadium, Cardiff"),
            ("A. Zinadine Zidane", "B. Miguel Munoz", "C. Carlo Ancelotti", "D. Jose Mourinho"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("********************")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("********************")
print("       RESULTS        ")
print("********************")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")