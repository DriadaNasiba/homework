import configparser
from logic import GuessNumberGame

def main():
    config = configparser.ConfigParser()
    try:
        config = config.read("config/settings.ini")
        min_number = config.getint('game', 'min_number')
        max_number = config.getint('game', 'max_number')
        attempts = config.getint('game', 'attempts')
        initial_capital = config.getint('game', 'initial_capital')

        game = GuessNumberGame(min_number, max_number, attempts, initial_capital)
        game.play()

if __name__ == "__main__":
    main()
