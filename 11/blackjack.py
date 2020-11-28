from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.computer = Player(dealer=True)

    def determine_winner(self, player: int, computer: int) -> str:
        """
            Determine the winner according to the blackjack rules
            Player wins if one of the following is true:
                - Player has a score of 21
                - Computer has a score greater than 21
                - Player's score is greater than computer's score
        """
        player_blackjack = player == 21
        computer_too_many = computer > 21
        player_over_computer = player > computer
        tie = player == computer
        if tie:
            return "It's a tie."
        elif player_blackjack or computer_too_many or player_over_computer:
            return "You win!"
        else:
            return "You lose."

    def play(self):
        """
            Play one blackjack game
        """
        print("Your cards: {}".format(self.player.get_cards()))
        print("Computer's first card: {}".format(self.computer.get_cards()))
        keep_dealing = True
        while keep_dealing:
            answer = input(
                "Type 'y' to get another card, type 'n' to pass: ").strip()
            if answer == 'n':
                keep_dealing = False
            else:
                self.player.deal()
                if self.player.score > 21:
                    keep_dealing = False
                print("Your cards: {}".format(self.player.get_cards()))
                print("Your score: {}".format(self.player.score))
        print("Your final hand: {}".format(self.player.get_cards()))
        print("Your final score: {}".format(self.player.score))
        message = ""
        if self.player.score > 21:
            message = "You lose."
        else:
            keep_dealing = True
            while keep_dealing:
                self.computer.deal()
                if self.computer.score > 16:
                    keep_dealing = False
            print("Computer's final hand: {}".format(self.computer.get_cards()))
            print("Computer's final score: {}".format(self.computer.score))
            message = self.determine_winner(
                player=self.player.score, computer=self.computer.score)
        print(message)
