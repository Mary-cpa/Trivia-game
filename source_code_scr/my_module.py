import requests
import random

def fetch_questions(amount=10, category=9, difficulty="easy"):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    data = response.json()
    return data['results']

def format_question(question_data):
    question = question_data['question']
    correct_answer = question_data['correct_answer']
    incorrect_answers = question_data['incorrect_answers']

    # Mix correct and incorrect answers
    all_answers = incorrect_answers + [correct_answer]
    random.shuffle(all_answers)

    return {
        "question": question,
        "correct_answer": correct_answer,
        "options": all_answers
    }

def main():
    questions = fetch_questions()
    score = 0

    for i, q in enumerate(questions):
        formatted_q = format_question(q)
        print(f"\nQuestion {i+1}: {formatted_q['question']}")
        for idx, option in enumerate(formatted_q['options']):
            print(f"{chr(ord('A') + idx)}. {option}")

        answer = input("\nYour answer (A-D): ").upper()
        if formatted_q['options'][ord(answer) - ord('A')] == formatted_q['correct_answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {formatted_q['correct_answer']}")

    print(f"\nYour final score is: {score}/{len(questions)}")


if __name__ == "__main__":
    main()
