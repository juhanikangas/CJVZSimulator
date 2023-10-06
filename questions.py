import random

def question():
    question = questions[0]
    # question = questions[random.randint(0, len(questions))]
    answers = question["answers"].copy()
    print(question["question"])
    for i in range(len(answers)):
        random_index = random.randint(0, len(answers) - 1)
        print(answers[random_index])
        answers.pop(random_index)




questions = [
    {"question": "Is the Boeing 747 often referred to as the 'Queen of the Skies'?", "answers": ["Yes", "No"], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""},
    {"question": "", "answers": ["", ""], "difficulty": ""}
]

question()
