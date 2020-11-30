from player import Player
import random


class Game:

    def __init__(self):
        random.shuffle(Player.shoe)
        self.player = Player()
        self.computer = Player(dealer=True)

    def determine_winner(self) -> str:
        """
            Determine the winner according to the blackjack rules
            Player wins if one of the following is true:
                - Player has a score of 21
                - Computer has a score greater than 21
                - Player's score is greater than computer's score
        """
        computer_too_many = self.computer.score > 21
        player_over_computer = self.player.score > self.computer.score
        tie = (self.player.score == self.computer.score) or (self.player.blackjack and self.computer.blackjack)
        if tie:
            return "It's a tie."
        elif computer_too_many:
            return "Too many for the computer. You win!"
        elif player_over_computer:
            return "You win!"
        else:
            return "You lose."

    def play(self):
        """
            Play one blackjack game
        """
        print("Your cards: {}".format(self.player.get_cards()))
        print("Computer's first card: {}".format(
            [self.computer.get_first_card()]))
        keep_dealing = not self.player.blackjack
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
        print("Your final score: {}".format(self.player.score))
        message = ""
        if self.player.score > 21:
            message = "Too many. You lose."
        else:
            keep_dealing = True
            while keep_dealing:
                self.computer.deal()
                if self.computer.score > 16:
                    keep_dealing = False
                    print("Computer's cards: {}".format(self.computer.get_cards()))
            print("Computer's final score: {}".format(self.computer.score))
            message = self.determine_winner()
        print(message)
