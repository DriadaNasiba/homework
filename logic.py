import random
import configparser

class GuessNumberGame:
    def __init__(self, min_number, max_number, attempts, initial_capital):
        self.min_number = min_number
        self.max_number = max_number
        self.attempts = attempts
        self.capital = initial_capital
        self.target_number = random.randint(self.min_number, self.max_number) # Генерация числа в конструкторе

    def play(self):
        print(f"Welcome to the game 'Guess the number'!")
        print(f'You have {self.attempts} attempts and initial capital {self.capital}. ')

        for attempt in range(self.attempts):
            print(f"\nAttempts {attempt + 1} from {self.attempts}. Your capital: {self.capital}.")

            if self.capital <= 0:
                print(f'You lost all your money! Game over!')
                break

            try:
                bet = float(input(f'Place your bet: '))
                if bet > self.capital:
                    print('The bet is greater than your capital! Try again.')
                    continue
            except ValueError:
                print("Invalid bet amount. Please enter a number.")
                continue

            try:
                guess = int(input(f"Guess the number from {self.min_number} to {self.max_number}: "))
            except ValueError:
                print("Invalid guess. Please enter an integer.")
                continue

            if guess == self.target_number:
                print(f'Congratulations! You guessed the number {self.target_number}. You double your bet!')
                self.capital += bet
            else:
                print(f'Wrong! The number was {self.target_number}. You lost your bet.')
                self.capital -= bet # Уменьшаем капитал на ставку
            self.target_number = random.randint(self.min_number, self.max_number)
        if self.capital > 0:
            print(f'\nGame Over. Your capital: {self.capital}. ')
        else:
            print("You couldn't earn any money. Try again.")