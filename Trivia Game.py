# Sarah Fine, Dante Diwan, Lorraine Jem, Michael Melnikas 
# CS2a Pop Culture Trivia Game

from collections import namedtuple
import random

"""
    This game will test your knowledge of the pop culture from the 1960's to 2017.
    Play in single-player or in multi-player mode and see who knows the most about the pop culture from the different
    eras. You will be asked up to 50 multiple choice questions with 4 possible answers.
    Type the letter of the answer to the question and if you are correct you will be rewarded points based
    on the level of difficulty of the questions. If you answer incorrectly, you will have the opportunity to attempt
    two more times,each time the points you would receive from answering that question correctly the first time
    decreasing. At the end of the game, whoever has the highest points wins the game!
"""

###################
# DATA STRUCTURES #
###################

# A Player has a Name and a Score.
Player = namedtuple("Player", "name score")

# A Question has a Prompt, a CorrectAnswer, and three WrongAnswers.
Question = namedtuple("Question", "prompt correct_answer wrong_answer_1 wrong_answer_2 wrong_answer_3")

#############
# FUNCTIONS #
#############


def import_questions(decade):
    """
    Imports questions from csv files, turns them into named tuples.
    Required files: 60s.csv, 70s.csv, 80s.csv, 90s.csv, 00s.csv, 10s.csv
    :param decade: Takes in 6, 7, 8, 9, 0, or 1 as the decade.
    """
    pass  # TODO


def reset():
    """
    Resets the player scores to zero, current player to random.
    """
    pass  # TODO


def random_player():
    """
    :return: a number between 0 and the number of players to signify which player is going to go first
    """
    return random.randint(0, num_players-1)


def is_game_over():
    """
    Game is over if a player has reached the max score or question bank is empty
    :return: True if game is over
    """
    pass  # TODO


def play_a_round():
    """
    Plays one "round" of trivia
    - Accesses random question from current question bank
    - Randomizes order of answers
    - Asks question to current player
    - Checks if given answer is correct
    - Increments player score when question is correct
    - Increments current player
    """
    pass  # TODO


def game_over():
    """
    Prints final scores, selects final winner, asks if you want to play again
    """
    pass  # TODO

########
# MAIN #
########

if __name__ == "__main__":

    # Instantiate play_again as true to make the while loop later actually work
    play_again = True

    # prompt for player number and names
    num_players = input("How many players are playing?")
    list_of_players = []
    for player in range(1, num_players):
        name = raw_input("What is the name of Player %d?" % player)
        new_player = Player(name=name, score=0)
        list_of_players.append(new_player)

    # prompt for maximum score game will go to
    max_score = input("What is the maximum points you would like to play to?")

    while play_again:
        reset()  # reset player scores to 0, don't reset number of wins
        decade = input("Which decade would you like? Enter a number signifying the first digit of the decade, i.e. 6 "
                       "for 60's")
        import_questions(decade=decade)
        while not is_game_over():  # check each player score against max score
            play_a_round()  # Prompt currentplayer with a question
        game_over()  # Game over screen, prompt to play again
