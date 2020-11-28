from blackjack import Game


def main():
    keep_playing = True
    while keep_playing:
        game = Game()
        game.play()
        answer = input(
            "Do you want to play one more game? Type 'y' or 'n': ").lower().strip()
        if answer == 'n':
            keep_playing = False
        print()


if __name__ == "__main__":
    main()
