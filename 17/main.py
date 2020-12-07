from quiz_game import Game
from question import Question
from data import question_data
import requests
import html


def generate_questions(data):
    questions = []
    for element in data["results"]:
        question = Question(html.unescape(
            element["question"]), element["correct_answer"])
        questions.append(question)
    return questions


def get_question_data():
    q_num = int(
        input("How many questions are you ready to answer? Enter a number: ").strip())
    response = requests.get(
        "https://opentdb.com/api.php?amount={}&type=boolean".format(q_num))
    return response.json()


def main():
    data = get_question_data()
    quiz = generate_questions(data)
    game = Game(quiz)
    game.start()


if __name__ == "__main__":
    main()
