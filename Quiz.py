import time


class Question:
    def __init__(self, question_text, choices):
        self.question_text = question_text
        self.choices = choices

    def display_question(self):
        print(self.question_text)
        for index, choice in enumerate(self.choices, start=1):
            print(f"{index}) {choice}")

def load_questions_from_file(filename):
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            question_text = data[0]
            choices = data[1:]
            questions.append(Question(question_text, choices))
    return questions

def load_answers_from_file(filename):
    answers = []
    with open(filename, 'r') as file:
        for line in file:
            answer = line.strip()
            answers.append(answer)
    return answers

def run_game():
    questions = load_questions_from_file("questions.txt")
    answers = load_answers_from_file("answers.txt")
    valid_answers = ['A', 'B', 'C', 'D']

    score = 0
    correct_answers = 0
    print("*** Welcome to the quiz game. Test your knowledge with us. Good luck! ***")
    print("*** You get 1 point for each correct answer and 0.65 deducted for incorrect ones. ***")
    print("*** Now loading the questions list. Please wait... ***")
    time.sleep(2)
    
    for i, question in enumerate(questions):
        question.display_question()
        user_answer = input(f"Enter your answer for question {i+1}:").upper()
        while user_answer not in valid_answers:
            print("Invalid answer. Please choose A, B, C, or D")
            user_answer = input(f"Enter your answer for question {i+1}:").upper()
        if answers[i] == user_answer:
            print("Correct!")
            score += 1
            correct_answers += 1
        else:
            print("Incorrect!")
            score -= 0.65
        print(f"Your current score is {score}")
    if correct_answers == 4:
        print("Excellent!")
    elif correct_answers == 3:
        print("Good!")
    elif correct_answers == 2:
        print("So so...")
    else:
        print("Very bad! :(")
    
    print("Quiz complete!")
    print(f"Your final score is {score}")
    print(f"You've answered {correct_answers} out of {len(questions)} questions correctly.")

if __name__ == "__main__":
    run_game()

