import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 7

    print("Вітаємо у грі 'Вгадай число'!")
    print("Я загадав число від 1 до 100. У вас є 7 спроб, щоб вгадати його.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input("Спроба " + str(attempt) + ": Введи своє число: "))
        except ValueError:
            print("Будь ласка, введіть ціле число.")
            continue

        if guess < number:
            print("Занадто маленьке.")
        elif guess > number:
            print("Занадто велике.")
        else:
            print("Вітаю! Ти вгадав число " + str(number) + " за " + str(attempt) + " спроб!")
            break
    else:
        print("На жаль, ти не вгадав. Загадане число було " + str(number) + ".")

if __name__ == "__main__":
    guess_the_number()
