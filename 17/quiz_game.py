from player import Player


class Game:

    def __init__(self, quiz):
        self.player = Player()
        self.quiz = quiz

    def get_user_answer(self, question):
        text = question.get_text() + " (True/False): "
        answer = input(text).strip()
        return answer

    def check_answer(self, answer, question):
        correct_answer = question.get_correct_answer()
        return answer == correct_answer, correct_answer

    def get_result_message(self, is_correct, correct_answer):
        if is_correct:
            return "You got it right!\nThe correct answer was: {}.".format(correct_answer)
        return "That's wrong\nThe correct answer was: {}.".format(correct_answer)

    def get_score_message(self):
        return "Your current score is: {}/{}".format(self.player.get_score(), len(self.quiz))

    def get_final_message(self):
        return "You've completed the quiz.\nYour final score was: {}/{}".format(self.player.get_score(), len(self.quiz))

    def start(self):
        for question in self.quiz:
            answer = self.get_user_answer(question)
            is_correct, correct_answer = self.check_answer(answer, question)
            if is_correct:
                self.player.increment_score()
            print(self.get_result_message(is_correct, correct_answer))
            print(self.get_score_message())
            print()
        print(self.get_final_message())
