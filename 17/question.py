class Question:

    def __init__(self, text, answer):
        self.text = text
        self.correct_answer = answer

    def get_text(self):
        return self.text

    def get_correct_answer(self):
        return self.correct_answer
