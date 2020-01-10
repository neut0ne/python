from random import choice

questions = [
    "Why is the sky blue? : ",
    "What do babies come from? : ",
    "Why do you tie your shoes? : ",
    ]

question = choice(questions)
answer = input(question.strip().lower()

    while answer != "just because!":
        answer = input("Why? : ").strip().lower()

print("Oh... Okay.")
