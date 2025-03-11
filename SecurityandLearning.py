import random

# Title
title = r"""
 _____                      _ _               _                           _                           _            
/  ___|                    (_) |          _  | |                         (_)                         | |           
\ `--.  ___  ___ _   _ _ __ _| |_ _   _ _| |_| |     ___  __ _ _ __ _ __  _ _ __   __ _   _ __   ___ | |_ ___  ___ 
 `--. \/ _ \/ __| | | | '__| | __| | | |_   _| |    / _ \/ _` | '__| '_ \| | '_ \ / _` | | '_ \ / _ \| __/ _ \/ __|
/\__/ /  __/ (__| |_| | |  | | |_| |_| | |_| | |___|  __/ (_| | |  | | | | | | | | (_| | | | | | (_) | ||  __/\__ \
\____/ \___|\___|\__,_|_|  |_|\__|\__, |     \_____/\___|\__,_|_|  |_| |_|_|_| |_|\__, | |_| |_|\___/ \__\___||___/
                                   __/ |                                           __/ |                           
                                  |___/                                           |___/                           
"""

# Quiz data based on your topics
quiz_data = [
    {
        "question": "What is the primary purpose of the GDPR?",
        "answer": "To protect personal data and privacy",
        "options": [
            "To regulate internet usage",
            "To protect personal data and privacy",
            "To enforce cybersecurity laws",
            "To monitor corporate finances"
        ],
        "explanation": "The GDPR (General Data Protection Regulation) is designed to protect the personal data and privacy of individuals within the European Union."
    },
    {
        "question": "Which of the following is NOT a type of penetration testing?",
        "answer": "Financial auditing",
        "options": [
            "Internal network testing",
            "Application testing",
            "IoT/OT testing",
            "Financial auditing"
        ],
        "explanation": "Financial auditing is not a type of penetration testing. Penetration testing focuses on identifying vulnerabilities in systems, networks, or applications."
    },
    {
        "question": "What does the Computer Misuse Act 1990 primarily address?",
        "answer": "Unauthorized access to computer systems",
        "options": [
            "Data visualization techniques",
            "Unauthorized access to computer systems",
            "Copyright infringement",
            "Email spam reduction"
        ],
        "explanation": "The Computer Misuse Act 1990 primarily addresses unauthorized access to computer systems, including hacking and other forms of cybercrime."
    },
    {
        "question": "What is the purpose of non-functional testing?",
        "answer": "To evaluate security, performance, and usability",
        "options": [
            "To test software functionality",
            "To evaluate security, performance, and usability",
            "To design user interfaces",
            "To analyze data formats"
        ],
        "explanation": "Non-functional testing evaluates aspects like security, performance, and usability, rather than specific functionalities of the software."
    },
    {
        "question": "Which of the following is a key concept in SQL?",
        "answer": "Data normalization",
        "options": [
            "Data normalization",
            "Data visualization",
            "Data encryption",
            "Data entry validation"
        ],
        "explanation": "Data normalization is a key concept in SQL, which involves organizing data to reduce redundancy and improve data integrity."
    },
    {
        "question": "What is the first stage of Kolb’s Experiential Learning Cycle?",
        "answer": "Concrete experience",
        "options": [
            "Abstract conceptualization",
            "Reflective observation",
            "Concrete experience",
            "Active experimentation"
        ],
        "explanation": "The first stage of Kolb’s Experiential Learning Cycle is 'Concrete Experience,' where the learner engages in a new experience or interprets an existing experience."
    },
    {
        "question": "What is the primary goal of design thinking?",
        "answer": "To focus on end-user needs and iterative problem-solving",
        "options": [
            "To enforce data protection laws",
            "To focus on end-user needs and iterative problem-solving",
            "To simulate cyberattacks",
            "To create data visualizations"
        ],
        "explanation": "The primary goal of design thinking is to focus on end-user needs and use iterative problem-solving to create effective solutions."
    },
    {
        "question": "Which of the following is a common misuse of the internet?",
        "answer": "Eavesdropping",
        "options": [
            "Eavesdropping",
            "Data normalization",
            "Reflective learning",
            "Design modelling"
        ],
        "explanation": "Eavesdropping is a common misuse of the internet, where unauthorized parties intercept private communications."
    }
]

def shuffle_quiz(data):
    """Shuffle questions and answer options."""
    random.shuffle(data)
    for question in data:
        random.shuffle(question["options"])
    return data

def take_quiz(data):
    """Present the quiz to the user, provide explanations, and track correct/incorrect answers."""
    score = 0
    correct_answers = []
    incorrect_answers = []

    for i, question in enumerate(data, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question['options'], 1):
            print(f"{j}. {option}")
        user_answer = input("Your answer (enter the number): ")
        if question['options'][int(user_answer) - 1] == question['answer']:
            print("Correct!")
            print(f"Explanation: {question['explanation']}\n")
            score += 1
            correct_answers.append(question['question'])
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")
            print(f"Explanation: {question['explanation']}\n")
            incorrect_answers.append(question['question'])

    print(f"\nYour final score is {score}/{len(data)}")

    # Display revision feedback
    if incorrect_answers:
        print("\nYou need to revise the following topics:")
        for question in incorrect_answers:
            print(f"- {question}")
    else:
        print("\nGreat job! You answered all questions correctly.")

    # Ask if the user wants to retake the quiz
    retake = input("\nWould you like to retake the quiz? (y/n): ").strip().lower()
    if retake == 'y':
        take_quiz(shuffle_quiz(quiz_data))
    else:
        print("\nThank you for taking the quiz. Goodbye!")

if __name__ == "__main__":
    print(title)
    print("Welcome to the Security and Learning Quiz!\n")
    shuffled_quiz = shuffle_quiz(quiz_data)
    take_quiz(shuffled_quiz)
