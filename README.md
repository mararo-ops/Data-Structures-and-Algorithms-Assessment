# Expression Balancer

This Python module provides a function, is_balanced(expression), that determines whether a given string expression containing parentheses, curly braces, and square brackets is balanced. An expression is considered balanced if each opening bracket has a corresponding closing bracket in the correct order.
Usage

python

from expression_balancer import is_balanced

expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

# Sequence Duplicate Remover

This Python module offers a function, remove_duplicates(sequence), designed to take a sequence (list or tuple) and return a new sequence with duplicates removed while preserving the original order of elements.
Usage

python

from sequence_duplicate_remover import remove_duplicates

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]

# Word Frequency Counter

This Python module provides a function, word_frequency(sentence), that takes a sentence and returns a dictionary containing the frequency of each word. Punctuation is ignored, and words are considered in a case-insensitive manner.
Usage

python

from word_frequency_counter import word_frequency

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

# License

This project is licensed under the MIT License - see the LICENSE file for details.
