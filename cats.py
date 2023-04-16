"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    """def select(p):
        if p <= len(paragraphs):
            return True
        else:
            return False"""
    passing = [item for item in paragraphs if select(item)]

    if k < len(passing):
        return passing[k]
    if k >= len(passing):
        return ''
    # END PROBLEM 1
"""paragraphs[k] """
"""choose(paragraphs[k], select, k + 1)"""


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def true_false(paragraphs):
        for word in split(lower(remove_punctuation(paragraphs))):
            if word in topic:
                return True
        return False
    return true_false

    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    all = 0
    split_typed = split(typed)
    split_reference = split(reference)
    min_length = min(len(split_typed), len(split_reference))
    if (len(typed) == 0):
        return 0.0
    for item in range(min_length):
        if (split_reference [item] == split_typed[item]):
            all += 1
    return 100 * all/len(split_typed)
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed)/5 * 60/elapsed
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    def amount_of_diff(one_word):
        return diff_function(user_word, one_word, limit)
    if diff_function(user_word, min(valid_words, key=amount_of_diff), limit) > limit:
        return user_word
    return min(valid_words, key=amount_of_diff)

    # END PROBLEM 5


def sphinx_swap(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    word_difference = abs(len(goal) - len(start))
    def helper_func(start, goal, word_difference):
        if start[0] != goal[0]:
            word_difference += 1
        if len(start) == 1:
            return word_difference
        elif len(goal) == 1:
            return word_difference
        elif word_difference > limit:
            return word_difference
        else:
            return helper_func(start[1:len(start)], goal[1:len(goal)], word_difference)
    return helper_func(start, goal, word_difference)

    # END PROBLEM 6


def feline_fixes(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""


    if limit == -1:
        return False
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
    elif len(start) == 0 or len(goal) == 0:
        return len(start) + len(goal)

    elif start[len(start) - 1] == goal[len(goal) - 1]:
        return feline_fixes(start[0:len(start) - 1], goal[0:len(goal) - 1], limit)

        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = feline_fixes(start, goal[0:len(goal) - 1], limit - 1) + 1
        remove_diff = feline_fixes(start[0:len(start) - 1], goal, limit - 1) + 1
        substitute_diff = feline_fixes(start[0:len(start) - 1], goal[0:len(goal) - 1], limit - 1) + 1
        return min(add_diff, remove_diff, substitute_diff)
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    count = 0
    correct = 0
    for i in typed:
        if typed[count] == prompt[count]:
            count += 1
            correct += 1
        else:
            break
    send({'id': id, 'progress': correct / len(prompt)})
    return (correct / len(prompt))


           # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    total_time = []
    for num in times_per_player:
        individual_time = []

        for inner_num in range(1, len(num)):
            individual_time.append(num[inner_num] - num[inner_num - 1])

        total_time.append(individual_time)
    return game(words, total_time)

    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    word_winner = []
    for item in range(len(players)):
        word_winner.append([])
    for word_items in words:
        smallest_holder = float('inf')
        for player_item in players:
            times = time(game, player_item, word_items)
            if times < smallest_holder:
                smallest_holder, best = times, player_item
        word_winner[best].append(word_at(game, word_items))
    return word_winner
    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
