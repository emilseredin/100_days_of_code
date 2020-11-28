class Card:

    def __init__(self, face):
        self.face = face
        if face == 'A':
            self.value = 11
        elif face == '10' or face == 'K' or face == 'Q' or face == 'J':
            self.value = 10
        else:
            self.value = int(face)
