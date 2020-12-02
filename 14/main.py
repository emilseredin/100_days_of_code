from game import Game


def main():
    keep_playing = True
    while keep_playing:
        game = Game()
        game.play()
        answer = input("Start new game? Type 'y' or 'n': ").strip()
        if not answer == 'y':
            keep_playing = False


if __name__ == "__main__":
    main()
