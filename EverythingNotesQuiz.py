import random

# Title
title = r"""
 _____                     _   _     _                           _                          _     
|  ___|                   | | | |   (_)                         | |                        (_)    
| |____   _____ _ __ _   _| |_| |__  _ _ __   __ _   _ __   ___ | |_ ___  ___    __ _ _   _ _ ____
|  __\ \ / / _ \ '__| | | | __| '_ \| | '_ \ / _` | | '_ \ / _ \| __/ _ \/ __|  / _` | | | | |_  /
| |___\ V /  __/ |  | |_| | |_| | | | | | | | (_| | | | | | (_) | ||  __/\__ \ | (_| | |_| | |/ / 
\____/ \_/ \___|_|   \__, |\__|_| |_|_|_| |_|\__, | |_| |_|\___/ \__\___||___/  \__, |\__,_|_/___|
                      __/ |                   __/ |                                | |            
                     |___/                   |___/                                 |_|            
"""

# Quiz data based on your notes
quiz_data = [
    # Design Modelling
    {
        "question": "What is the primary purpose of design modelling?",
        "answer": "To create a working prototype using software development tools",
        "options": [
            "To create a working prototype using software development tools",
            "To write code for software applications",
            "To design user interfaces",
            "To test software for bugs"
        ],
        "explanation": "Design modelling focuses on creating a prototype by planning the system's structure, including conceptual and detailed design. It is not about writing code, designing user interfaces, or testing for bugs."
    },
    {
        "question": "Which of the following is NOT a key stage in design modelling?",
        "answer": "Debugging",
        "options": [
            "Conceptual design",
            "Detailed design",
            "Database design",
            "Debugging"
        ],
        "explanation": "Debugging is part of the testing phase, not design modelling. Design modelling involves conceptual design, detailed design, and database design, which are planning stages."
    },

    # Data Flow Diagrams (DFDs)
    {
        "question": "What does a Data Flow Diagram (DFD) represent?",
        "answer": "Processes that capture, manipulate, store, and distribute data",
        "options": [
            "The physical layout of a network",
            "Processes that capture, manipulate, store, and distribute data",
            "The hierarchy of employees in an organization",
            "The financial flow of a company"
        ],
        "explanation": "DFDs are graphical tools used to represent how data flows through a system, including processes, data stores, and external entities. They do not represent physical layouts, employee hierarchies, or financial flows."
    },
    {
        "question": "Which symbol in a DFD represents a function or activity?",
        "answer": "Process",
        "options": [
            "Data Flow",
            "Data Store",
            "Process",
            "Source/Sink"
        ],
        "explanation": "In DFDs, the 'Process' symbol represents a function or activity that manipulates data. Data Flow represents the movement of data, Data Store represents data at rest, and Source/Sink represents external entities."
    },

    # ASCII and Data Entry
    {
        "question": "What does ASCII stand for?",
        "answer": "American Standard Code for Information Interchange",
        "options": [
            "American Standard Code for Information Interchange",
            "Advanced System for Computer Information Interchange",
            "Automated Standard Code for Information Integration",
            "American System for Computer Information Integration"
        ],
        "explanation": "ASCII is a character encoding standard used to represent text in computers. It is widely used for data representation and communication between systems."
    },
    {
        "question": "Which of the following is NOT a common data type in data entry systems?",
        "answer": "Image",
        "options": [
            "Numeric",
            "Text",
            "Boolean",
            "Image"
        ],
        "explanation": "Common data types in data entry systems include numeric (e.g., integers, floats), text (e.g., strings), and Boolean (true/false). While images can be stored, they are not considered a basic data type in the context of data entry systems."
    },

    # Validation Methods
    {
        "question": "What does GIGO stand for?",
        "answer": "Garbage In Garbage Out",
        "options": [
            "Good Input Good Output",
            "Garbage In Garbage Out",
            "General Input General Output",
            "Global Input Global Output"
        ],
        "explanation": "GIGO emphasizes that incorrect input data leads to incorrect output. It highlights the importance of accurate data entry and validation to avoid useless or erroneous data."
    },
    {
        "question": "Which of the following is a key method to reduce data entry errors?",
        "answer": "Automation",
        "options": [
            "Manual data entry",
            "Automation",
            "Increasing the number of data entry personnel",
            "Reducing the amount of data entered"
        ],
        "explanation": "Automation reduces human errors in data entry by using software tools to validate and verify data, ensuring accuracy and consistency. Manual data entry is prone to errors, and increasing personnel or reducing data does not address the root cause of errors."
    },

    # Entity Relationship Diagrams (ERD)
    {
        "question": "What does cardinality in an ERD indicate?",
        "answer": "The type of relationship between tables",
        "options": [
            "The size of the database",
            "The type of relationship between tables",
            "The number of attributes in a table",
            "The number of records in a table"
        ],
        "explanation": "Cardinality defines how entities (tables) in a database are related, such as one-to-one, one-to-many, or many-to-many. It does not refer to the size of the database, the number of attributes, or the number of records."
    },
    {
        "question": "Which of the following is an example of a one-to-many relationship?",
        "answer": "Customer and Order",
        "options": [
            "Employee and Company Car",
            "Customer and Order",
            "Patient and Doctor",
            "Singer and Album"
        ],
        "explanation": "In a one-to-many relationship, one entity (e.g., Customer) can be associated with multiple instances of another entity (e.g., Orders). A customer can place many orders, but each order is associated with only one customer."
    },

    # Structured Query Language (SQL)
    {
        "question": "What is the primary purpose of SQL?",
        "answer": "To manage relational databases",
        "options": [
            "To design user interfaces",
            "To manage relational databases",
            "To create graphical visualizations",
            "To write operating systems"
        ],
        "explanation": "SQL is a programming language used to manage and manipulate relational databases. It is not used for designing user interfaces, creating visualizations, or writing operating systems."
    },
    {
        "question": "Which SQL command is used to retrieve data from a database?",
        "answer": "SELECT",
        "options": [
            "INSERT",
            "DELETE",
            "SELECT",
            "UPDATE"
        ],
        "explanation": "The SELECT command is used to retrieve data from a database. INSERT is used to add data, DELETE is used to remove data, and UPDATE is used to modify existing data."
    },

    # Data Visualization
    {
        "question": "Which of the following is NOT a common data visualization technique?",
        "answer": "SQL queries",
        "options": [
            "Line graphs",
            "Histograms",
            "Pie charts",
            "SQL queries"
        ],
        "explanation": "SQL queries are used to retrieve data from databases, not to visualize data. Line graphs, histograms, and pie charts are common data visualization techniques."
    },
    {
        "question": "What is the primary purpose of a heat map?",
        "answer": "To represent data density using color gradients",
        "options": [
            "To show geographical data",
            "To represent data density using color gradients",
            "To display hierarchical data",
            "To compare categorical data"
        ],
        "explanation": "Heat maps use color gradients to represent data density, making it easy to identify areas of high or low activity. They are not primarily used for geographical data, hierarchical data, or categorical comparisons."
    },

    # Cybersecurity
    {
        "question": "What is the primary purpose of a firewall?",
        "answer": "To monitor and control inbound/outbound traffic",
        "options": [
            "To store data",
            "To monitor and control inbound/outbound traffic",
            "To create virtual private networks",
            "To encrypt data"
        ],
        "explanation": "A firewall is a security device that monitors and controls network traffic based on predefined rules. It is not used to store data, create VPNs, or encrypt data."
    },
    {
        "question": "Which of the following is a type of penetration testing?",
        "answer": "All of the above",
        "options": [
            "Network Penetration Testing",
            "Social Engineering Testing",
            "Physical Penetration Testing",
            "All of the above"
        ],
        "explanation": "Penetration testing includes various types, such as network penetration testing, social engineering testing, and physical penetration testing, to identify vulnerabilities in different areas of a system."
    },

    # Root Cause Analysis (RCA)
    {
        "question": "What is the first step in Root Cause Analysis (RCA)?",
        "answer": "Define the Problem",
        "options": [
            "Collect Data",
            "Define the Problem",
            "Identify Root Causes",
            "Implement Changes"
        ],
        "explanation": "The first step in RCA is to clearly define the problem. Without a clear understanding of the problem, it is impossible to identify its root causes or implement solutions."
    },
    {
        "question": "Which technique involves repeatedly asking 'Why?' to drill down to the root cause of a problem?",
        "answer": "5 Whys",
        "options": [
            "Pareto Analysis",
            "Fishbone Diagram",
            "5 Whys",
            "SWOT Analysis"
        ],
        "explanation": "The 5 Whys technique involves asking 'Why?' multiple times to uncover the root cause of a problem. Pareto Analysis, Fishbone Diagrams, and SWOT Analysis are other problem-solving tools but do not use this specific approach."
    },

    # Testing Methods
    {
        "question": "Which type of testing focuses on the internal structure and logic of an application?",
        "answer": "White-Box Testing",
        "options": [
            "Black-Box Testing",
            "White-Box Testing",
            "Usability Testing",
            "Penetration Testing"
        ],
        "explanation": "White-box testing focuses on the internal structure and logic of an application, requiring knowledge of the code. Black-box testing focuses on functionality without knowledge of the internal code."
    },
    {
        "question": "What is the purpose of a test plan?",
        "answer": "To document the approach, resources, and schedule for testing",
        "options": [
            "To document the approach, resources, and schedule for testing",
            "To write code for the application",
            "To design the user interface",
            "To manage the database"
        ],
        "explanation": "A test plan outlines the strategy, resources, and timeline for testing. It is not used for writing code, designing interfaces, or managing databases."
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

    for i, question in enumerate(data[:10], 1):  # Only take 10 questions
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

    print(f"\nYour final score is {score}/10")

    # Display revision feedback
    if incorrect_answers:
        print("\nYou need to revise the following topics:")
        for question in incorrect_answers:
            print(f"- {question}")
    else:
        print("\nGreat job! You answered all questions correctly.")

if __name__ == "__main__":
    print(title)
    print("Welcome to the Comprehensive Quiz!\n")
    shuffled_quiz = shuffle_quiz(quiz_data)
    take_quiz(shuffled_quiz)

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
