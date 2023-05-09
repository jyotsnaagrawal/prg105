import questions
import random


def main():
    q1 = questions.Questions("What is the capital of France?", "Madrid", "Paris", "Rome", "Berlin", "B")
    q2 = questions.Questions("Who painted the Mona Lisa?",
                             "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso", "Michelangelo", "A")
    q3 = questions.Questions("What is the smallest planet in our solar system?", "Mercury",
                             "Venus", "Earth", "Mars", "A")
    q4 = questions.Questions("Who is the current president of the United States?",
                             "Donald Trump", "Joe Biden", "Barack Obama", "George W. Bush", "B")
    q5 = questions.Questions("What is the highest mountain in the world?",
                             "Mount Everest", "Mount Kilimanjaro", "Mount Mc Kinley", "Mount Fuji", "A")
    q6 = questions.Questions("What is the largest mammal in the world?",
                             "Elephant", "Blue Whale", "Polar Bear", "Gorilla", "B")
    q7 = questions.Questions("What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", "C")
    q8 = questions.Questions("Who wrote the novel 'To Kill a Mockingbird'?",
                             "J.K. Rowling", "Harper Lee", "Ernest Hemingway", "Mark Twain", "B")
    q9 = questions.Questions("What is the currency of Japan?", "Yen", "Euro", "Dollar", "Pound", "A")
    q10 = questions.Questions("What is the smallest continent by land area?", "Europe", "Africa", "Asia", "Australia",
                              "D")
    all_the_questions = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    print("******Player One******")
    player_1 = ask(all_the_questions)
    print("******Player Two******")
    player_2 = ask(all_the_questions)

    if player_1 == player_2:
        print("it is a tie!")
    elif player_1 > player_2:
        print("Player one is winner")
    else:
        print("Player two is winner")


def ask(all_questions):
    correct = 0
    for item in range(2):
        player_questions = random.choice(all_questions)
        print(player_questions.get_question())
        print("A. " + player_questions.get_answer1())
        print("B. " + player_questions.get_answer2())
        print("C. " + player_questions.get_answer3())
        print("D. " + player_questions.get_answer4())
        player_response = input("\nPlease enter the letter of your answer: ")

        if player_response.upper() == player_questions.get_correct_answer():
            print("\nWhoopee! You got that one\n\n")
            correct += 1
        else:
            print("\nSo sad. Better luck next time.\n\n")
    return correct


main()

