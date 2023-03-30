import random


class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def get_question(self):
        return self.question

    def get_options(self):
        return self.options

    def get_answer(self):
        return self.answer

    def __str__(self):
        return f"{self.question}\n{self.options}"


questions = [
    Question("What is the capital of France?", ["A) Madrid", "B) Paris", "C) Rome", "D) Berlin"], 2),
    Question("Who painted the Mona Lisa?",
             ["A) Leonardo da Vinci", "B) Vincent van Gogh", "C) Pablo Picasso", "D) Michelangelo"], 1),
    Question("What is the smallest planet in our solar system?", ["A) Mercury", "B) Venus", "C) Earth", "D) Mars"], 1),
    Question("Who is the current president of the United States?",
             ["A) Donald Trump", "B) Joe Biden", "C) Barack Obama", "D) George W. Bush"], 2),
    Question("What is the highest mountain in the world?",
             ["A) Mount Everest", "B) Mount Kilimanjaro", "C) Mount Mc Kinley", "D) Mount Fuji"], 1),
    Question("What is the largest mammal in the world?",
             ["A) Elephant", "B) Blue Whale", "C) Polar Bear", "D) Gorilla"], 2),
    Question("What is the capital of Australia?", ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Brisbane"], 3),
    Question("Who wrote the novel 'To Kill a Mockingbird'?",
             ["A) J.K. Rowling", "B) Harper Lee", "C) Ernest Hemingway", "D) Mark Twain"], 2),
    Question("What is the currency of Japan?", ["A) Yen", "B) Euro", "C) Dollar", "D) Pound"], 1),
    Question("What is the smallest continent by land area?", ["A) Europe", "B) Africa", "C) Asia", "D) Australia"], 4)
]


def play_game():
    player1_score = 0
    player2_score = 0

    random.shuffle(questions)

    for i in range(5):
        print(f"Question {i + 1} for Player 1:")
        print(questions[i])
        choice = int(input("Enter your choice (1-4): "))
        if choice == questions[i].get_answer():
            print("Correct!")
            player1_score += 1
        else:
            print("Incorrect!")

        print(f"Question {i + 1} for Player 2:")
        print(questions[i + 5])
        choice = int(input("Enter your choice (1-4): "))
        if choice == questions[i + 5].get_answer():
            print("Correct!")
            player2_score += 1
        else:
            print("Incorrect!")

    print(f"Player 1 score: {player1_score}")
    print(f"Player 2 score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("Tie game!")


play_game()
